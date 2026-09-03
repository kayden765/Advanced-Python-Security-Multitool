# ================================================================================
# CORE - Directory Banner Rendering Engine
# ================================================================================
# Themed banners for each subdirectory. Each theme renders a decorative header
# with a decorative art section above the command list below it.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# ANSI COLOR CODES (defined locally to avoid circular import with ui_theme)
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


# ---------------------------------------------------------------------------
# COMMAND DATA - Edit commands here (shared across all directory themes)
# Each directory has its own list of (key, name, description) tuples.
# To add/remove/rename a command, edit the list below.
# ---------------------------------------------------------------------------
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


# Directory display titles
DIR_TITLES = {
    "01": "NETWORK INFRASTRUCTURE & ENDPOINT RECON",
    "02": "EXTERNAL OSINT & TARGET PROFILE MGMT",
    "03": "LOCAL DATA TRAFFIC, SECURITY AUDITS & UTILITIES",
    "04": "ADVANCED INFRASTRUCTURE AUDITS & INTEGRITY",
    "05": "ATTACK VECTORS, EXPLOIT FRAMEWORKS & DEFENSIVE AUDITING",
}


# ---------------------------------------------------------------------------
# MARKERS - Visual markers per theme (used in command list)
# ---------------------------------------------------------------------------
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
    """Format command tuples into themed menu lines."""
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
    """Format command tuples as a table (used by Corporate theme)."""
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


# ---------------------------------------------------------------------------
# BANNER ARTS - Edit these to change the decorative art for each theme.
# Each function returns (banner_art_string, color_code, marker).
# The banner_art is the decorative header; commands are rendered separately.
# ---------------------------------------------------------------------------

def _art_planet(title):
    """ORBITAL SECTOR - space/planet theme"""
    return """🪐 ────────────────────────── [ ORBITAL SECTOR: {title} ] ────────────────────────── 🌍
      *        .             *         .     *       *          .*
      *    .    *         .       *     (●)       .         *
  🌍 ────────────────────────── [ RADAR LOCK: ACTIVE ] ───────────────────────── 🪐"""


def _art_reaper(title):
    """SOUL REAPER - death/reaper theme"""
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
    """HITLA ARCHIVE - classified/archive theme"""
    return """=========================================================================================================
  [CLASSIFIED] HITLA ARCHIVE // {title}
----------------------------------------------------------------------------------------------------------
     _______________________________________
    | [CONFIDENTIAL FILE #88 EXILE JEWS]    |
    | STATUS: TOP SECRET // RESTRICTED      |
    |_______________________________________|
========================================================================================================"""


def _art_matrix(title):
    """MATRIX - code rain theme"""
    return """THE MATRIX // RESIDUAL SELF IMAGE ENGINE
TARGET NODE: {title}"""


def _art_cyberpunk(title):
    """CYBERPUNK - netrunner deck theme"""
    return """NETRUNNER DECK // ICE BREAKER SUITE [VALENCIA SUB NET]

   __  __ _  ___  ___ _ _  _ _ _  _ ___
  |  \\/  | |/ __|/ __| || | \\| | \\| | __|
  | |\\/| | | (__| (__| __ | .` | .` | _|
  |_|  |_|_|\\___|\\___|_||_|_|\\_|\\_|___|"""


def _art_ghost_shell(title):
    """GHOST SHELL - phantom/hacker theme"""
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
    """RETRO - 80s synthwave theme"""
    return """ _________________________________________________________________________________________
|  ___ _____ _____ ___  ___   _   _  ___  _  _ _____ ___   ___ ___  ___   ___ _____ ___   |
| | _ |_   _|_   _/ _ \\| _ \\ | \\_/ |/ _ \\| \\/ |_   _/ _ \\ | _ \\_  )/ _ \\ / _ \\_   _/ _ \\  |
| |   / | |   | | | (_) |   / | . . | (_) | .` | | | | (_) ||  _// // (_) | (_) || | | (_) | |
| |_|\\ |_|   |_|  \\___/|_|\\_ |_|_|_|\\___/|_|\\_| |_|  \\___/ |_| /___|\\___/ \\___/ |_|  \\___/  |
 \\_________________________________________________________________________________________/
  >> {title}"""


def _art_neon(title):
    """NEON - glowing neon theme"""
    return """  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
  █  ★ {title} ★  █
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"""


def _art_space(title):
    """DEEP SPACE - cosmic/space theme"""
    return """    _
   / \\     [ {title} ]
  / _ \\    ----------------------------------------------------
 / ___ \\   COORDINATES :: 45.2911° N, 12.0041° E
/_/   \\_\\  STATUS      :: SIGNAL RECEIVED FROM EXOPLANET X-9"""


def _art_c137(title):
    """DIMENSION C-137 - Rick & Morty portal theme"""
    return """
                        🟢 [DIMENSION C-137 PORTAL ACTIVE]          ⋆˚꩜｡
⋆˚꩜｡        🌀 ══════════════════════════════════════════════ 🌀
    🪐                      {title}                              ⋆˚꩜｡
        🌀 ══════════════════════════════════════════════ 🌀        🪐

        🌀 ══════════════════════════════════════════════ 🌀     ⭐
    🪐  ⋆                [PORTAL READY - PRESS INDEX TO JUMP]                    ✨ ⋆"""


def _art_medieval(title):
    """MEDIEVAL - guild archives theme"""
    return """⚔️ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [ THE GUILD ARCHIVES ] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 🛡️
  
     📜 Scroll of Discovery: {title}
      
🛡️ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ⚔️"""


def _art_steampunk(title):
    """STEAMPUNK - industrial/boiler theme"""
    return """⚙️ [STEAM-PRESSURE GAUGE: 120 PSI] ═══════════════════════════════════ [BOILER ACTIVE] ⚙️
  
🏭 ═════════════════════════════════════════════════════════════════════════════════════ 🏭"""


def _art_synthwave(title):
    """SYNTHWAVE - vaporwave/digital theme"""
    return """◢◤ ═══════════════════════════ [ 1984 VAPOR_NET ] ═══════════════════════════ ◥◣
  
◢◤ ═════════════════════════════════════════════════════════════════════════ ◥◣"""


def _art_wasteland(title):
    """WASTELAND - hazard zone theme"""
    return """☢️ ========================== [ SECTOR ZERO: HAZARD ZONE ] ========================== ☣️
  
     [!] WARNING: UNSTABLE NETWORK ANOMALIES DETECTED
                                                    [!] DANGER RADIATION WARNING
                                  
☣️ ====================================================================================== ☢️"""


def _art_corporate(title):
    """CORPORATE - compliance/strategic theme"""
    return """=========================================================================================
  STRATEGIC COMPLIANCE DIRECTORY // ASSET CLASS: {title}
  -----------------------------------------------------------------------------------------
    REF ID  | MODULE DESCRIPTION
  -----------------------------------------------------------------------------------------"""


def _art_abyssal(title):
    """ABYSSAL - ocean/deep sea theme"""
    return """🌊 ~~~~~~~~~~~~~~~~~~~~~~~~ [ ABYSSAL TRENCH SECTOR ] ~~~~~~~~~~~~~~~~~~~~~~~~ 🦑
  
     o      °          .               °          .           o"""


def _art_devil(title):
    """DEVIL CORE - hellfire/infernal theme"""
    return """INFERNAL DEVIL CORE SUBDIRECTORY // HELLFIRE PROTOCOLS

        \\m/ (,,>,,) \\m/
          \\_____/
          (_____  )
         /      \\  🔥
        /_________\\"""


def _art_void(title):
    """VOID - cosmic horror theme"""
    return """👁️ ════════════════════════ [ THE BEYOND: {title} ] ════════════════════════ 👁️
  
     ~ ~ ~ The geometry of this network defies mortal architecture ~ ~ ~"""


def _art_glitch(title):
    """MATRIX GLITCH - corrupted code theme"""
    return """___  _  _  ___  _  _      _  _  _  _  ___  _  _  ___  _  _  ___  _  _  ___
 / __)( °)(__ \\(_)(_ )    (_)(_)(_)(_)(__ )(_)(_)((_  )(_)(_)(__ )(_)(_)(_  )
( (__  )(  / /  _  _        _  _  _  _    / /  _  _    )(  _  _    / /  _  _    )(
 \\___)(__)(___)(_)(_)     (_)(_)(_)(_) (__)(_)(_)  (__)(_)(_) (__)(_)(_)  (__)

 [x] TARGET: {title}
 [x] HASH: 0x9F4C2A1E // STATUS: COMPROMISED

 root@underground:~# select_exploit
 ---------------------------------------------------------------------------"""


def _art_cmd_recon(title):
    """CMD RECON - terminal/command prompt theme"""
    return """C:\\NET_TOOLS\\SUB_01> load_recon_modules --active"""


def _art_morty(title):
    """MORTY - Rick & Morty ASCII art theme"""
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


# ---------------------------------------------------------------------------
# BANNER RENDERERS - Each function produces the full banner for a theme
# Consists of: decorative art + command list below
# ---------------------------------------------------------------------------

def render_banners(theme_key, dir_id):
    """Render the themed banner for a given directory and theme.

    Args:
        theme_key: The active theme key string (e.g. "1", "13").
        dir_id: Directory ID string ("01"-"05").

    Returns the banner string with all commands embedded, or None if theme
    is "1" (use plain rendering instead).
    """
    if theme_key == "1":
        return None  # Theme 1 uses plain rendering

    # Theme-specific styles
    theme_info = THEME_INFO.get(theme_key)
    if not theme_info:
        return None

    art_func = theme_info["art"]
    color = theme_info["color"]
    marker, mcolor = MARKERS.get(theme_key, MARKERS["1"])
    title = f"SUB-DIRECTORY {dir_id} // {DIR_TITLES.get(dir_id, '')}"

    # Render the banner art
    art = art_func(title).format(title=title)
    banner = color + art + COLOR_RESET
    items = DIR_ITEMS.get(dir_id, [])
    if theme_info.get("is_table"):
        commands = _fmt_items_table(items, marker, color)
    else:
        commands = _fmt_items(items, marker, color)

    banner += "\n" + commands
    return banner


# Theme -> rendering info
# Maps each theme to its banner art function, color, and rendering style.
# Edit the art functions above to change how banners look.
# Edit DIR_ITEMS above to change the commands shown.
THEME_INFO = {
    "1":  {"art": None,               "color": COLOR_CYAN, "is_table": False},  # Terminal (default) - no banner
    "2":  {"art": _art_planet,          "color": COLOR_CYAN, "is_table": False},  # Planet UI
    "3":  {"art": _art_planet,          "color": COLOR_GREEN, "is_table": False},  # Mainframe UI (use planet art but green)
    "4":  {"art": _art_reaper,          "color": COLOR_RED,     "is_table": False},  # Reaper UI
    "5":  {"art": _art_hitla,           "color": COLOR_MAGENTA, "is_table": False},  # Hitla UI
    "6":  {"art": _art_matrix,          "color": COLOR_GREEN,   "is_table": False},  # Matrix UI
    "7":  {"art": _art_cyberpunk,       "color": COLOR_NEON_PINK, "is_table": False},  # Cyberpunk 2077 UI
    "8":  {"art": _art_ghost_shell,     "color": COLOR_WHITE,   "is_table": False},  # Ghost Shell UI
    "9":  {"art": _art_devil,           "color": COLOR_RED,     "is_table": False},  # Devil Core UI
    "10": {"art": _art_retro,           "color": COLOR_ORANGE,  "is_table": False},  # Retro 80s Synth UI
    "11": {"art": _art_neon,            "color": COLOR_LIME,    "is_table": False},  # Neon Hack UI
    "12": {"art": _art_space,           "color": COLOR_PURPLE,  "is_table": False},  # Deep Space Node UI
    "13": {"art": _art_c137,            "color": COLOR_GREEN,   "is_table": False},  # Morty Exact ASCII Art UI
    "14": {"art": _art_medieval,        "color": COLOR_YELLOW,  "is_table": False},  # Medieval UI
    "15": {"art": _art_steampunk,       "color": COLOR_ORANGE,  "is_table": False},  # Steampunk UI
    "16": {"art": _art_synthwave,       "color": COLOR_NEON_PINK, "is_table": False},  # Synthwave UI
    "17": {"art": _art_wasteland,       "color": COLOR_RED,     "is_table": False},  # Wasteland UI
    "18": {"art": _art_corporate,       "color": COLOR_WHITE,   "is_table": True},  # Corporate UI (table style)
    "19": {"art": _art_abyssal,         "color": COLOR_CYAN,    "is_table": False},  # Abyssal UI
    "20": {"art": _art_void,            "color": COLOR_PURPLE,  "is_table": False},  # Void UI
}


# Backwards-compatible wrappers
def get_dir_banner(dir_id, theme_key):
    """Return the themed banner string for a given directory and theme."""
    return render_banners(theme_key, dir_id)
