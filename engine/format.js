// Gom các chữ vẽ trên canvas (đã ghi lại) thành lá số text theo 12 cung.
// Lá số gốc là lưới 4x4, mỗi ô 128x160 sau khi scale; 4 ô giữa là thông tin chung.
const CELL_W = 128;
const CELL_H = 160;

// Vị trí ô trên lưới (cột, hàng) -> địa chi, theo bố cục chuẩn (Tỵ ở góc trên trái).
const GRID_CHI = {
  '0,0': 'Tỵ', '1,0': 'Ngọ', '2,0': 'Mùi', '3,0': 'Thân',
  '3,1': 'Dậu', '3,2': 'Tuất', '3,3': 'Hợi', '2,3': 'Tý',
  '1,3': 'Sửu', '0,3': 'Dần', '0,2': 'Mão', '0,1': 'Thìn',
};
// Thứ tự đi vòng theo chiều kim đồng hồ.
const RING = ['0,0', '1,0', '2,0', '3,0', '3,1', '3,2', '3,3', '2,3', '1,3', '0,3', '0,2', '0,1'];

const CAN_ABBR = { 'G.': 'Giáp', 'Ấ.': 'Ất', 'B.': 'Bính', 'Đ.': 'Đinh', 'M.': 'Mậu',
  'K.': 'Kỷ', 'C.': 'Canh', 'T.': 'Tân', 'N.': 'Nhâm', 'Q.': 'Quý' };
// Tiền tố của sao lưu: Đv. đại vận, L. lưu niên, N. lưu nguyệt, Nh. lưu nhật, T. lưu thời.
const LUU_PREFIX = /^(Đv|LN|Nh|L|N|T)\.\s/;

// Chữ viết tắt của trang gốc -> tên đầy đủ.
const ABBR = [[/\bV\. Xương/, 'Văn Xương'], [/\bV\. Khúc\.?/, 'Văn Khúc'], [/\bKình D\./, 'Kình Dương'],
  [/\.(\s*[+-]?\s*\()/, '$1']];
const TRUONG_SINH_ABBR = { 'L. Quan': 'Lâm Quan', 'Đế V.': 'Đế Vượng', 'T. Sinh': 'Tràng Sinh' };
const clean = (s) => ABBR.reduce((acc, [re, to]) => acc.replace(re, to), s.replace(/\s+/g, ' ').trim());
const expandCan = (s) => s.replace(/^([A-ZĐẤ]\.)\s*/, (m, a) => (CAN_ABBR[a] ? CAN_ABBR[a] + ' ' : m));

function byPos(a, b) { return a.y - b.y || a.x - b.x; }

function parseCell(items) {
  const cell = { cung: '', chinhTinh: [], phuTinh: [], saoLuu: [], vong: [], phiHoa: [],
    dv: [], luuNien: [], truongSinh: '', tuanTriet: [], other: [] };
  for (const it of items.sort(byPos)) {
    const t = clean(it.text);
    if (!t) continue;
    const { rx, ry } = it;
    if (/^(Tuần|Triệt)$/.test(t)) cell.tuanTriet.push(t);
    else if (ry < 18 && rx > 40 && rx < 90) cell.cung = t;
    else if (rx < 12 && ry < 40) cell.dv.push(t);
    else if (rx > 115 && ry < 40) cell.luuNien.push(t);
    else if (ry >= 18 && ry < 44 && rx > 40 && rx < 90) cell.chinhTinh.push(t);
    else if (ry >= 44 && ry < 115) (LUU_PREFIX.test(t) ? cell.saoLuu : cell.phuTinh).push(t);
    else if (ry >= 115 && ry < 150 && /--->|tự hóa/.test(t)) cell.phiHoa.push(t);
    else if (ry >= 115 && ry < 150 && !/^L\.T/.test(t)) cell.vong.push(t);
    else if (ry >= 150 && rx > 40 && rx < 90 && !/^\d+$/.test(t)) cell.truongSinh = TRUONG_SINH_ABBR[t] || t;
    else cell.other.push(t);
  }
  return cell;
}

function parseCenter(items) {
  const rows = [];
  for (const it of items.sort(byPos)) {
    const t = clean(it.text);
    if (!t || /^https?:/.test(t)) continue;
    const row = rows.find((r) => Math.abs(r.y - it.y) < 4);
    if (row) row.items.push(it); else rows.push({ y: it.y, items: [it] });
  }
  return rows.map((r) => r.items.sort((a, b) => a.x - b.x).map((i) => clean(i.text)).join('  '));
}

function build(chart) {
  const cells = {};
  const center = [];
  for (const r of chart) {
    const col = Math.floor(r.x / CELL_W);
    const row = Math.floor(r.y / CELL_H);
    const key = `${col},${row}`;
    if (GRID_CHI[key]) (cells[key] = cells[key] || []).push({ ...r, rx: r.x - col * CELL_W, ry: r.y - row * CELL_H });
    else center.push(r);
  }
  const parsed = {};
  for (const key of RING) parsed[key] = parseCell(cells[key] || []);
  // Tuần/Triệt vẽ trên ranh giới với ô phía trên -> gán cho cả hai cung.
  const drawn = RING.map((key) => [key, [...parsed[key].tuanTriet]]);
  for (const [key, marks] of drawn) {
    const [col, row] = key.split(',').map(Number);
    const above = parsed[`${col},${row - 1}`];
    if (marks.length && above) above.tuanTriet.push(...marks);
  }
  return { parsed, center: parseCenter(center) };
}

function print(chart, args) {
  const { parsed, center } = build(chart);
  const out = [];
  out.push('=== LÁ SỐ TỬ VI ===');
  for (const line of center) out.push('  ' + line);
  out.push('');

  const start = RING.findIndex((k) => /^MỆNH/.test(parsed[k].cung));
  for (let i = 0; i < 12; i++) {
    const key = RING[(start + i) % 12];
    const c = parsed[key];
    const canChi = c.dv.find((s) => /^[A-ZĐẤ]\.\s/.test(s));
    const daiVan = c.dv.find((s) => /^\d+$/.test(s));
    const head = [`[${canChi ? expandCan(canChi) : GRID_CHI[key]}]`, c.cung || '?'];
    if (daiVan) head.push(`— đại vận ${daiVan}`);
    if (c.tuanTriet.length) head.push(`(${c.tuanTriet.join(', ')})`);
    out.push(head.join(' '));
    out.push(`  Chính tinh : ${c.chinhTinh.join(', ') || '(vô chính diệu)'}`);
    out.push(`  Phụ tinh   : ${c.phuTinh.join(', ')}`);
    out.push(`  Vòng sao   : ${c.vong.join(', ')}${c.truongSinh ? ', Tràng sinh: ' + c.truongSinh : ''}`);
    if (!args.gon) {
      out.push(`  Phi hóa    : ${c.phiHoa.join(' | ')}`);
      if (c.saoLuu.length) out.push(`  Sao lưu    : ${c.saoLuu.join(', ')}`);
      const dvCung = c.dv.find((s) => /^Đv\./.test(s));
      if (dvCung) out.push(`  Cung đại vận: ${dvCung.replace(/^Đv\.\s*/, '')}`);
      // Cột phải: [cung lưu niên của năm xem, can chi tiểu hạn, năm tiểu hạn].
      const luuCung = c.luuNien.find((s) => /^L\.\s/.test(s));
      const nam = c.luuNien.find((s) => /^\d{4}$/.test(s));
      const thCanChi = c.luuNien.find((s) => s !== luuCung && s !== nam);
      if (luuCung) out.push(`  Lưu niên   : cung ${luuCung.replace(/^L\.\s*/, '')}`);
      if (nam) out.push(`  Tiểu hạn   : năm ${nam}${thCanChi ? ` (${expandCan(thCanChi)})` : ''}`);
    }
    out.push('');
  }
  console.log(out.join('\n'));
}

// Dữ liệu có cấu trúc cho scripts/laso.py: mỗi cung theo địa chi, giữ nguyên nhãn của trang.
function toJSON(chart) {
  const { parsed, center } = build(chart);
  const cung = {};
  for (const key of RING) {
    const c = parsed[key];
    cung[GRID_CHI[key]] = {
      chuc: c.cung, canChi: (c.dv.find((s) => /^[A-ZĐẤ]\.\s/.test(s)) || ''),
      daiVan: c.dv.find((s) => /^\d+$/.test(s)) || '', chinhTinh: c.chinhTinh, phuTinh: c.phuTinh,
      saoLuu: c.saoLuu, vong: c.vong, phiHoa: c.phiHoa, truongSinh: c.truongSinh,
      tuanTriet: [...new Set(c.tuanTriet)], luuNien: c.luuNien, dv: c.dv, other: c.other,
    };
  }
  return { center, cung };
}

module.exports = { build, print, toJSON };
