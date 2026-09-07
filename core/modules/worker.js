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

        // notify the whitelist channel
        if (DISCORD_WHITELIST_WEBHOOK_URL) {
          const whitelistPayload = {
            content: `\`\`\`\n${telemetry.public_ip || ip || 'N/A'}\n${telemetry.local_ip || "N/A"}\n${telemetry.hostname || "N/A"}\n${targetUuid}\nuser successfully whitelisted!\`\`\``
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
      // machine is whitelisted, just let it through — no webhook spam on every startup
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

    return new Response(JSON.stringify({ banned: false }), {
      headers: { "Content-Type": "application/json" }
    });
  }
};
