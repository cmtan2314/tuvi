"""Gọi engine Bắc phái (engine/, code tuvibacphai chạy trong jsdom) và chuẩn hóa kết quả.

Engine trả mỗi cung: chính tinh, phụ tinh kèm độ sáng (M miếu, V vượng, Đ đắc, B bình, N nhàn, H hãm),
sao lưu (Đv. đại vận, L. lưu niên, N. lưu nguyệt...), phi hóa, vòng sao, Tràng Sinh, Tuần Triệt.

Tìm node theo thứ tự: biến môi trường TUVI_NODE, <skill>/engine/node, `node` trong PATH.
jsdom: <skill>/engine/node_modules (cài bằng `npm install` trong engine/ nếu thiếu).
"""
import json
import os
import re
import shutil
import subprocess
from pathlib import Path

ENGINE = Path(__file__).resolve().parent.parent / "engine"
CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
# Thang độ sáng của engine (bảng Bắc phái, khác sách Việt ở một số vị trí):
# miếu > vượng > đắc > bình > nhàn > hãm
SANG = {"M": "miếu", "V": "vượng", "Đ": "đắc", "B": "bình", "N": "nhàn", "H": "hãm"}

# tên trên trang -> tên dùng trong laso.py
TEN = {
    "Thiên quan": "Thiên Quan", "Thiên phúc": "Thiên Phúc", "Tả Phù": "Tả Phụ", "Thiên Diêu": "Thiên Riêu",
    "Thiên Hỉ": "Thiên Hỷ", "Hỉ Thần": "Hỷ Thần", "Lưu Niên Văn Tinh": "Văn Tinh", "LN Văn Tinh": "Văn Tinh",
    "Phục Binh": "Phục Binh", "Tràng sinh": "Tràng Sinh", "Thiên Tọa": "Bát Tọa", "Tọa": "Bát Tọa",
    "Đào Hoa": "Đào Hoa", "Phá Toái": "Phá Toái", "Thai Phụ": "Thai Phụ", "Thiên Thọ": "Thiên Thọ",
}


def node_bin():
    for c in (os.environ.get("TUVI_NODE"), str(ENGINE / "node"), shutil.which("node")):
        if c and Path(c).exists():
            return c
    return None


def san_sang():
    """(True, '') nếu chạy được engine; (False, lý do) nếu không."""
    if not node_bin():
        return False, "không tìm thấy node (đặt TUVI_NODE, hoặc cài node vào PATH)"
    if not (ENGINE / "node_modules" / "jsdom").exists():
        return False, f"thiếu jsdom: chạy `npm install` trong {ENGINE}"
    return True, ""


def tach(nhan: str):
    """'Đà La (H)' -> ('Đà La', 'hãm');  'CỰ MÔN+ (V)' -> ('Cự Môn', 'vượng')."""
    m = re.match(r"^(.*?)\s*([+-])?\s*(?:\((\w)\))?\s*$", nhan.strip())
    ten, sang = m.group(1).strip(), SANG.get(m.group(3) or "", "")
    if ten.isupper():
        ten = " ".join(w.capitalize() for w in ten.lower().split())
    return TEN.get(ten, ten), sang


def chay(ngay, thang, nam, gio, phut=1, nu=False, am=False, nhuan=False, namxem=None):
    """Chạy engine, trả {'center': [...], 'cung': {chi: {...}}}. gio: giờ 0-23 (dương) hoặc chi (âm)."""
    ok, why = san_sang()
    if not ok:
        raise RuntimeError(why)
    cmd = [node_bin(), str(ENGINE / "lasotuvi.js"), "--ngay", str(ngay), "--thang", str(thang),
           "--nam", str(nam), "--gio", str(gio), "--phut", str(max(1, phut)),
           "--gioitinh", "nu" if nu else "nam", "--lich", "am" if am else "duong", "--json"]
    if nhuan:
        cmd.append("--nhuan")
    if namxem:
        cmd += ["--namxem", str(namxem)]
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=60, cwd=ENGINE)
    if out.returncode != 0:
        raise RuntimeError(out.stderr.strip()[-500:])
    d = json.loads(out.stdout)
    res = {"center": d["center"], "cung": {}}
    for chi, c in d["cung"].items():
        chinh = [tach(s) for s in c["chinhTinh"]]
        phu = [tach(s) for s in c["phuTinh"]]
        luu = [tach(s) for s in c["saoLuu"]]
        res["cung"][CHI.index(chi)] = {
            "chuc": c["chuc"], "chinh": chinh, "phu": phu, "luu": luu, "vong": c["vong"],
            "phi_hoa": c["phiHoa"], "trang_sinh": c["truongSinh"], "tuan_triet": c["tuanTriet"],
            "dai_van": c["daiVan"],
        }
    return res


def vi_tri(res):
    """{tên sao: (chi, độ sáng)} cho chính tinh + phụ tinh + vòng sao của engine."""
    pos = {}
    for p, c in res["cung"].items():
        for ten, sang in c["chinh"] + c["phu"]:
            pos.setdefault(ten, (p, sang))
        for v in c["vong"]:
            ten, sang = tach(v)
            pos.setdefault(ten, (p, sang))
    return pos
