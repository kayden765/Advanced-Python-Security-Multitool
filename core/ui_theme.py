import json
import os
import time

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

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


TERMINAL_BANNER = f"""{COLOR_GRAY}========================================================================================================================
{COLOR_GREEN}PuTTY Terminal Engine (v0.78-SSH)
Login successful. Server: debian-mainframe-prod
Last login: {time.strftime('%a %b %d %H:%M:%S %Y')} from 192.168.1.104
{COLOR_GRAY}========================================================================================================================{COLOR_RESET}"""

PLANET_BANNER = f"""{COLOR_CYAN}                                .                                             .
     *   .                    .              .        .   *          .
  .         .                      .        .            .      .        .
        o                               .                    .
         .               .                  .            .
          0     .
                 .          .                   ,                ,    ,
 .         \\          .                           .
      .     \\   ,
   .         o     .                  .                    .            .
     .         \\                ,             .                .
               #\\##\\#      .                               .        .
             #  #O##\\###                .                        .
   .        #*#  #\\##\\###                       .                            ,
        .   ##*#  #\\##\\##                .                      .
      .      ##*#  #o##\\#         .                              ,        .
          .     *#  #\\#     .                    .              .          ,
                      \\          .                         .
____^/\\___^--____/\\____O____________/\\/\\---/\\___________---______________
   /\\^   ^  ^    ^                 ^^ ^  '\\ ^         ^        ---
         --           -            --  -      -         ---  __       ^
   --  __                   ___--  ^  ^                         --  __{COLOR_RESET}"""

MAINFRAME_BANNER = f"""{COLOR_GREEN}========================================================================================================================
┌─ [MAINFRAME ENGINE] ─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                                                      │
│   ███▄ ▄███▒    ▄▄▄         ██▓    ███▄    █                                                                         │
│  ▓██▒▀█▀ ██▒   ▒████▄      ▓██▒    ██ ▀█   █                                                                         │
│  ▓██    ▓██░   ▒██  ▀█▄    ▒██▒   ▓██  ▀█ ██▒                                                                        │
│  ▒██    ▒██    ░██▄▄▄▄██   ░██░   ▓██▒  ▐▌██▒                                                                        │
│  ▒██▒   ░██▒    ▓█    ▓██▒ ░██░   ▒██░   ▓██░                                                                        │
│  ░ ▒░   ░  ░    ▒▒    ▓▒█░ ░▓     ░ ▒░   ▒ ▒                                                                         │
│                                                                                                                      │
│   [+] SYSTEM ARCHITECTURE: 45-IN-1 MULTI-TOOL ENGINE | SECURITY OPERATOR ACCESS LEVEL 0                             │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘{COLOR_RESET}"""

REAPER_BANNER = rf"""{COLOR_RED}
              ...                            
             ;::::;                           
           ;::::; :;                          
         ;:::::'   :;                         
        ;:::::;     ;.                        
       ,:::::'       ;           OOO\         
       ::::::;       ;          OOOOO\        
       ;:::::;       ;         OOOOOOOO       
      ,;::::::;     ;'         / OOOOOOO      
    ;:::::::::`. ,,,;.        /  / DOOOOOO    
  .';:::::::::::::::::;,     /  /     DOOOO   
 ,::::::;::::::;;;;::::;,   /  /        DOOO  
;`::::::`'::::::;;;::::: ,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;' /  / `:#                  
   ::::::`:::::;'  /  /   `#    
{COLOR_RESET}"""

HITLA_BANNER = rf"""{COLOR_MAGENTA}
⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⢶⣟⣚⣢⣦⠀⠀⠀⠀⠀⣀⣀⡀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣄⣀⣀⣀⣀⣀⣀⣀⣀
⠀⢿⣿⣿⣿⣿⣿⣿⣿⣏⠻⣿⣿⣿⣿⣯⡻⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⣿⣿⣿⡏⠉⠀⠀⠀⠀⢠⣿⣿⣿⣿⡿⢋⣽⣿⣿⣿⡿⢟⣽⣿⣿⣿⣿⣿⣿⣿⠿⠃
⠀⠰⢶⣶⣶⣶⣶⣶⣶⣶⣶⣦⠰⣶⡶⠶⣀⢶⣶⣯⣝⢿⣅⠀⠀⠀⠀⣸⣿⣿⣿⣿⣄⠀⠀⠀⠀⣸⡿⣫⣷⣶⡖⣀⠶⢶⣶⠆⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠂⠀
⠀⠀⠐⠳⠾⠶⠷⠾⠶⠷⠾⠾⠧⠒⣛⣻⡵⢂⠹⣿⣿⣷⣝⢷⣦⣴⣿⣿⣿⣿⣿⣿⣿⣷⣤⣴⠟⣫⣾⣿⣿⢋⡐⢮⣟⣓⠒⠾⠶⠷⠾⠶⠷⠾⠶⠷⠞⠃⠀⠀
⠀⠀⠀⠈⠙⢛⣛⣛⣛⣛⣛⣛⣛⣊⠩⡵⢞⣫⠖⣨⢙⢿⣿⣷⣌⢻⣿⣿⣿⣿⣿⣿⣿⣿⡟⣥⣾⣿⡿⡋⣅⠢⣝⡳⢮⠍⣘⣛⣛⣛⣛⣛⣛⣛⠛⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠙⠛⢛⡛⣛⢛⡛⣛⢂⠡⠞⣫⡴⢫⡾⣨⠙⡻⠿⡼⣿⣿⣿⣿⣿⣿⣿⣿⢱⠿⢟⠋⣅⢷⡝⣦⣙⠷⠌⣐⣛⣛⣛⢛⣛⠛⠛⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⠿⠷⠘⢫⣴⢟⣵⢏⣾⢣⡇⡄⣿⣿⣿⣿⣿⣿⣿⣿⢀⢺⡼⣧⠻⣮⡻⣮⠙⠁⠿⠿⠿⠛⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢣⡾⢣⣿⢳⡇⣿⣿⣿⣿⣿⣿⣿⣿⢸⡼⣷⡙⢷⠝⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠛⠃⣿⣿⣇⣿⣶⢼⣿⣿⠘⠛⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢟⣶⣃⡻⢿⣚⣶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣘⠍⡟⡆⣶⣶⢰⣿⣍⣥⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⡥⢚⣿⡩⠕⢘⡞⠢⠍⡿⢿⡫⢴⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢡⡌⠰⠃⠁⢀⣴⣿⠟⠀⠀⠈⠘⢏⢰⣷⣣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣘⢛⠓⠀⠀⠰⣿⣿⡁⢀⣴⣿⣦⡀⠈⠙⡏⣧⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢼⠁⣴⣦⡀⠈⢻⣿⣿⡟⠉⠻⣿⣦⠈⠽⠹⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⠡⡌⠀⠙⢿⣷⣤⣾⡿⢿⣷⣄⠀⠙⠋⢀⣠⡦⠱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⢟⢅⡄⠀⠙⠿⠋⠀⣠⣿⡿⠃⠀⠀⢤⢻⠻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢎⢓⡰⢀⠀⠀⢾⡿⠋⠀⠀⠀⣑⢢⣉⠍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠜⣻⣟⡠⠇⢰⣶⠠⠧⢚⣖⠛⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠅⠾⠠⠠⠛⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀          
{COLOR_RESET}"""

MATRIX_BANNER = f"""{COLOR_GREEN}┌─ [MATRIX DIGITAL ENGINE] ────────────────────────────────────────────────────────────────────────────┐
│  01001101 01000001 01010100 01010010 01001001 01011000  │  SYSTEM STATUS : ONLINE                               │
│  10110010 11001010 00110101 10100101 11000011 00101010  │  ENCRYPTION    : 256-BIT RSA                          │
│  00110100 01101001 01101110 01110100 01100101 01110010  │  CONNECTION    : ENCRYPTED NEURAL NODE                │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘{COLOR_RESET}"""

CYBERPUNK_BANNER = f"""{COLOR_NEON_PINK}
.▄▄▄  ▄▄▄ .▄▄▄  ▄▄▄·  ▄▄▄·     .▄▄▄  ▄▄▄ .   ▄▄▄· ▄▄▄ ...  ▄▄▄... dynamic UI interface
▐█ ▀. ▀▄.▀·▐█ ▀.▐█ ▀█ ▐█ ▀█     ▐█ ▀. ▀▄.▀·  ▐█ ▀█ ▐█ ▀.  · ▐█ ▀.  
▄▀▀▀█▄▐▀▀▪▄▄▀▀▀█▄▄█▀▀█▄▄█▀▀█    ▄▀▀▀█▄▐▀▀▪▄  ▄█▀▀█▄▄█▀▀█▄   ▄█▀▀█▄ 
▐█▄▪▐█▐█▄▄▌▐█▄▪▐█▐█ ▪▐█▐█ ▪▐█   ▐█▄▪▐█▐█▄▄▌  ▐█ ▪▐█▐█ ▪▐█   ▐█ ▪▐█ 
 ▀▀▀▀  ▀▀▀  ▀▀▀▀  ▀  ▀  ▀  ▀     ▀▀▀▀  ▀▀▀    ▀  ▀  ▀  ▀     ▀  ▀  
{COLOR_NEON_CYAN}════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{COLOR_RESET}"""

GHOST_BANNER = f"""{COLOR_WHITE}
         .---.
        /     \\
       | () () |  [ GHOST IN THE SHELL OS v4.09 ]
        \\  ^  /   -----------------------------------------
         |||||    SECURE NODE :: UNREGISTERED GHOST OPERATOR
         |||||    INTEGRITY   :: 99.8% STABLE
{COLOR_RESET}"""

DEVIL_BANNER = f"""{COLOR_RED}
             ,   ,
            (  /|  )
           , .--./  ,
          / /    \\ \\
         | |  0 0 | |   [ INFERNAL DEVIL CORE ]
         | |  .-. | |   ----------------------------------------
         \\ \\  --- / /   ACCESS LEVEL :: ROOT DEMON
          ` '--' `'     PAYLOADS     :: ARMED & READY
{COLOR_RESET}"""

RETRO_BANNER = f"""{COLOR_ORANGE}
 _________________________________________________________________________________________
/                                                                                         \\
|  ___ _____ _____ ___  ___   _   _  ___  _  _ _____ ___   ___ ___  ___   ___ _____ ___   |
| | _ |_   _|_   _/ _ \\| _ \\ | \\_/ |/ _ \\| \\/ |_   _/ _ \\ | _ \\_  )/ _ \\ / _ \\_   _/ _ \\  |
| |   / | |   | | | (_) |   / | . . | (_) | .` | | | | (_) ||  _// // (_) | (_) || | | (_) | |
| |_|\\ |_|   |_|  \\___/|_|\\_ |_|_|_|\\___/|_|\\_| |_|  \\___/ |_| /___|\\___/ \\___/ |_|  \\___/  |
\\_________________________________________________________________________________________/
{COLOR_RESET}"""

NEON_BANNER = f"""{COLOR_LIME}
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  ░▀█▀░█░█░█▀▀░█░█░█▀█░█▀█░█░█░█▀█░█░█░█▀█░█▀█░█░█    ░█▀█░█▀▀░█▀█░█▀█░█▀▀░█░█░▀█▀░█▀▀  │
│  ░░█░░█▀█░█▀▀░█▀█░█▀█░█▀▀░█▀█░█░█░█▀█░█░█░█░█░█▀█    ░█░█░█▀▀░█░█░█░█░▀▀█░█▀█░░█░░▀▀█  │
│  ░░▀░░▀░▀░▀▀▀░▀░▀░▀░▀░▀░░░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀░▀    ░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀  │
└────────────────────────────────────────────────────────────────────────────────────────┘{COLOR_RESET}"""

MORTY_EXACT_BANNER = f"""{COLOR_YELLOW}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠙⢿⣦⡀⠀⠀⠀⢀⣾⡿⠉⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠙⣿⣄⣠⣴⡿⠋⠀⠀⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠈⠿⠟⠉⠀⠀⠀⢀⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⣿⡿⠿⠿⠿⠷⣶⣾⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣤⣤⣴⣶⣶⡀
⠀⠀⠀⠹⣿⡀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠚⠉⠉⠉⠉⠓⠲⣄⠀⠈⠉⠉⠉⠁⣨⣿⠟
⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⢀⡔⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⢠⣾⡏⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣷⠀⠀⢀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⢠⣾⡏⠀⠀⠀
⠀⢀⣠⣴⡾⠟⠋⠀⠀⣸⠀⠀⠀⣴⣒⣒⣛⣛⣛⣋⣉⣉⣉⣙⣛⣷⠀⠙⠿⣶⣤⡀
⣾⣿⡋⠁⠀⠀⠀⠀⠀⡏⠀⠀⡄⠉⠉⠀⠀⠀⠹⢹⠃⠀⠀⠀⠀⠙⡄⠀⠀⣨⣿⠟
⠈⠛⠿⣷⣦⣀⠀⠀⠀⡇⠀⠸⡼⠻⠛⡿⠿⠿⡿⢿⠛⠹⠟⠉⠉⠙⡇⣠⣾⠟⠁⠀⠀⠀⠀
⠀⠀⠀⢀⣽⣿⠇⠀⠀⡇⠀⠀⢳⣄⠀⣀⣈⣉⠁⠀⠠⡀⠸⡇⠠⠤⠴⣟⣧⡿⠇⠀⠀⠀⠀
⠀⢠⣴⡿⠋⠁⠀⠀⣀⡧⠄⠀⠦⣀⣉⣛⣛⠁⠀⠠⡀⠘⡆⠠⠤⠴⢿⣄⠀⠙⣿⣦⠀
⠀⠹⢿⣦⣤⣀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣄⡆⠀⠀⠀⣼⢘⣷⡿⠟⠋⠀⠀⠀⠀
⠀⠀⠀⠈⠉⣿⡇⠈⠣⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠻⣇⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣤⣤⣤⣧⠀⢀⡆⣠⠴⠒⠋⢹⠉⠉⢹⠗⠒⠄⣧⣾⡿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠉⠛⠁⣿⣧⣉⣼⠀⠳⠤⠀⠀⠀⠈⣇⡖⡍⠀⠠⣟⣧⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠁⣷⣄⠀⠀⠀⠀⠁⠀⠀⠀⣠⣧⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣉⣿⣷⠲⠤⠤⠤⣤⣶⣿⣟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⡿⠿⠛⠛⠋⢹⠉⠉⢹⠗⠒⠄⣟⣧⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣧⣶⠏⠀⠀⠀⠀⠀⠀⠀⠀
{COLOR_RESET}"""

SPACE_BANNER = f"""{COLOR_PURPLE}
      _                      
     / \\     [ DEEP SPACE OBSERVATORY MAIN NODE ]
    / _ \\    ----------------------------------------------------
   / ___ \\   COORDINATES :: 45.2911° N, 12.0041° E
  /_/   \\_\\  STATUS      :: SIGNAL RECEIVED FROM EXOPLANET X-9
{COLOR_RESET}"""


MEDIEVAL_MAIN_BANNER = f"""{COLOR_YELLOW}
    .---.                         .---.
   /     \\       ⚔️ THE GUILD ARCHIVES ⚔️       /     \\
  |       |    ---------------------------------     |       |
  |  (@)  |      [ THE MAIN COMMAND NEXUS ]      |  (@)  |
  |       |                                          |       |
 /=========\\       _.-'\\         /'-._       /=========\\
|===========|   _.'     \\       /     '._   |===========|
|===|===|===|  (_.-------'     '-------._)  |===|===|===|
{COLOR_RESET}"""

STEAMPUNK_MAIN_BANNER = f"""{COLOR_ORANGE}
  _..-------.._               _..-------.._
.'    _....._    '.   ⚙️   ⚙️   .'    _....._    '.
|    .'       '.    \\  VICTORIAN  /    .'       '.    |
|   |   (O)     |    |   ENGINE   |    |   (O)     |   |
|    '._______.-'    |    ROOM    |    '._______.-'    |
 \\                  /              \\                  /
  '._______________.'                '._______________.'
     | | |     | | |                    | | |     | | |
{COLOR_RESET}"""

SYNTH_MAIN_BANNER = f"""{COLOR_NEON_PINK}
     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
     █  ★ 1984 VAPOR_MAINFRAME CORE ARCHITECTURE ★  █
     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
           \\    /     \\    /     \\    /     \\    /
            \\  /       \\  /       \\  /       \\  /
             \\/         \\/         \\/         \\/
{COLOR_RESET}"""

WASTELAND_MAIN_BANNER = f"""{COLOR_RED}
 //\\\\//\\\\//\\\\//\\\\//\\\\//\\\\//\\\\//\\\\//\\\\//\\\\//\\\\//\\\\//\\\\
<  [!] SECTOR ZERO: APOCALYPTIC CONTROL CORE [!]  >
 \\\\//\\\\//\\\\//\\\\//\\\\//\\\\//\\\\//\\\\//\\\\//\\\\//\\\\//\\\\//\\\\//\\\\
      _.-^^---....,,--      ,,--....---^^-_
   _--'-'               \\--/               '-'--_
  <   [CAUTION: HOSTILE ENVIRONMENT DETECTED]   >
{COLOR_RESET}"""

CORPORATE_MAIN_BANNER = f"""{COLOR_WHITE}
╔══════════════════════════════════════════════════════════════╗
║            OMNI-CORP EXECUTIVE SUITE TERMINAL              ║
║                CENTRAL COMMAND INTERFACE                   ║
╠══════════════════════════════════════════════════════════════╣
║ STATUS: SECURE // LEVEL 5 CLEARANCE // NODE: ACTIVE        ║
╚══════════════════════════════════════════════════════════════╝
{COLOR_RESET}"""

ABYSSAL_MAIN_BANNER = f"""{COLOR_CYAN}
       ,---.       .---------------------------------------.       ,---.
      /     \\     /      🌊 ABYSSAL DEEP-SEA NEXUS 🌊      \\     /     \\
     |  [o]  |   |   -------------------------------------   |   |  [o]  |
      \\     /    |     DEPTH: 11,000m // PRESSURE: MAX      |    \\     /
       `---'     |   -------------------------------------   |     `---'
     .-'   '-.    \\          [ SUB-ZERO SECTOR ]            /    .-'   '-.
   .'         '.   '---------------------------------------'   .'         '.
  /     \\ /     \\                                             /     \\ /     \\
 |       V       |               ~ ~ ~ ~ ~ ~ ~ ~ ~            |       V       |
  \\             /              .----.   .----.                 \\             /
   '.________.-'              (      \\ /      )                 '.________.-'
{COLOR_RESET}"""

VOID_MAIN_BANNER = f"""{COLOR_PURPLE}
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟
⣿⣿⣿⣿⣿⣿⣿⣯⣻⣿⣿⣿⣿⣿⡿⣽⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣞⢿⣿⣷⡝⢛⣻⣭⣕⣴⣏⣴⣿⣿⢿⢟⣮⡻⣿⡿⣋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣯⡻⢫⣾⢿⣭⣿⣻⣼⣇⣿⣿⣿⣿⡿⠁⠁⠈⠁⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣷⢟⣴⡿⡿⣿⣿⠿⢿⣿⠿⠉⠁⣿⢿⢇⠀⠀⣐⣸⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣯⣭⣍⣭⣭⡅⡿⣧⣋⠁⣿⠑⠀⢁⣹⡇⣀⣤⡏⡐⡠⢐⠿⠼⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⠟⣃⡒⢍⡁⠐⣽⣿⣿⣿⡿⠑⠙⠿⠿⠹⢇⠁⣼⢻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⢏⢤⣿⢣⡰⢌⠸⣭⢍⠁⠁⠀⠀⠀⠀⠀⠀⠸⣀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⢟⣵⣺⣣⣟⣾⣿⠸⡳⣙⢂⠢⡀⠀⠀⠀⠀⠀⠀⡇⣄⣞⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣯⣿⣿⣿⣟⣿⣿⣿⣼⢷⣿⣞⠐⣌⠒⠀⠀⠀⠈⢠⡇⣿⣿⣿⠆⠉⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⡿⣾⣸⣿⢸⣩⣧⠳⣤⠀⣠⡞⣼⡏⠉⠹⣇⠀⠀⠀⠘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⣿⢹⣧⣻⣶⠈⠙⣿⣿⠟⠀⠀⠀⠀⠀⠢⠀⠈⣮⣟⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣼⣿⣿⠇⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣤⣀⠋⣟⡿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⣷⣿⣷⣈⣝⣻⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⡇⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⢻⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠫⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣜⣛⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⡇⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⢿⡇
{COLOR_RESET}"""

UI_MAP = {
    "1":  ("Terminal UI (Default)", TERMINAL_BANNER, COLOR_GREEN),
    "2":  ("Planet UI", PLANET_BANNER, COLOR_CYAN),
    "3":  ("Mainframe UI", MAINFRAME_BANNER, COLOR_GREEN),
    "4":  ("Reaper UI", REAPER_BANNER, COLOR_RED),
    "5":  ("Hitla UI", HITLA_BANNER, COLOR_MAGENTA),
    "6":  ("Matrix UI", MATRIX_BANNER, COLOR_GREEN),
    "7":  ("Cyberpunk 2077 UI", CYBERPUNK_BANNER, COLOR_NEON_PINK),
    "8":  ("Ghost Shell UI", GHOST_BANNER, COLOR_WHITE),
    "9":  ("Devil Core UI", DEVIL_BANNER, COLOR_RED),
    "10": ("Retro 80s Synth UI", RETRO_BANNER, COLOR_ORANGE),
    "11": ("Neon Hack UI", NEON_BANNER, COLOR_LIME),
    "12": ("Deep Space Node UI", SPACE_BANNER, COLOR_PURPLE),
    "13": ("Morty Exact ASCII Art UI", MORTY_EXACT_BANNER, COLOR_YELLOW),
    "14": ("Medieval UI", MEDIEVAL_MAIN_BANNER, COLOR_YELLOW),
    "15": ("Steampunk UI", STEAMPUNK_MAIN_BANNER, COLOR_ORANGE),
    "16": ("Synthwave UI", SYNTH_MAIN_BANNER, COLOR_NEON_PINK),
    "17": ("Wasteland UI", WASTELAND_MAIN_BANNER, COLOR_RED),
    "18": ("Corporate UI", CORPORATE_MAIN_BANNER, COLOR_WHITE),
    "19": ("Abyssal UI", ABYSSAL_MAIN_BANNER, COLOR_CYAN),
    "20": ("Void UI", VOID_MAIN_BANNER, COLOR_PURPLE),
}

DIR_THEME_STYLES = {
    "1":  {"plain": True},
    "2":  {"color": COLOR_CYAN,       "marker": "◯"},
    "3":  {"color": COLOR_GREEN,       "marker": "█"},
    "4":  {"color": COLOR_RED,        "marker": "☠"},
    "5":  {"color": COLOR_MAGENTA,    "marker": "✦"},
    "6":  {"color": COLOR_CYAN,       "marker": "0"},
    "7":  {"color": COLOR_NEON_PINK,  "marker": "#"},
    "8":  {"color": COLOR_WHITE,      "marker": "👻"},
    "9":  {"color": COLOR_RED,        "marker": "🔥"},
    "10": {"color": COLOR_YELLOW,     "marker": "◆"},
    "11": {"color": COLOR_LIME,       "marker": "◉"},
    "12": {"color": COLOR_PURPLE,      "marker": "★"},
    "13": {"color": COLOR_YELLOW,     "marker": "🌀"},
    "14": {"color": COLOR_YELLOW,     "marker": "⚔️"},
    "15": {"color": COLOR_ORANGE,     "marker": "⚙️"},
    "16": {"color": COLOR_NEON_PINK,   "marker": "★"},
    "17": {"color": COLOR_RED,        "marker": "☣"},
    "18": {"color": COLOR_WHITE,      "marker": "◼"},
    "19": {"color": COLOR_CYAN,       "marker": "🌊"},
    "20": {"color": COLOR_PURPLE,     "marker": "□"},
}


try:
    from core.dir_banners import get_dir_banner
    _HAS_DIR_BANNERS = True
except Exception:
    get_dir_banner = None
    _HAS_DIR_BANNERS = False


def render_directory_ui(theme_key, dir_id, items=None):
    if get_dir_banner is not None:
        banner = get_dir_banner(dir_id, theme_key)
        if banner:
            print(banner)
            return

    style = DIR_THEME_STYLES.get(theme_key, DIR_THEME_STYLES.get("1", {}))
    if style.get("plain"):
        print(f"  [DIRECTORY {dir_id}]")
        print()
        if items:
            maxw = max(len(item[1]) for item in items)
            for item in items:
                raw_key = item[0]
                key = f"{int(raw_key):02d}" if str(raw_key).isdigit() else str(raw_key)
                name = item[1]
                desc = item[2] if len(item) > 2 else ""
                print(f"  [{key}] {name.ljust(maxw)} - {desc}")


def load_theme():
    try:
        with open(CONFIG_PATH, "r") as f:
            return json.load(f).get("ui_theme", "1")
    except Exception:
        return "1"


def save_theme(theme_key):
    try:
        data = {}
        if os.path.exists(CONFIG_PATH):
            try:
                with open(CONFIG_PATH, "r") as f:
                    data = json.load(f)
            except Exception:
                data = {}
        data["ui_theme"] = str(theme_key)
        with open(CONFIG_PATH, "w") as f:
            json.dump(data, ensure_ascii=False, indent=4, fp=f)
        return True
    except Exception as e:
        print(f"{COLOR_RED}[-] Error saving theme config: {e}{COLOR_RESET}")
        return False


def show_theme(theme_key):
    _, banner_text, _ = UI_MAP.get(theme_key, UI_MAP["1"])
    print(banner_text)


def handle_customize(current_ui_key):
    print(f"\n{COLOR_BOLD}Select UI Theme (1-20):{COLOR_RESET}")
    for key, (name, _, color_code) in UI_MAP.items():
        prefix = f"{COLOR_YELLOW}->{COLOR_RESET}" if key == str(current_ui_key) else "  "
        print(f"{prefix} {key.rjust(2)}. {color_code}{name}{COLOR_RESET}")

    choice = input(f"\n{COLOR_BOLD}Enter theme index (1-20): {COLOR_RESET}").strip()
    if choice in UI_MAP:
        save_theme(choice)
        print(f"\n{COLOR_GREEN}[+] Theme successfully changed to {UI_MAP[choice][0]}. Reloading...{COLOR_RESET}")
        time.sleep(0.5)
        return choice
    else:
        print(f"\n{COLOR_RED}[-] Invalid selection. Keeping current theme.{COLOR_RESET}")
        return current_ui_key

