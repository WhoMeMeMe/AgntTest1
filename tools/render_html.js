// Render a time-driven HTML animation to MP4.
// The page must expose window.renderAt(seconds), window.DURATION and window.FPS.
// Usage: node tools/render_html.js <page.html> <out.mp4> [--still <seconds> <out.png>]
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');

(async () => {
  const [page_, out, flag, stillT, stillOut] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(page_));
  await page.evaluate(() => document.fonts.ready);
  if (flag === '--still') {
    await page.evaluate((t) => window.renderAt(t), Number(stillT));
    await page.screenshot({ path: stillOut });
    await browser.close();
    return;
  }
  const { dur, fps } = await page.evaluate(() => ({ dur: window.DURATION, fps: window.FPS }));
  console.log('SFX_TIMES ' + JSON.stringify(await page.evaluate(() => window.SFX_TIMES || [])));
  const ff = spawn('ffmpeg', ['-loglevel', 'error', '-y', '-f', 'image2pipe', '-framerate', String(fps),
    '-c:v', 'mjpeg', '-i', '-', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '16', out],
    { stdio: ['pipe', 'inherit', 'inherit'] });
  const total = Math.round(dur * fps);
  for (let i = 0; i < total; i++) {
    await page.evaluate((t) => window.renderAt(t), i / fps);
    const buf = await page.screenshot({ type: 'jpeg', quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once('drain', r));
  }
  ff.stdin.end();
  await new Promise((r) => ff.on('close', r));
  await browser.close();
  console.log(`rendered ${total} frames -> ${out}`);
})();
