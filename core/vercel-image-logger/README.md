# Vercel Image Logger Deployment

## Quick Deploy

1. Install Vercel CLI:
   ```
   npm i -g vercel
   ```

2. Navigate to this folder:
   ```
   cd vercel-image-logger
   ```

3. Deploy:
   ```
   vercel --prod
   ```

4. Copy the public URL Vercel gives you and share it with your target.

## Features
- Serves the "dont middle click" GIF with Open Graph tags
- Logs visitor IP, User-Agent, and timestamp
- `/api/logs` endpoint to view captured data
- Mainframe can monitor logs in real-time

## Structure
- `api/track.js` - Vercel serverless function
- `vercel.json` - Vercel routing config
- `package.json` - Project metadata

## Note
Vercel serverless functions are stateless. Logs stored in `/tmp` are ephemeral and may be lost between cold starts. For persistent logging, consider adding Vercel KV or a database.
