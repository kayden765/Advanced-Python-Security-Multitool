@echo off
chcp 65001 >nul
title MAINFRAME - Complete Setup Installer
echo ============================================
echo  MAINFRAME Complete Setup Installer
echo  40-IN-1 Security Platform ^| v5.90
echo ============================================
echo.

:: Check for Administrator
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Please run this script as Administrator!
    echo     Right-click the file and select "Run as administrator"
    pause
    exit /b 1
)

set "PYTHON=python"
where python >nul 2>nul
if %errorlevel% neq 0 (
    set "PYTHON=python3"
)

set "SCRIPT_DIR=%~dp0"
set "IMPACKET_DIR=%SCRIPT_DIR%core\impacket_scripts"

echo [*] Working directory: %SCRIPT_DIR%
echo [*] Python: %PYTHON%
echo.

:: ============================================
:: STEP 1: Python Dependencies
:: ============================================
echo [1/6] Installing Python dependencies...
%PYTHON% -m pip install --upgrade pip
%PYTHON% -m pip install -r "%SCRIPT_DIR%requirements.txt"
if %errorlevel% equ 0 (
    echo [+] Python dependencies installed successfully.
) else (
    echo [!] Some Python dependencies failed. Continuing anyway...
)
echo.

:: ============================================
:: STEP 2: Impacket Library + Scripts
:: ============================================
echo [2/6] Installing Impacket library...
%PYTHON% -m pip install --upgrade impacket
if %errorlevel% equ 0 (
    echo [+] Impacket library installed.
) else (
    echo [!] Failed to install Impacket.
)
echo.

echo [2/6] Downloading Impacket scripts (psexec.py / wmiexec.py)...
if not exist "%IMPACKET_DIR%" mkdir "%IMPACKET_DIR%"
powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/fortra/impacket/master/examples/psexec.py' -OutFile '%IMPACKET_DIR%\psexec.py' -UseBasicParsing"
powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/fortra/impacket/master/examples/wmiexec.py' -OutFile '%IMPACKET_DIR%\wmiexec.py' -UseBasicParsing"
if exist "%IMPACKET_DIR%\psexec.py" (
    echo [+] Impacket scripts downloaded to %IMPACKET_DIR%
) else (
    echo [!] Failed to download Impacket scripts.
)
echo.

:: ============================================
:: STEP 3: Chocolatey Setup
:: ============================================
echo [3/6] Checking Chocolatey (package manager)...
where choco >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] Chocolatey not found. Installing Chocolatey...
    echo     This requires an active internet connection.
    powershell -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
    
    echo [+] Chocolatey installation attempted.
    
    :: Refresh PATH for current session so choco is available
    set "PATH=%PATH%;C:\ProgramData\chocolatey\bin"
    refreshenv >nul 2>&1
) else (
    echo [=] Chocolatey is already installed.
)
echo.

:: ============================================
:: STEP 4: Nmap
:: ============================================
echo [4/7] Installing Nmap...
where nmap >nul 2>nul
if %errorlevel% equ 0 (
    echo [=] Nmap is already installed.
) else (
    echo     Attempting installation via winget...
    winget install --id Insecure.Nmap --accept-package-agreements --accept-source-agreements
    if %errorlevel% equ 0 (
        echo [+] Nmap installed via winget.
    ) else (
        echo [!] winget install failed.
        echo [!] Please install manually from https://nmap.org/
    )
)
echo.

:: ============================================
:: STEP 5: Hashcat
:: ============================================
echo [5/7] Installing Hashcat...
where hashcat >nul 2>nul
if %errorlevel% equ 0 (
    echo [=] Hashcat is already installed.
) else (
    echo     Installing via Chocolatey...
    choco install hashcat -y
    if %errorlevel% equ 0 (
        echo [+] Hashcat installed via Chocolatey.
    ) else (
        echo [!] Chocolatey install failed.
        echo [!] Please install manually from https://hashcat.net/hashcat/
    )
)

:: Add local hashcat folder to PATH if found
set "HASHCAT_LOCAL_DIR=%SCRIPT_DIR%hashcat-*"
if exist "%HASHCAT_LOCAL_DIR%" (
    echo [+] Found local Hashcat folder: %HASHCAT_LOCAL_DIR%
    echo     Adding to system PATH...
    powershell -Command "[Environment]::SetEnvironmentVariable('Path', [Environment]::GetEnvironmentVariable('Path', 'Machine') + ';%HASHCAT_LOCAL_DIR%', 'Machine')"
    set "PATH=%PATH%;%HASHCAT_LOCAL_DIR%"
    echo [+] Hashcat folder added to PATH.
) else (
    echo [!] No local hashcat-* folder found in %SCRIPT_DIR%
)
echo.

:: ============================================
:: STEP 6: Metasploit Framework
:: ============================================
echo [6/7] Installing Metasploit Framework...
where msfconsole >nul 2>nul
if %errorlevel% equ 0 (
    echo [=] Metasploit is already installed.
) else (
    echo     Checking for existing installation...
    if exist "C:\metasploit-framework\bin\msfconsole.bat" (
        echo [+] Found Metasploit at C:\metasploit-framework\
        echo     Adding to system PATH...
        powershell -Command "[Environment]::SetEnvironmentVariable('Path', [Environment]::GetEnvironmentVariable('Path', 'Machine') + ';C:\metasploit-framework\bin', 'Machine')"
        set "PATH=%PATH%;C:\metasploit-framework\bin"
        echo [+] Metasploit bin folder added to PATH.
    ) else (
        echo [!] Metasploit not found.
        echo [!] Please install manually from https://www.metasploit.com/download
    )
)
echo.

:: ============================================
:: STEP 7: Verification
:: ============================================
echo [7/7] Verifying installations...
echo.

set "FAILED=0"

where msfconsole >nul 2>nul
if %errorlevel% equ 0 (
    echo [+] msfconsole found
) else (
    echo [-] msfconsole NOT found
    set "FAILED=1"
)

where msfvenom >nul 2>nul
if %errorlevel% equ 0 (
    echo [+] msfvenom found
) else (
    echo [-] msfvenom NOT found
    set "FAILED=1"
)

where hashcat >nul 2>nul
if %errorlevel% equ 0 (
    echo [+] hashcat found
) else (
    echo [-] hashcat NOT found
    set "FAILED=1"
)

where nmap >nul 2>nul
if %errorlevel% equ 0 (
    echo [+] nmap found
) else (
    echo [-] nmap NOT found
    set "FAILED=1"
)

if exist "%IMPACKET_DIR%\psexec.py" (
    echo [+] psexec.py found at %IMPACKET_DIR%
) else (
    echo [-] psexec.py NOT found
    set "FAILED=1"
)

if exist "%IMPACKET_DIR%\wmiexec.py" (
    echo [+] wmiexec.py found at %IMPACKET_DIR%
) else (
    echo [-] wmiexec.py NOT found
    set "FAILED=1"
)

echo.
echo ============================================
if %FAILED% equ 0 (
    echo  ALL TOOLS INSTALLED SUCCESSFULLY!
) else (
    echo  SOME TOOLS FAILED TO INSTALL
)
echo ============================================
echo.
echo IMPORTANT:
echo   1. Close this terminal and run 'refreshenv'
echo   2. Or restart your terminal completely
echo   3. Run 'python mainframe.py'
echo   4. Select Sub-Directory 01 or 05 to test tools
echo.
echo If Chocolatey installs failed, install manually:
echo   - Nmap: https://nmap.org/
echo   - Hashcat: https://hashcat.net/hashcat/
echo   - Metasploit: https://www.metasploit.com/download
echo.
pause
