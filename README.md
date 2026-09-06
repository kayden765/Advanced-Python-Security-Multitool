Documents
1
README.md
MAINFRAME // COMPREHENSIVE SECURITY RECONNAISSANCE ENGINE
This is a powerful open-source Python multitool designed for system telemetry, hardware ID tracking, security auditing, network reconnaissance, and automated penetration testing. A 45-in-1 advanced security platform featuring Cloudflare integration, OSINT gathering, system information profiling, and defensive auditing tools.

Version: v2.0.0
Architecture: Multi-Tier Nested Subsystem Shell (Directory-Driven Layout)
Platform: Cross-Platform Windows/Linux/macOS
Python: 3.8+
Tools: 40-IN-1 Security Platform

Quick Setup Tutorial
Basic Setup (All Platforms)
Get MAINFRAME running in under 2 minutes with Python 3.8+:

# 1. Clone the repository
git clone https://github.com/kayden765/python-ddos-multitool-script.git
cd python-ddos-multitool-script

# 2. Install Python dependencies
pip install -r setup/requirements.txt

# 3. Run the tool
python mainframe.py
Windows Setup (Recommended)
Run setup\setup.bat as Administrator to auto-install all Python dependencies and external tools in one go:

setup\setup.bat
This will:

Install all Python dependencies from setup/requirements.txt
Install Impacket and download psexec.py / wmiexec.py to core/impacket_scripts/
Install Chocolatey if not present
Install Hashcat, Metasploit, Nmap via Chocolatey
Download PhoneInfoga binary
Check for Node.js and Vercel CLI (for image logger)
Verify all installations and report status
After setup completes, restart your terminal and run python mainframe.py.

Image Logger — Vercel Deployment Setup
The Image Logger can be deployed to Vercel for a public tracking URL that works everywhere, including Discord.

Prerequisites
Node.js installed (https://nodejs.org/)
Vercel CLI installed: npm install -g vercel
A Vercel account (free tier works)
Deployment Steps
Navigate to the Vercel project folder:
cd core/vercel-image-logger
Deploy to Vercel:
vercel --prod
Follow the prompts to link your project. Vercel will output a public URL like:

https://vercel-image-logger.vercel.app
Set Cloudflare Worker URL in mainframe: After deployment, update the Worker URL in mainframe.py if needed. The default Worker endpoint is:
https://broken-boat-ed6e.multitool-43.workers.dev
Configure Discord Webhooks (optional): The Vercel serverless function reads webhook URLs from Cloudflare Worker environment variables (DISCORD_WEBHOOK_URL, DISCORD_BAN_WEBHOOK_URL, DISCORD_WHITELIST_WEBHOOK_URL). These are configured in your Cloudflare Worker dashboard — not in the Vercel project.
Verify deployment: Open the deployed URL in a browser. You should see the tracking GIF. Any visit will be logged and posted to your Discord webhook.
Local vs Vercel
Feature	Local Server	Vercel Deployment
URL	localhost:8080	*.vercel.app
Discord Preview	Limited	Full image preview
Accessibility	Local only	Public internet
Logs	In-memory	Vercel /tmp (ephemeral)
Monitoring	Live terminal	Live terminal via API
Repository Topics (Tags)
Add these topics to your GitHub repository (via the "About" gear icon in the right sidebar) so users discover the project through GitHub's filtered category loops:

python · python-multitool · security-tool · penetration-testing · osint · network-security · system-info · telemetry · hardware-id · cloudflare · ddos · brute-force · hashcat · metasploit · automation
About Section (Short Description)
Set your repository's short description to under 15 words, front-loading exact keywords:

An advanced Python multitool featuring system telemetry, hardware ID tracking, and Cloudflare integration.

this application may be detected by antivirus due to the msfvenom module and the ncat module.
TABLE OF CONTENTS
Quick Setup Tutorial
Repository Topics (Tags)
Overview
How to Support / Boost Social Signals
Architecture
Installation
Main System Directory Core
Sub-Directory 01 — Network Infrastructure & Endpoint Recon
Sub-Directory 02 — External OSINT & Target Record Profilers
Sub-Directory 03 — Local Data Traffic, Security Audits & Utilities
Sub-Directory 04 — Advanced Infrastructure Audits & Integrity
Sub-Directory 05 — Attack Vectors, Exploit Frameworks & Defensive Auditing
Image Logger — Vercel Deployment
Logging & Privacy
Configuration & Customization
UI Themes & Directory Banners
Dependencies
Disclaimer
OVERVIEW
MAINFRAME is a comprehensive Python multitool and security reconnaissance and testing platform designed for authorized security assessments, penetration testing, and educational purposes. It provides a unified terminal interface for network analysis, OSINT gathering, local system auditing, and controlled attack vector testing with system telemetry and hardware ID tracking.

The tool is organized into five primary operational directories, each containing specialized modules for different aspects of security testing.

How to Support / Boost Social Signals
GitHub's search algorithm pushes repositories with higher engagement (stars, watchers, forks) to the top of search results. You can help this project gain visibility:

Star this repository — stars are the single biggest ranking signal
Watch the repository to get notified of new releases
Fork the repository and contribute fixes or new modules
Share this tool in relevant developer communities, subreddits (r/netsec, r/Python, r/hacking), and Discord channels to get initial traction
Post about it on Twitter/X, LinkedIn, or Hacker News with the GitHub link
Once real users star and clone the project, GitHub's algorithm recognizes it as an authority result and moves it up in search rankings.

ARCHITECTURE
cybertool/
├── mainframe.py                 # Core orchestration engine ^amp; UI
├── setup.bat                    # Complete Windows installer
├── requirements.txt             # Python dependencies
├── core/
│   ├── etc/
│   │   ├── settings.py          # Configuration management
│   │   └── functions.py         # UI helpers, banners, menus
│   ├── ddos_attack/
│   │   └── ddos.py              # Beast Mode DDoS engine
│   ├── brute_force/
│   │   └── bruteforce.py        # Brute force attack module
│   ├── image_logger/
│   │   └── imagelogger.py       # Local image logger server
│   ├── impacket_scripts/        # Impacket remoting scripts
│   │   ├── psexec.py
│   │   └── wmiexec.py
│   ├── vercel-image-logger/     # Vercel deployment assets
│   │   ├── api/
│   │   │   └── track.js
│   │   ├── vercel.json
│   │   └── package.json
│   └── input/                   # User data (gitignored)
└── README.md
Key Design Principles
Modular Architecture: Each attack/recon module is isolated in its own directory under core/
Lazy Imports: Optional modules are imported independently so missing dependencies don't break the entire tool
Dual-Stream Logging: All terminal output is simultaneously logged to disk
Cross-Platform: Supports Windows, Linux, and macOS with platform-specific optimizations
Auto-Elevation: Automatically requests Administrator/Root privileges on Windows when needed
INSTALLATION
Prerequisites
Python 3.8 or higher
pip package manager
Git (for cloning)
Setup
# Clone the repository
git clone https://github.com/kayden765/python-ddos-multitool-script.git
cd cybertool

# Install Python dependencies
pip install -r requirements.txt
Complete Setup (Recommended)
Run setup.bat as Administrator to automatically install all Python dependencies and external tools:

setup.bat
This will:

Install all Python dependencies from requirements.txt
Install Impacket (psexec.py / wmiexec.py) via pip
Download psexec.py and wmiexec.py to core/impacket_scripts/
Install Chocolatey if not present
Install Hashcat via Chocolatey
Install Metasploit Framework (msfconsole / msfvenom) via Chocolatey
Verify all installations and report status
Manual External Tool Installation
If setup.bat does not cover your platform, install these tools manually:

Tool	Purpose	Install Method
Impacket	Administrative remoting (psexec.py, wmiexec.py)	pip install impacket
Hashcat	Password compliance auditing	Download from https://hashcat.net/hashcat/
Metasploit Framework	msfconsole / msfvenom	Download from https://www.metasploit.com/download
Nmap	Advanced port scanning and service profiling	choco install nmap or download from https://nmap.org/
Sherlock	Username tracing	pip install sherlock-project
PhoneInfoga	Telecom scanning	Requires Go: go install github.com/sundowndev/phoneinfoga@latest
Holehe	Email platform auditor	pip install holehe
Socialscan	Identity profiler	pip install socialscan
Ensure all installed tools are in your system PATH so mainframe.py can locate them.

Sub-Directory 05 — Defensive Auditing Tools Installation
The following 5 tools were added to Sub-Directory 05 for defensive auditing and baseline validation:

1. Metasploit Framework Console (msfconsole)
Purpose: Systems administrators use msfconsole to validate known infrastructure configurations, test network boundaries against documented service behaviors, and confirm patch integrity through controlled exploitation modules in isolated lab environments.
Installation:
Windows: Download the official installer from https://www.metasploit.com/download
Or use Chocolatey: choco install metasploit
After installation, ensure msfconsole and msfvenom are in your system PATH
Verification: Run msfconsole --version to confirm installation
2. Msfvenom Network Egress Verification Tool (msfvenom)
Purpose: Generates synthetic network communication payloads to test whether internal IDS and corporate firewalls successfully alert on or block abnormal outbound connections.
Installation: Bundled with Metasploit Framework. Install Metasploit as described above.
Verification: Run msfvenom --help to confirm installation
3. Hashcat Password-Strength Compliance Auditor (hashcat)
Purpose: Offline cryptographic verification core used to cross-reference enterprise database hashes against common dictionary lists, ensuring internal passwords adhere to corporate complexity standards.
Installation:
Windows: Download from https://hashcat.net/hashcat/
Or use Chocolatey: choco install hashcat
Extract the archive and add the directory to your system PATH
Verification: Run hashcat --version to confirm installation
4. Impacket Administrative Remoting Suite (psexec.py / wmiexec.py)
Purpose: Evaluates local credential hygiene, auditing whether standard enterprise service accounts have excessive implicit cross-network permissions or misconfigured access tokens.
Installation:
Install via pip: pip install impacket
The mainframe automatically downloads psexec.py and wmiexec.py from the official Impacket repository to core/impacket_scripts/
No additional PATH configuration needed; the mainframe resolves these scripts automatically
Verification: Run python -c "from impacket import version; print(version.__version__)" to confirm the library is installed
5. Real-Time Security Log Diagnostic Module
Purpose: Defensive telemetry module used to tail, read, and stream local audit text logs and session history outputs to the operator in real time.
Installation: No external dependencies required. This is a pure-Python module built into mainframe.py.
Verification: Select option [8] from Sub-Directory 05 and provide a valid log file path to test streaming.
MAIN SYSTEM DIRECTORY CORE
The main menu serves as the primary navigation hub, organized into 5 operational subdirectories plus a shutdown control.

[MAIN SYSTEM DIRECTORY CORE]

[1] Sub-Directory 01 // Network Infrastructure & Endpoint Recon Cores
[2] Sub-Directory 02 // External OSINT & Target Record Profilers
[3] Sub-Directory 03 // Local Data Traffic, Security Audits & Utilities
[4] Sub-Directory 04 // Advanced Infrastructure Audits & Integrity Cores
[5] Sub-Directory 05 // Attack Vectors, Exploit Frameworks & Defensive Auditing

[SYSTEM SHUTDOWN CONTROL]
[6] Terminate Active Mainframe Operator Control Session
SUB-DIRECTORY 01 — NETWORK INFRASTRUCTURE & ENDPOINT RECON
Purpose: Active network reconnaissance, host discovery, and service enumeration.

Modules
[1] High-Speed Rainbow Echo Pinger Latency Monitor
Measures ICMP echo latency to target hosts
Supports continuous ping monitoring with color-coded status
Configurable target IP with default fallback
Real-time latency display with responsive/non-responsive indicators
[2] Reverse DNS Infrastructure Resolver (IP-to-Host PTR Check)
Resolves IP addresses to hostnames using reverse DNS
Displays PTR record results or indicates missing reverse name pointers
Useful for identifying infrastructure ownership
[3] Multi-Threaded Target Service Port Scanner & Vulnerability Profiler
Scans target hosts for open TCP ports
Multi-threaded for high-speed scanning
Service version detection and vulnerability profiling
Common port-to-service mapping with defensive mitigation hints
Adjustable thread count
[4] Local Subnet Parallel Ping Sweeper Matrix
Discovers active devices on local network segments
Parallel ping sweeps across IP ranges
Color-coded responsive device detection
Subnet calculator for target range generation
[5] Network Application Service Banner Grabber Auditor
Connects to open ports and retrieves service banners
Identifies software versions and potential vulnerabilities
TCP connection-based banner extraction
[6] Passive Domain Subdomain Discovery Engine (via crt.sh Logs)
Discovers subdomains through Certificate Transparency logs
Queries crt.sh API for historical certificate data
Passive reconnaissance without direct target contact
[7] Advanced RDAP Registration Infrastructure Allocation Mapper
Queries RDAP (Registration Data Access Protocol) for domain registration info
Extracts registrar, organization, country, and network allocation data
Provides production infrastructure metric data blocks
[8] HTTP Header Security Compliance & Hardening Auditor
Analyzes HTTP security headers
Checks for HSTS, CSP, X-Frame-Options, X-XSS-Protection, etc.
Provides mitigation purpose descriptions for each header
[9] DNS-over-HTTPS (DoH) Client Resolver Subsystem
Performs DNS queries over HTTPS using Cloudflare DoH
Encrypted DNS resolution for privacy
Returns structured DNS records with TTL data
[10] IP Address Geolocation & Metadata Lookup
Geolocates IP addresses using ip-api.com
Returns city, region, country, ISP, ASN, and timezone data
JSON-based structured geolocation results
SUB-DIRECTORY 02 — EXTERNAL OSINT & TARGET RECORD PROFILERS
Purpose: Open-source intelligence gathering and target profiling using external tools.

Modules
[1] Sherlock Username Account Tracer (Live Shell Subprocess Launch)
Hunts for usernames across 300+ social media platforms
Launches Sherlock in a subprocess with colored output
Real-time account discovery with site-by-site results
[2] PhoneInfoga Telecom Target Scanner (Live Shell Subprocess Launch)
Telecom reconnaissance using PhoneInfoga
Phone number validation and carrier lookup
Number formatting and regional analysis
[3] Holehe Email Platform Account Auditor (Live Shell Subprocess Launch)
Checks if email addresses are registered on 100+ platforms
Uses Holehe to audit email presence across sites
Color-coded results for quick analysis
[4] Socialscan Concurrent Identity Profiler (Live Shell Subprocess Launch)
Concurrent username/email scanning across platforms
Multi-threaded profile enumeration
Live shell output with progress indicators
[5] Live Online Data Breach Explorer & Password Leak Checker
Checks email/username against known data breaches
Queries breach databases for compromised credentials
Provides breach count and exposure details
[6] Tor Exit Node Network Threat Intelligence Node Validator
Fetches current Tor exit node IPs from dan.me.uk
Validates if an IP is a known Tor exit node
Threat intelligence for network access control
[7] Online IP Geolocation & Autonomous System (ASN) Metadata Explorer
Geolocates IP addresses using ip-api.com
Returns city, region, country, ISP, ASN, and timezone data
JSON-based structured geolocation results
[8] IDN Homograph Phishing Domain & Punycode Analyzer
Detects internationalized domain name (IDN) homograph attacks
Analyzes domains for deceptive Unicode characters
Punycode conversion and visual similarity detection
SUB-DIRECTORY 03 — LOCAL DATA TRAFFIC, SECURITY AUDITS & UTILITIES
Purpose: Local system analysis, encryption utilities, and traffic monitoring.

Modules
[1] Inbound Network Packet Monitor Engine (Requires Admin Context)
Live packet capture and analysis
Requires Administrator privileges on Windows
Displays source/destination IPs and protocols
Real-time traffic monitoring with color-coded output
[2] Local Directory Source Code 'Secret & Private Key' Leak Scanner
Recursively scans directories for exposed secrets
Pattern matching for API keys, tokens, passwords, private keys
Supports multiple file extensions: .env, .pem, .key, .p12, etc.
Base64 pattern detection for encoded secrets
[3] Cryptographic Hash Signatures Matrix Generation & Token Analyzer
Generates MD5, SHA-1, SHA-256 hashes for files/text
Batch hash processing with progress indicators
Hash format validation and display
[4] Advanced Local Host Operating System Telemetry Profiler
Comprehensive system information gathering
OS, hostname, architecture, processor, RAM, GPU, network interfaces
Formatted table output with all system metrics
[5] Base64 Cryptographic Processing Matrix (Data Transformation)
Encode/decode text to/from Base64
Encrypt/decrypt text with custom password key
File encoding/decoding support
Stream cipher implementation for text encryption
SUB-DIRECTORY 04 — ADVANCED INFRASTRUCTURE AUDITS & INTEGRITY
Purpose: Deep system audits, integrity checking, and network analysis.

Modules
[1] Local File Integrity Monitor (FIMS Directory Snapshot Tracker)
Creates baseline snapshots of file integrity
SHA-256 hash tracking for files in specified directories
Compares current state against baseline
Detects unauthorized file modifications
[2] SSL/TLS Certificate Expiration & Cipher Suite Auditor
Connects to remote servers and retrieves SSL/TLS certificates
Extracts expiration dates, issuers, and subjects
Color-coded warnings for expiring certificates
Cipher suite enumeration
[3] Host Active Network Connection & Listening Port Profiler
Displays active network connections using netstat
Shows local/foreign addresses and connection states
Lists listening ports and associated processes
Windows-specific process resolution
[4] Password Complexity & Offline Information Entropy Matrix
Analyzes password strength using Shannon entropy calculations
Calculates entropy bits and character pool complexity
Checks against common patterns and dictionary words
Provides strength score and suggestions
[5] Local Network ARP Table Cache Profiler & Duplicate MAC Auditor
Displays ARP table entries using arp -a
Shows IP-to-MAC mappings for local network
Identifies potential duplicate MAC address conflicts
[6] CIDR Subnet IPv4 Network Range & Mask Calculator
Calculates network ranges from CIDR notation
Converts subnet masks to wildcard masks
Determines network class, host capacity, and broadcast address
Supports all valid CIDR prefixes (1-32)
[7] UPnP SSDP Local LAN Smart Device Discovery Explorer
Discovers UPnP devices on local network
SSDP multicast discovery protocol
Identifies smart devices, routers, and media servers
[8] Local Hosts File DNS Spoofing & Cache Poisoning Auditor
Scans local hosts file for suspicious entries
Detects potential DNS hijacking or cache poisoning
Checks for common phishing/malware domains
File hash verification for hosts file integrity
[9] MAC Address OUI Vendor Directory Lookup Engine
Identifies device manufacturers from MAC addresses
OUI (Organizationally Unique Identifier) lookup
Supports local ARP table scanning or manual input
Vendor name resolution from MAC prefix
SUB-DIRECTORY 05 — ATTACK VECTORS, EXPLOIT FRAMEWORKS & DEFENSIVE AUDITING
Purpose: Controlled attack vectors for authorized security testing, plus defensive auditing and baseline validation tools.

Modules
[1] Beast Mode (DDoS)
Multi-threaded DDoS testing engine
Beast Mode feature: Hold 1 key to continuously launch attack bursts
Press 0 to stop beast mode
Configurable thread count and target URL
Real-time success/failure counters
[2] Image Logger
Generates image tracking links that log visitor IP addresses
Two deployment options:
Local Server: Runs on http://localhost:8080
Vercel Deployment: Auto-deploys to public Vercel URL
Displays target GIF with Open Graph tags for Discord/social preview
Real-time IP monitoring in mainframe terminal
Captures User-Agent, timestamp, and IP on page visit
/api/logs endpoint for programmatic log access
[3] Brute Force
Automated password brute forcing with configurable wordlists
Auto wordlist: Uses core/input/brutef.txt by default
Two attack modes:
Login Form: POST request brute forcing with custom field names
Basic Auth: HTTP Basic Authentication header brute forcing
Success indicator matching (page text or HTTP status)
Real-time cracked/failed counters
[4] Metasploit Framework Console Interface (msfconsole)
Legitimate Purpose: Systems administrators use msfconsole to validate known infrastructure configurations, test network boundaries against documented service behaviors, and confirm patch integrity through controlled exploitation modules in isolated lab environments.
Script Role: An interactive choice that maps inputs directly to call msfconsole inline within the current terminal loop.
Dynamically resolves msfconsole from system PATH via shutil.which
Launches the full Metasploit console inline (no detached windows)
Type exit or Ctrl+C to return to menu
[5] Msfvenom Network Egress Verification Tool (msfvenom)
Legitimate Purpose: A baseline boundary-testing companion utility used to generate synthetic network communication payloads. It tests if internal intrusion detection systems (IDS) and corporate firewalls successfully alert on or block abnormal outbound connections.
Script Role: A prompt wizard gathering local loopback parameters (like LHOST, LPORT, format) to execute an msfvenom syntax call directly to an output file.
Interactive wizard for payload generation
Prompts for LHOST, LPORT, payload format (py/php/exe/elf/asp/war), and output file path
Writes payload directly to disk for controlled egress testing
Validates binary existence before execution
[6] Hashcat Password-Strength Compliance Auditor (hashcat)
Legitimate Purpose: An administrative offline cryptographic verification core used to cross-reference enterprise database hashes against common dictionary lists, ensuring internal passwords adhere to corporate complexity standards.
Script Role: An inline interface prompting for target database file paths and wordlists to call the local hashcat command.
Prompts for hash file path and wordlist path
Validates both files exist before execution
Supports configurable hash mode (MD5, SHA1, NTLM, etc.)
Runs hashcat inline in the current terminal session
[7] Impacket Administrative Remoting Suite (psexec.py / wmiexec.py)
Legitimate Purpose: Used to evaluate local credential hygiene, auditing whether standard enterprise service accounts have excessive implicit cross-network permissions or misconfigured access tokens.
Script Role: A clean parameter wrapper that structures a unified terminal command line call to standard Impacket Python scripts using the user's input.
Supports both psexec.py and wmiexec.py
Prompts for target host, username, password/hash, and optional domain
Resolves script paths from PATH, pipx, or common Impacket install locations
Executes inline via subprocess.run with live output
[8] Real-Time Security Log Diagnostic Module
Legitimate Purpose: A defensive telemetry module used to tail, read, and stream local audit text logs and session history outputs to the operator in real time.
Script Role: A loop that prints incoming log updates directly to the console display.
Prompts for a local log file path
Streams new log lines to the console in real-time
Pure Python implementation (no external dependencies)
Press Ctrl+C to stop streaming
[9] Nmap Advanced Port Scanner & Service Profiler
Legitimate Purpose: Industry-standard port scanning and network discovery for authorized infrastructure assessment and firewall rule validation.
Script Role: A wrapper that invokes nmap inline with scan profiles for quick, full, service-detection, OS fingerprinting, and aggressive scans.
Prompts for target IP/hostname/CIDR
Scan presets: Quick TCP, Full TCP, Service/version detection, OS fingerprinting, Aggressive, Custom args
Output streams directly to the mainframe terminal
Requires nmap binary in system PATH
IMAGE LOGGER — VERCEl DEPLOYMENT
The Image Logger can be deployed to Vercel for a public URL that works everywhere, including Discord.

How It Works
Deployment: Mainframe auto-deploys core/vercel-image-logger/ to Vercel
Public URL: Generates a shareable https://*.vercel.app link
Tracking: When someone opens the link:
Their IP address is logged
User-Agent and timestamp are captured
Data is stored in Vercel's ephemeral /tmp storage
Monitoring: Mainframe terminal polls /api/logs and displays captures in real-time
Image Preview: The page serves a GIF directly as image/gif for proper Discord preview
Technical Details
Framework: Vercel Node.js Serverless Function
Image: https://c.tenor.com/HtRab3iYiisAAAAC/tenor.gif
Logs Endpoint: https://vercel-image-logger.vercel.app/api/logs
Response Format: Direct binary GIF with caching disabled
OG Tags: Open Graph and Twitter Card meta tags for social previews
Local vs Vercel
Feature	Local Server	Vercel Deployment
URL	localhost:8080	*.vercel.app
Discord Preview	Limited	Full image preview
Accessibility	Local only	Public internet
Logs	In-memory	Vercel /tmp (ephemeral)
Monitoring	Live terminal	Live terminal via API
LOGGING & PRIVACY
Session Logging
MAINFRAME implements dual-stream logging:

All terminal output is captured to logs/session_YYYYMMDD_HHMMSS.txt
Logs are written in real-time as the tool runs
ANSI color codes are stripped from log files for readability
Privacy Protection
To protect your privacy when sharing this tool:

Logs Directory: The logs/ folder is gitignored
No IP Storage: The Vercel image logger does not store logs locally
Ephemeral Storage: Vercel serverless functions use temporary storage
Session Isolation: Each run creates a new timestamped log file
Input Directory: The core/input/ folder is gitignored to prevent accidental commit of wordlists, tokens, or IP lists
What Gets Logged
Terminal output from all modules
Image logger captures (Vercel only, not local)
Session start/stop timestamps
Error messages and stack traces
What Does NOT Get Logged
Your personal IP address (unless you test with yourself)
Credentials or passwords entered during brute force
Target information from recon modules
Any data from the core/input/ directory
CONFIGURATION & CUSTOMIZATION
Wordlist Configuration
The Brute Force module automatically uses:

core/input/brutef.txt
Place your custom wordlist at this path. One password per line.

Language Settings
Access settings via the main menu or directly in core/etc/settings.py:

Language preferences (EN/RU)
Color schemes
Module Paths
All modules are loaded from core/ with independent imports. To disable a module:

Delete or rename its folder under core/
The mainframe will skip it gracefully with a "not loaded" message
UI THEMES & DIRECTORY BANNERS
MAINFRAME supports 20 visual UI themes, each with its own themed directory banner that displays the full command list for each subdirectory.

Available Themes
Theme	UI Name	Style
1	Terminal UI (Default)	Plain [NN] format, no decorative banner
2	Planet UI	🪐 Orbital sector with space/art deco styling
3	Mainframe UI	Green terminal style with box borders
4	Reaper UI	☠ Skull & crossbones with Soul Reaper ASCII art
5	Hitla UI	Classified archive with security badge framing
6	Matrix UI	Green code rain aesthetic
7	Cyberpunk 2077 UI	Netrunner deck / ICE breaker theme
8	Ghost Shell UI	Phantom protocol with GHOST SHELL ASCII art
9	Devil Core UI	🔥 Infernal devil with hellfire styling
10	Retro 80s Synth UI	Retro cassette/terminal aesthetic
11	Neon Hack UI	Glowing neon cyber aesthetic
12	Deep Space Node UI	Cosmic space exploration theme
13	Morty Exact ASCII Art UI	🟢 Dimension C-137 portal with Rick & Morty art
14	Medieval UI	⚔️ Guild archives with scroll/medieval styling
15	Steampunk UI	⚙️ Industrial steam-powered aesthetic
16	Synthwave UI	◢◤ 1984 vaporwave digital theme
17	Wasteland UI	☣️ Post-apocalyptic hazard zone
18	Corporate UI	Strategic compliance directory (table format)
19	Abyssal UI	🌊 Deep ocean trench sonar theme
20	Void UI	👁️ Cosmic horror / void dimension
Directory Banner Structure
Each directory (DIR 01-DIR 05) has its own themed banner showing all available commands:

SUB-DIRECTORY 01: Network Infrastructure & Endpoint Recon (11 commands)
SUB-DIRECTORY 02: External OSINT & Target Profile Management (8 commands)
SUB-DIRECTORY 03: Local Data Traffic, Security Audits & Utilities (6 commands)
SUB-DIRECTORY 04: Advanced Infrastructure Audits & Integrity (10 commands)
SUB-DIRECTORY 05: Attack Vectors, Exploit Frameworks & Defensive Auditing (10 commands)
Customizing UI Themes
Theme files are located in core/dir_banners.py:

Edit DIR_ITEMS to modify command names and descriptions per directory
Edit _art_* functions to change the decorative ASCII art per theme
Edit THEME_INFO to remap themes to art/color combinations
The MARKERS dict controls the command line markers (◯, ☠, 🔥, etc.) per theme
DEPENDENCIES
Python Packages
colorama==0.4.6       # Terminal colors
requests==2.31.0      # HTTP requests
fade==0.0.9           # ASCII art fading
beautifulsoup4==4.12.3 # HTML parsing
fake-useragent==1.5.1 # Random user agents
aiohttp==3.9.5        # Async HTTP
urllib3==2.2.3        # HTTP client
pythonping==1.0.0     # ICMP ping wrapper
impacket==0.12.0      # Impacket remoting scripts
External Tools (Optional / Auto-Installed)
msfconsole            # Metasploit Framework console
msfvenom              # Metasploit payload generator
hashcat               # Password compliance auditor
psexec.py             # Impacket SMB exec
wmiexec.py            # Impacket WMI exec
sherlock              # Username tracer
phoneinfoga           # Telecom scanner
holehe                # Email auditor
socialscan            # Identity profiler
nmap                  # Port scanning
tshark                # Packet capture
go                    # Sherlock, PhoneInfoga runtime
node.js               # Vercel image logger
vercel CLI            # Image logger deployment
Platform-Specific
Windows: ctypes for UAC elevation, GetAsyncKeyState for beast mode
Linux/macOS: subprocess for system commands, termios for key detection
DISCLAIMER
This tool is for authorized security testing and educational purposes only.

Only use on systems you own or have explicit written permission to test
Unauthorized access to computer systems is illegal
The authors are not responsible for misuse or damage caused by this tool
Users assume all liability for their actions
Respect all applicable laws and regulations in your jurisdiction
LICENSE
Copyright (C) 2024 un1ucm
All rights reserved.

When posting this code on other resources, please indicate the author.

MAINFRAME v5.90 — Comprehensive Security Reconnaissance Engine
