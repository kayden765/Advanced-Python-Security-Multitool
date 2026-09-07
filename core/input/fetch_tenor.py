import urllib.request
import re
import sys

url = 'https://tenor.com/view/dont-middle-click-this-gif-gif-5755784118672546328'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8')
    matches = re.findall(r'https://media[^\s"<>]+\.gif', html)
    print('\n'.join(matches[:10]))
    if not matches:
        matches2 = re.findall(r'https://media[^\s"<>]+', html)
        print('\n'.join(matches2[:10]))
