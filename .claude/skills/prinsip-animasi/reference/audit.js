const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 900, height: 900 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + process.cwd() + '/studio-gaya3.html'); await p.waitForTimeout(300);
  await p.evaluate(() => { document.getElementById('pause').click(); });
  const res = await p.evaluate(() => {
    const L = window.g3lists(), out = { nan: [], oob: [], jump: [], thrown: [], counts: { frames: 0, poseFrames: 0 } };
    const host = document.createElementNS('http://www.w3.org/2000/svg', 'svg'); host.setAttribute('viewBox', '-70 -138 540 621'); host.style.cssText = 'position:absolute;left:0;top:0;width:400px;height:460px'; document.body.appendChild(host);
    const num = ['y', 'x', 'rot', 'tilt', 'lean', 'sq', 'hdy', 'turn', 'sit'], lim = { y: 26, x: 30, rot: 34, tilt: 14, lean: 10, sq: .13, hdy: 9, turn: 22, sit: .5 };
    // 1) pose continuity for every action x mood, both modes, 6 seconds at 25 fps
    for (const pri of [true, false]) { document.getElementById('pri').checked = pri;
      for (const a of L.acts) for (const m of L.moods) { let prev = null;
        for (let f = 0; f <= 150; f++) { const t = f / 25; let r; try { r = window.g3render('nisa', a, m, 'd34', t); } catch (e) { out.thrown.push([pri, a, m, t, e.message].join('|')); break; }
          const ps = r.pose; out.counts.poseFrames++;
          for (const k of num) if (!isFinite(ps[k])) out.nan.push(['pose', pri, a, m, t, k].join('|'));
          for (const k of ['aL', 'aR', 'lL', 'lR']) for (const v of ps[k]) if (!isFinite(v)) out.nan.push(['pose', pri, a, m, t, k].join('|'));
          if (prev) { for (const k of num) { const d = Math.abs(ps[k] - prev[k]); if (d > lim[k]) out.jump.push([pri ? '12p' : 'acuan', a, m, 't=' + t.toFixed(2), k, d.toFixed(2)].join(' ')); }
            for (const k of ['aL', 'aR', 'lL', 'lR']) { const d0 = Math.abs(ps[k][0] - prev[k][0]), d2 = Math.abs(ps[k][2] - prev[k][2]); if (d0 > 42 || d2 > 55) out.jump.push([pri ? '12p' : 'acuan', a, m, 't=' + t.toFixed(2), k, Math.max(d0, d2).toFixed(0)].join(' ')); } }
          prev = ps; } } }
    document.getElementById('pri').checked = true;
    // 2) drawing check: every cast x action x view, 10 frames; NaN in markup and out-of-stage geometry
    const ts = [0, .1, .22, .3, .45, .6, .82, 1.0, 1.6, 3.9];
    for (const c of L.cast) for (const a of L.acts) for (const v of L.views) for (const t of ts) { let r; try { r = window.g3render(c, a, 'netral', v, t); } catch (e) { out.thrown.push([c, a, v, t, e.message].join('|')); continue; }
      out.counts.frames++; if (/NaN|undefined|Infinity/.test(r.svg)) { out.nan.push(['svg', c, a, v, t].join('|')); continue; }
      host.innerHTML = r.svg; const bb = host.getBBox(); if (bb.x < -68 || bb.y < -136 || bb.x + bb.width > 468 || bb.y + bb.height > 483) out.oob.push([c || 'manusia', a, v, 't=' + t, 'x' + bb.x.toFixed(0) + '..' + (bb.x + bb.width).toFixed(0), 'y' + bb.y.toFixed(0) + '..' + (bb.y + bb.height).toFixed(0)].join(' ')); }
    // 3) moods on walking/standing/sitting for every cast, front + side
    for (const c of L.cast) for (const m of L.moods) for (const a of ['diam', 'jalan', 'duduk']) for (const v of ['depan', 'samping']) for (const t of [.3, 3.9]) { let r; try { r = window.g3render(c, a, m, v, t); } catch (e) { out.thrown.push([c, a, m, v, t, e.message].join('|')); continue; }
      out.counts.frames++; if (/NaN|undefined|Infinity/.test(r.svg)) out.nan.push(['svg', c, a, m, v, t].join('|')); else { host.innerHTML = r.svg; const bb = host.getBBox(); if (bb.x < -68 || bb.y < -136 || bb.x + bb.width > 468 || bb.y + bb.height > 483) out.oob.push([c || 'manusia', a, m, v, 't=' + t, 'x' + bb.x.toFixed(0) + '..' + (bb.x + bb.width).toFixed(0), 'y' + bb.y.toFixed(0) + '..' + (bb.y + bb.height).toFixed(0)].join(' ')); } }
    host.remove(); return out; });
  console.log('counts', JSON.stringify(res.counts), 'pageerrors', errs.length, errs.slice(0, 3));
  const uniq = a => [...new Set(a)];
  console.log('THROWN', res.thrown.length, uniq(res.thrown.map(x => x.split('|').slice(-1)[0])).slice(0, 5));
  console.log('NAN', res.nan.length, res.nan.slice(0, 8));
  const jg = {}; res.jump.forEach(j => { const k = j.split(' ').slice(0, 2).join(' ') + ' ' + j.split(' ')[4]; (jg[k] = jg[k] || []).push(j); });
  console.log('JUMP groups', Object.keys(jg).length); Object.keys(jg).slice(0, 40).forEach(k => console.log('  ', k, 'x' + jg[k].length, '| e.g.', jg[k][0]));
  const og = {}; res.oob.forEach(j => { const w = j.split(' '); const k = w[1]; (og[k] = og[k] || []).push(j); });
  console.log('OOB total', res.oob.length); Object.keys(og).forEach(k => console.log('  ', k, 'x' + og[k].length, '| e.g.', og[k][0], '||', og[k][og[k].length - 1]));
  await b.close();
})();
