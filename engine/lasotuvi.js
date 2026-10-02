// Chạy code lá số của tuvibacphai.com/tuvilyso trong jsdom, ghi lại chữ vẽ trên canvas
// rồi in lá số Tử Vi ra dạng text.
//
// Dùng: node lasotuvi.js --ngay 18 --thang 2 --nam 1992 --gio 17 [--phut 1] [--gioitinh nam|nu]
//                        [--lich duong|am] [--nhuan] [--namxem 2026] [--ten "Tên"] [--gon] [--raw] [--json]
//   Âm lịch: --gio là tên chi (tý, sửu, dần...) hoặc số 1-12.
const fs = require('fs');
const path = require('path');
const { JSDOM, ResourceLoader, VirtualConsole } = require('jsdom');

const SRC = path.join(__dirname, 'source');
const CHI = ['tý', 'sửu', 'dần', 'mão', 'thìn', 'tỵ', 'ngọ', 'mùi', 'thân', 'dậu', 'tuất', 'hợi'];

function parseArgs(argv) {
  const a = { phut: 1, gioitinh: 'nam', lich: 'duong', nhuan: false, ten: 'Đương số', raw: false };
  for (let i = 0; i < argv.length; i++) {
    const k = argv[i].replace(/^--/, '');
    if (k === 'nhuan' || k === 'raw' || k === 'gon' || k === 'json') a[k] = true;
    else a[k] = argv[++i];
  }
  for (const k of ['ngay', 'thang', 'nam', 'gio']) {
    if (a[k] === undefined) throw new Error(`Thiếu --${k}`);
  }
  return a;
}

// Canvas giả: ghi lại mọi fillText kèm toạ độ thực (đã áp transform).
function makeRecorder(store) {
  let m = [1, 0, 0, 1, 0, 0];
  const stack = [];
  const mul = (n) => {
    const [a, b, c, d, e, f] = m;
    m = [a * n[0] + c * n[1], b * n[0] + d * n[1], a * n[2] + c * n[3], b * n[2] + d * n[3],
      a * n[4] + c * n[5] + e, b * n[4] + d * n[5] + f];
  };
  const ctx = {
    font: '10px Arial', fillStyle: 'black', strokeStyle: 'black', textAlign: 'left',
    globalAlpha: 1, lineWidth: 1, lineCap: 'butt', textBaseline: 'alphabetic',
    save() { stack.push([...m]); },
    restore() { if (stack.length) m = stack.pop(); },
    translate(x, y) { mul([1, 0, 0, 1, x, y]); },
    rotate(r) { mul([Math.cos(r), Math.sin(r), -Math.sin(r), Math.cos(r), 0, 0]); },
    scale(x, y) { mul([x, 0, 0, y, 0, 0]); },
    setTransform(a, b, c, d, e, f) { m = [a, b, c, d, e, f]; },
    resetTransform() { m = [1, 0, 0, 1, 0, 0]; },
    fillText(text, x, y) {
      store.push({ text: String(text), x: m[0] * x + m[2] * y + m[4], y: m[1] * x + m[3] * y + m[5],
        color: this.fillStyle, font: this.font });
    },
    strokeText() {},
    measureText(t) { return { width: String(t).length * 6 }; },
    createLinearGradient() { return { addColorStop() {} }; },
    createRadialGradient() { return { addColorStop() {} }; },
    drawImage() {},
    getImageData() { return { data: [] }; },
  };
  return new Proxy(ctx, { get: (t, p) => (p in t ? t[p] : () => {}) });
}

function setSelect(doc, id, value) {
  const el = doc.getElementById(id);
  if (!el) throw new Error(`Không thấy #${id}`);
  el.value = String(value);
  if (el.value !== String(value)) throw new Error(`#${id} không có giá trị ${value}`);
}

function run(args) {
  const html = fs.readFileSync(path.join(SRC, 'page.html'), 'utf8');
  const recorded = { current: [] };

  class LocalLoader extends ResourceLoader {
    fetch(url) {
      const name = path.basename(new URL(url).pathname);
      const file = path.join(SRC, name);
      if (!url.startsWith('file:') || !fs.existsSync(file)) return Promise.resolve(Buffer.from(''));
      return Promise.resolve(fs.readFileSync(file));
    }
  }
  const vc = new VirtualConsole();
  const errors = [];
  vc.on('jsdomError', (e) => errors.push(e.message));

  const dom = new JSDOM(html, {
    url: 'file://' + path.join(SRC, 'page.html'),
    runScripts: 'dangerously',
    resources: new LocalLoader(),
    virtualConsole: vc,
    pretendToBeVisual: true,
    beforeParse(window) {
      const ctxs = new WeakMap();
      window.HTMLCanvasElement.prototype.getContext = function () {
        if (!ctxs.has(this)) ctxs.set(this, makeRecorder({ push: (r) => recorded.current.push(r) }));
        return ctxs.get(this);
      };
      window.HTMLCanvasElement.prototype.toDataURL = () => 'data:,';
      // Phần Tứ Trụ của trang vẽ vào biến toàn cục `context` chưa khai báo -> cấp canvas giả để khỏi lỗi.
      window.context = makeRecorder({ push() {} });
      window.alert = () => {};
      window.screen = { width: 1920, height: 1080 };
    },
  });

  return new Promise((resolve, reject) => {
    dom.window.addEventListener('load', () => {
      try {
        const w = dom.window, doc = w.document;
        // Chế độ âm lịch của trang vẽ bố cục khác, nên đổi sang dương lịch bằng chính
        // hàm của trang rồi luôn chạy theo đường dương lịch.
        let { ngay, thang, nam, gio } = args;
        if (args.lich === 'am') {
          const chiIdx = CHI.indexOf(String(gio).toLowerCase()) + 1 || parseInt(gio, 10);
          if (!(chiIdx >= 1 && chiIdx <= 12)) throw new Error('--gio âm lịch là tên chi (ty, suu, dan...) hoặc số 1-12');
          [ngay, thang, nam] = w.convertLunar2Solar(+ngay, +thang, +nam, args.nhuan ? 1 : 0, 7);
          gio = 2 * chiIdx - 2; // giờ giữa của canh giờ, giống setup() của trang
        }
        setSelect(doc, 'ID_LICH', 1);
        setSelect(doc, 'ID_NAMDL', nam);
        setSelect(doc, 'ID_THANGDL', thang);
        w.ChangeNgay();
        setSelect(doc, 'ID_NGAYDL', ngay);
        setSelect(doc, 'ID_GIODL', gio);
        setSelect(doc, 'ID_PHUTDL', Math.max(1, +args.phut));
        const gt = args.gioitinh.toLowerCase().startsWith('n') && args.gioitinh.toLowerCase() !== 'nam' ? 0 : 1;
        doc.querySelectorAll('#ID_GIOITINH').forEach((el) => { el.value = String(gt); });
        doc.getElementById('ID_TEN').value = args.ten;
        if (args.namxem) setSelect(doc, 'ID_NAMXEM', args.namxem);

        // Chỉ lấy lần vẽ Thiên bàn (id_diaban = 0).
        const origBacot = w.bacot;
        const charts = [];
        w.bacot = function () {
          recorded.current = [];
          const r = origBacot.apply(this, arguments);
          charts.push(recorded.current);
          return r;
        };
        w.tutru = () => 'data:,';
        w.setup();
        resolve({ chart: charts[0] || [], errors, vars: w });
      } catch (e) {
        reject(e);
      }
    });
  });
}

module.exports = { run, parseArgs };

if (require.main === module) {
  const args = parseArgs(process.argv.slice(2));
  run(args).then(({ chart, errors }) => {
    if (errors.length) console.error('JS errors:', errors.slice(0, 5));
    if (args.raw) {
      for (const r of chart) console.log(`${r.x.toFixed(0)}\t${r.y.toFixed(0)}\t${r.color}\t${r.font}\t${r.text}`);
      return;
    }
    if (args.json) {
      console.log(JSON.stringify(require('./format').toJSON(chart)));
      return;
    }
    require('./format').print(chart, args);
  }).catch((e) => { console.error(e); process.exit(1); });
}
