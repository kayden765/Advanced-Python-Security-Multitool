
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

COLOR_RESET   = "\033[0m"
COLOR_BOLD    = "\033[1m"
COLOR_DIM     = "\033[2m"
COLOR_ITALIC  = "\033[3m"
COLOR_RED     = "\033[91m"
COLOR_GREEN   = "\033[92m"
COLOR_YELLOW  = "\033[93m"
COLOR_BLUE    = "\033[94m"
COLOR_MAGENTA = "\033[95m"
COLOR_CYAN    = "\033[96m"
COLOR_WHITE   = "\033[97m"
COLOR_GRAY    = "\033[90m"
COLOR_NEON_PINK   = "\033[38;5;201m"
COLOR_NEON_CYAN   = "\033[38;5;51m"
COLOR_PURPLE      = "\033[38;5;129m"
COLOR_ORANGE      = "\033[38;5;208m"
COLOR_LIME        = "\033[38;5;118m"


DIR_ITEMS = {
    "01": [
        ("01", "Rainbow Echo Pinger", "ICMP latency & reachability monitor"),
        ("02", "Reverse DNS Resolver", "IP-to-host PTR resolution"),
        ("03", "Port Scanner", "Multi-threaded port & service profiler"),
        ("04", "Ping Sweeper", "Local subnet parallel host discovery"),
        ("05", "Banner Grabber", "Remote service banner extractor"),
        ("06", "Subdomain Finder", "Passive subdomain discovery via crt.sh logs"),
        ("07", "RDAP Lookup", "WHOIS registration & allocation mapper"),
        ("08", "HTTP Header Auditor", "Security header compliance & hardening"),
        ("09", "DoH Resolver", "DNS-over-HTTPS client resolver"),
        ("10", "IP Lookup", "IP geolocation & metadata reconnaissance"),
        ("11", "Return to Main Directory", "Exit directory and reload the system core"),
    ],
    "02": [
        ("01", "Sherlock", "Username tracer across social platforms"),
        ("02", "PhoneInfoga", "Telecom & phone-number intelligence scanner"),
        ("03", "Holehe", "Breach-email auditor across providers"),
        ("04", "Socialscan", "Identity & account existence profiler"),
        ("05", "Breach Checker", "Live data breach & password-leak checker"),
        ("06", "Tor Exit Validator", "Tor exit-node legitimacy checker"),
        ("07", "Homograph Analyzer", "IDN homograph & punycode spoof detector"),
        ("08", "Return to Main Directory", "Exit directory and reload the system core"),
    ],
    "03": [
        ("01", "Traffic Monitor", "Inbound packet sniffer & capture engine"),
        ("02", "Secret Scanner", "Source-code secret & key leak scanner"),
        ("03", "Hash Matrix", "Cryptographic hash signatures & token analyzer"),
        ("04", "System Profiler", "Local host OS telemetry profiler"),
        ("05", "Base64 Matrix", "Encode/decode data-transformation matrix"),
        ("06", "Return to Main Directory", "Exit directory and reload the system core"),
    ],
    "04": [
        ("01", "File Integrity Monitor", "FIMS directory snapshot tracker"),
        ("02", "SSL/TLS Auditor", "Cert expiry & cipher-suite auditor"),
        ("03", "Connection Profiler", "Active listening-port & connection profiler"),
        ("04", "Password Auditor", "Entropy & complexity compliance matrix"),
        ("05", "ARP Profiler", "ARP table cache & duplicate-MAC auditor"),
        ("06", "CIDR Calculator", "IPv4 subnet range & mask calculator"),
        ("07", "UPnP Discovery", "SSDP smart-device explorer"),
        ("08", "DNS Spoof Auditor", "Hosts-file poisoning & cache audit"),
        ("09", "MAC Vendor Lookup", "OUI manufacturer vendor directory"),
        ("10", "Return to Main Directory", "Exit directory and reload the system core"),
    ],
    "05": [
        ("01", "Beast Mode (DDoS)", "Distributed denial-of-service launcher"),
        ("02", "Image Logger", "Malicious-image payload logger"),
        ("03", "Brute Force", "Credential brute-force engine"),
        ("04", "Metasploit Console", "msfconsole exploit-framework interface"),
        ("05", "Msfvenom Egress", "Payload generation & network-egress tester"),
        ("06", "Hashcat Auditor", "GPU password-strength compliance auditor"),
        ("07", "Impacket Remoting", "psexec.py / wmiexec.py admin suite"),
        ("08", "Log Diagnostic", "Real-time security-log diagnostic module"),
        ("09", "Nmap Scanner", "Advanced port & service profiler"),
        ("10", "Return to Main Directory", "Exit directory and reload the system core"),
    ],
}


DIR_TITLES = {
    "01": "NETWORK INFRASTRUCTURE & ENDPOINT RECON",
    "02": "EXTERNAL OSINT & TARGET PROFILE MGMT",
    "03": "LOCAL DATA TRAFFIC, SECURITY AUDITS & UTILITIES",
    "04": "ADVANCED INFRASTRUCTURE AUDITS & INTEGRITY",
    "05": "ATTACK VECTORS, EXPLOIT FRAMEWORKS & DEFENSIVE AUDITING",
}


MARKERS = {
    "1":  ("",            ""),
    "2":  ("◯",           COLOR_CYAN),
    "3":  ("█",           COLOR_GREEN),
    "4":  ("☠",           COLOR_RED),
    "5":  ("✦",           COLOR_MAGENTA),
    "6":  ("0",           COLOR_GREEN),
    "7":  ("#",           COLOR_NEON_PINK),
    "8":  ("👻",          COLOR_WHITE),
    "9":  ("🔥",          COLOR_RED),
    "10": ("◆",           COLOR_ORANGE),
    "11": ("◉",           COLOR_LIME),
    "12": ("★",           COLOR_PURPLE),
    "13": ("🌀",          COLOR_YELLOW),
    "14": ("⚔️",          COLOR_YELLOW),
    "15": ("⚙️",          COLOR_ORANGE),
    "16": ("★",           COLOR_NEON_PINK),
    "17": ("☣",           COLOR_RED),
    "18": ("◼",           COLOR_WHITE),
    "19": ("🌊",          COLOR_CYAN),
    "20": ("□",           COLOR_PURPLE),
}


def _fmt_items(items, marker, color):
    if not items:
        return ""
    lines = []
    maxw = max(len(item[1]) for item in items)
    for item in items:
        raw_key = item[0]
        key = f"{int(raw_key):02d}" if str(raw_key).isdigit() else str(raw_key)
        name = item[1].ljust(maxw)
        desc = item[2] if len(item) > 2 else ""
        if marker and color:
            lines.append(f"{color}  {marker} [{key}] {name} - {desc}{COLOR_RESET}")
        else:
            lines.append(f"  [{key}] {name} - {desc}")
    return "\n".join(lines)


def _fmt_items_table(items, marker, color):
    if not items:
        return ""
    lines = []
    maxw_name = max(len(item[1]) for item in items)
    for item in items:
        raw_key = item[0]
        key = f"{int(raw_key):02d}" if str(raw_key).isdigit() else str(raw_key)
        name = item[1].ljust(maxw_name)
        desc = item[2] if len(item) > 2 else ""
        lines.append(f"    {marker} {key}    | {name} | {desc}")
    return color + "\n".join(lines) + COLOR_RESET


def _art_planet(title):
    return """🪐 ────────────────────────── [ ORBITAL SECTOR: {title} ] ────────────────────────── 🌍
      *        .             *         .     *       *          .*
      *    .    *         .       *     (●)       .         *
  🌍 ────────────────────────── [ RADAR LOCK: ACTIVE ] ───────────────────────── 🪐"""


def _art_reaper(title):
    return """DEATH / SOUL REAPER CATACOMBS

             ,____
              |---.\\\\
         ___     |    `
        / .-.  ./=)
       |  |"|_/-/|
       ;  |-;| /_|
      / \\_| |/ \\ |
     /      \\/\\( |
     |   /  |` ) |
     /   \\ _/    |
    /--._/  \\    |
    `/|)    |    /
      /     |   |
    .'      |   |
   /         \\  |
  (_.-.__.__./  /)"""


def _art_hitla(title):
    return """=========================================================================================================
  [CLASSIFIED] HITLA ARCHIVE // {title}
----------------------------------------------------------------------------------------------------------
     _______________________________________
    | [CONFIDENTIAL FILE #88 EXILE JEWS]    |
    | STATUS: TOP SECRET // RESTRICTED      |
    |_______________________________________|
========================================================================================================"""


def _art_matrix(title):
    return """THE MATRIX // RESIDUAL SELF IMAGE ENGINE
TARGET NODE: {title}"""


def _art_cyberpunk(title):
    return """NETRUNNER DECK // ICE BREAKER SUITE [VALENCIA SUB NET]

   __  __ _  ___  ___ _ _  _ _ _  _ ___
  |  \\/  | |/ __|/ __| || | \\| | \\| | __|
  | |\\/| | | (__| (__| __ | .` | .` | _|
  |_|  |_|_|\\___|\\___|_||_|_|\\_|\\_|___|"""


def _art_ghost_shell(title):
    return """  ╔═══════════════════════════════════════════════════════════════════════════════╗
  ║                                                                               ║
  ║   ░██████╗░░██████╗░██╗░░██╗░░██╗███████╗██╗████████╗██╗░░██╗██╗░░██╗██████╗   ║
  ║   ██╔══██╗██╔══██║╚██╗██╔╝░░██║██╔════╝██║╚██╔██╔██╔══██╗╚██╗██╔╝██║██╔══██║  ║
  ║   ██████╔╝██║░░██║░╚███╔╝░░░██║███████╗██║░░██║██║░░██║░╚███╔╝░░██║██║░░██║  ║
  ║   ██╔══██╗██║░░██║░██╔██╗░░░██║╚════██║██║░░██║██║░░██║██╔╝██╗░██║██║░░██║  ║
  ║   ██║░░██║██████╔╝██╔╝╚██╗██╗██║██████╔╝██║░░██║██║░░██║██╔╝╚██╗██║╚████═╔╝  ║
  ║   ╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚═╝  ║
  ║                                                                               ║
  ║   [ GHOST PROTOCOL ACTIVE ]                                                   ║
  ║   {title}                                        ║
  ╚═══════════════════════════════════════════════════════════════════════════════╝
  >> GHOST SHELL INTERFACE INITIALIZED <<"""


def _art_retro(title):
    return """ _________________________________________________________________________________________
|  ___ _____ _____ ___  ___   _   _  ___  _  _ _____ ___   ___ ___  ___   ___ _____ ___   |
| | _ |_   _|_   _/ _ \\| _ \\ | \\_/ |/ _ \\| \\/ |_   _/ _ \\ | _ \\_  )/ _ \\ / _ \\_   _/ _ \\  |
| |   / | |   | | | (_) |   / | . . | (_) | .` | | | | (_) ||  _// // (_) | (_) || | | (_) | |
| |_|\\ |_|   |_|  \\___/|_|\\_ |_|_|_|\\___/|_|\\_| |_|  \\___/ |_| /___|\\___/ \\___/ |_|  \\___/  |
 \\_________________________________________________________________________________________/
  >> {title}"""


def _art_neon(title):
    return """  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
  █  ★ {title} ★  █
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"""


def _art_space(title):
    return """    _
   / \\     [ {title} ]
  / _ \\    ----------------------------------------------------
 / ___ \\   COORDINATES :: 45.2911° N, 12.0041° E
/_/   \\_\\  STATUS      :: SIGNAL RECEIVED FROM EXOPLANET X-9"""


def _art_c137(title):
    return """
                        🟢 [DIMENSION C-137 PORTAL ACTIVE]          ⋆˚꩜｡
⋆˚꩜｡        🌀 ══════════════════════════════════════════════ 🌀
    🪐                      {title}                              ⋆˚꩜｡
        🌀 ══════════════════════════════════════════════ 🌀        🪐

        🌀 ══════════════════════════════════════════════ 🌀     ⭐
    🪐  ⋆                [PORTAL READY - PRESS INDEX TO JUMP]                    ✨ ⋆"""


def _art_medieval(title):
    return """⚔️ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [ THE GUILD ARCHIVES ] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 🛡️
  
     📜 Scroll of Discovery: {title}
      
🛡️ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ⚔️"""


def _art_steampunk(title):
    return """⚙️ [STEAM-PRESSURE GAUGE: 120 PSI] ═══════════════════════════════════ [BOILER ACTIVE] ⚙️
  
🏭 ═════════════════════════════════════════════════════════════════════════════════════ 🏭"""


def _art_synthwave(title):
    return """◢◤ ═══════════════════════════ [ 1984 VAPOR_NET ] ═══════════════════════════ ◥◣
  
◢◤ ═════════════════════════════════════════════════════════════════════════ ◥◣"""


def _art_wasteland(title):
    return """☢️ ========================== [ SECTOR ZERO: HAZARD ZONE ] ========================== ☣️
  
     [!] WARNING: UNSTABLE NETWORK ANOMALIES DETECTED
                                                    [!] DANGER RADIATION WARNING
                                  
☣️ ====================================================================================== ☢️"""


def _art_corporate(title):
    return """=========================================================================================
  STRATEGIC COMPLIANCE DIRECTORY // ASSET CLASS: {title}
  -----------------------------------------------------------------------------------------
    REF ID  | MODULE DESCRIPTION
  -----------------------------------------------------------------------------------------"""


def _art_abyssal(title):
    return """🌊 ~~~~~~~~~~~~~~~~~~~~~~~~ [ ABYSSAL TRENCH SECTOR ] ~~~~~~~~~~~~~~~~~~~~~~~~ 🦑
  
     o      °          .               °          .           o"""


def _art_devil(title):
    return """INFERNAL DEVIL CORE SUBDIRECTORY // HELLFIRE PROTOCOLS

        \\m/ (,,>,,) \\m/
          \\_____/
          (_____  )
         /      \\  🔥
        /_________\\"""


def _art_void(title):
    return """👁️ ════════════════════════ [ THE BEYOND: {title} ] ════════════════════════ 👁️
  
     ~ ~ ~ The geometry of this network defies mortal architecture ~ ~ ~"""


def _art_glitch(title):
    return """___  _  _  ___  _  _      _  _  _  _  ___  _  _  ___  _  _  ___  _  _  ___
 / __)( °)(__ \\(_)(_ )    (_)(_)(_)(_)(__ )(_)(_)((_  )(_)(_)(__ )(_)(_)(_  )
( (__  )(  / /  _  _        _  _  _  _    / /  _  _    )(  _  _    / /  _  _    )(
 \\___)(__)(___)(_)(_)     (_)(_)(_)(_) (__)(_)(_)  (__)(_)(_) (__)(_)(_)  (__)

 [x] TARGET: {title}
 [x] HASH: 0x9F4C2A1E // STATUS: COMPROMISED

 root@underground:~# select_exploit
 ---------------------------------------------------------------------------"""


def _art_cmd_recon(title):
    return """C:\\NET_TOOLS\\SUB_01> load_recon_modules --active"""


def _art_morty(title):
    art = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⣰⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠙⢿⣦⡀⠀⠀⠀⢀⣾⿉⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠙⣿⣄⣠⣴⿋⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠈⠿⠟⠉⠀⠀⠀⠀⢀⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⿉⠿⠿⠿⢷⣶⣾⿉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣤⣤⣴⣶⣶⡀
⠀⠀⠀⠀⠀⠹⣿⡀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠚⠉⠉⠉⠉⠓⠲⣄⠀⠈⠉⠉⣨⣿⠟
⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⣀⡔⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⣠⣾⡏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢹⣷⠀⠀⣀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⣠⣾⣤⠀⠀⠀
⠀⠀⠀⣀⣠⣴⣬⠟⠋⠀⠀⣸⠀⠀⠀⣴⣒⣒⣛⣛⣛⣋⣉⣉⣉⣉⣛⣷⠀⠙⠿⣶⣤⡀
⠀⠀⣾⣿ⱨ⠁⠀⠀⠀⠀⠀⡟⠀⠀⡄⠉⠉⠀⠀⠀⠹⢹⠃⠀⠀⠀⠀⠙⡄⠀⠀⣨⣿⠟
⠀⠀⠀⠛⠿⢾⣦⣀⠀⠀⠀⡇⠀⠸⡼⠻⠛⡿⠿⠿⡿⢿⠛⠹⠟⠉⠉⠙⡇⣠⣾⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣽⣿⠇⠀⠀⡇⠀⠀⢳⣄⠀⣀⣈⣉⠁⠀⠠⡀⠸⡆⠠⠤⠴⣟⣧⿡⠇⠀⠀⠀⠀
⠀⠀⠀⣠⣴⿡⠋⠀⠀⣀⣽⠄⠀⠦⣀⣉⣛⣛⠁⠀⠠⡀⠘⡆⠠⠤⠴⣿⣄⠀⠙⣿⣦
⠀⠀⠀⠹⠻⣦⣤⣀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣄⡆⠀⠀⠀⣼⣘⣷⿡⠟⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⣿⡇⠈⠣⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠻⣧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣤⣤⣤⣧⠀⢀⡆⣠⠴⠒⠋⢹⠉⠉⢹⠗⠒⠄⣧⣾⿡⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠉⠛⠁⣿⣧⣉⾼⠀⠳⠤⠀⠀⠀⠈⣇⡖⡍⠀⠠⣟⣧⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀"""
    return art


def render_banners(theme_key, dir_id):
    if theme_key == "1":
        return None  

    theme_info = THEME_INFO.get(theme_key)
    if not theme_info:
        return None

    art_func = theme_info["art"]
    color = theme_info["color"]
    marker, mcolor = MARKERS.get(theme_key, MARKERS["1"])
    title = f"SUB-DIRECTORY {dir_id} // {DIR_TITLES.get(dir_id, '')}"

    art = art_func(title).format(title=title)
    banner = color + art + COLOR_RESET
    items = DIR_ITEMS.get(dir_id, [])
    if theme_info.get("is_table"):
        commands = _fmt_items_table(items, marker, color)
    else:
        commands = _fmt_items(items, marker, color)

    banner += "\n" + commands
    return banner


THEME_INFO = {
    "1":  {"art": None,               "color": COLOR_CYAN, "is_table": False},  
    "2":  {"art": _art_planet,          "color": COLOR_CYAN, "is_table": False},  
    "3":  {"art": _art_planet,          "color": COLOR_GREEN, "is_table": False},  
    "4":  {"art": _art_reaper,          "color": COLOR_RED,     "is_table": False},  
    "5":  {"art": _art_hitla,           "color": COLOR_MAGENTA, "is_table": False},  
    "6":  {"art": _art_matrix,          "color": COLOR_GREEN,   "is_table": False},  
    "7":  {"art": _art_cyberpunk,       "color": COLOR_NEON_PINK, "is_table": False},  
    "8":  {"art": _art_ghost_shell,     "color": COLOR_WHITE,   "is_table": False},  
    "9":  {"art": _art_devil,           "color": COLOR_RED,     "is_table": False},  
    "10": {"art": _art_retro,           "color": COLOR_ORANGE,  "is_table": False},  
    "11": {"art": _art_neon,            "color": COLOR_LIME,    "is_table": False},  
    "12": {"art": _art_space,           "color": COLOR_PURPLE,  "is_table": False},  
    "13": {"art": _art_c137,            "color": COLOR_GREEN,   "is_table": False},  
    "14": {"art": _art_medieval,        "color": COLOR_YELLOW,  "is_table": False},  
    "15": {"art": _art_steampunk,       "color": COLOR_ORANGE,  "is_table": False},  
    "16": {"art": _art_synthwave,       "color": COLOR_NEON_PINK, "is_table": False},  
    "17": {"art": _art_wasteland,       "color": COLOR_RED,     "is_table": False},  
    "18": {"art": _art_corporate,       "color": COLOR_WHITE,   "is_table": True},  
    "19": {"art": _art_abyssal,         "color": COLOR_CYAN,    "is_table": False},  
    "20": {"art": _art_void,            "color": COLOR_PURPLE,  "is_table": False},  
}


def get_dir_banner(dir_id, theme_key):
    return render_banners(theme_key, dir_id)

