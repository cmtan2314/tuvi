#!/usr/bin/env python3
"""Đối chiếu engine Bắc phái (JS) với laso.py + khamthien.py (Python) trên N lá số ngẫu nhiên: vị trí sao và phi hóa 12 cung.

Hai engine viết độc lập; Python lập theo quy ước Bắc phái (Hỏa Linh cùng chiều, Canh Khoa Âm Kỵ Đồng,
nhuận = tháng chính) thì mọi sao chung phải trùng, TRỪ các sao đã biết là khác quy ước:
  Thiên Thương/Thiên Sứ (BP đổi chỗ cho âm nam, dương nữ), Thiên Khôi/Thiên Việt (BP chia theo can âm dương),
  Thiên Quan (BP khác bảng ở tuổi Tân, Kỷ).
Lệch ở sao khác = lỗi thật ở một trong hai bên -> in ra và thoát mã 1.

  python3 doichieu.py [N=40] [seed=1]
"""
import random
import sys
from concurrent.futures import ThreadPoolExecutor

import engine
import khamthien
import laso

# tên cung engine -> tên cung khamthien
EC = {"mệnh": "Mệnh", "bào": "Huynh Đệ", "phu": "Phu Thê", "phối": "Phu Thê", "tử": "Tử Tức", "tài": "Tài Bạch",
      "tật": "Tật Ách", "di": "Thiên Di", "nô": "Nô Bộc", "quan": "Quan Lộc", "điền": "Điền Trạch",
      "phúc": "Phúc Đức", "phụ": "Phụ Mẫu"}

BIET = {"Thiên Thương", "Thiên Sứ", "Thiên Khôi", "Thiên Việt", "Thiên Quan"}


def mot(c):
    d, m, y, h, nu = c
    e = engine.chay(d, m, y, h, nu=nu)
    ld, lm, ly, _ = laso.solar_to_lunar(d, m, y, 7.0)
    r = laso.lap_la_so(ld, lm, ly, laso.gio_chi(h), not nu, canh_ky_dong=True, hoa_linh_cung_chieu=True)
    pe = engine.vi_tri(e)
    lech = [(t, laso.CHI[p], laso.CHI[pe[t][0]]) for t, p in r["sao"].items()
            if t in pe and t not in BIET and pe[t][0] != p]
    # phi hóa 12 cung: khamthien.py (Python) so với engine
    B = khamthien.Ban(r["menh"], r["_raw"]["can_cung"], r["sao"])
    for p, ce in e["cung"].items():
        eng = {}
        for x in ce["phi_hoa"]:
            hoa, _, dich = x.partition(" ")
            eng[hoa] = p if "tự hóa" in dich else B.vi[EC[dich.split()[-1]]]
        py = {hoa: q for hoa, _, q in B.phi(p)}
        if eng and eng != py:  # engine đôi khi bỏ trống phi hóa (năm sinh tương lai)
            lech.append(("phi hóa " + laso.CHI[p], py, eng))
    return c, lech


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    random.seed(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
    cases = [(random.randint(1, 28), random.randint(1, 12), random.randint(1930, 2030),
              random.choice(range(0, 23)), random.random() < .5) for _ in range(n)]
    bad = 0
    with ThreadPoolExecutor(8) as tp:
        for c, lech in tp.map(mot, cases):
            if lech:
                bad += 1
                print("LỆCH", c, lech[:6])
    print(f"đối chiếu {n} lá số: {n - bad} khớp, {bad} lệch ngoài quy ước đã biết")
    print("ĐỐI CHIẾU OK" if not bad else "ĐỐI CHIẾU HỎNG")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
