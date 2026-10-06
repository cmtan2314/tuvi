#!/usr/bin/env python3
"""Khung Tứ Hóa theo phái Khâm Thiên (KTTH: Giáo trình Đại Hoa; KTSC: Sơ cấp Chiến Nguyễn).

Tính thẳng từ can 12 cung (ngũ hổ độn) và vị trí 18 sao (14 chính tinh + Tả Hữu Xương Khúc),
không cần engine. Chỉ đưa DỮ KIỆN và GẮN CỜ các cách đã định nghĩa trong sách (kèm dòng nguồn);
việc luận vẫn theo references/luan.md §8.

  lai nhân cung, nguyên thần cung          KTSC L288-297, KTTH L94-124
  tứ hóa năm sinh, nam tinh / nữ tinh       KTTH L198-207, KTSC L252
  phi hóa 12 cung, tự hóa ly tâm/hướng tâm  KTSC L42-65, L150-156
  song tượng, phá tượng                     KTSC L197-217, L1514-1571
  Kỵ tinh kỳ phổ                            KTSC L1573-1669
  đại hạn, lưu niên (cấp dưới xung cấp trên) KTSC L1641, L1686-1690
"""

CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

# Bảng tứ hóa của phái (KTTH L198-207 = KTSC L116-133), thứ tự Lộc Quyền Khoa Kỵ.
# Tuổi Canh: Thái Âm Khoa, Thiên Đồng Kỵ (KTSC L128) — khác bảng Tử Vi Chỉ Nam.
TU_HOA = [
    ("Liêm Trinh", "Phá Quân", "Vũ Khúc", "Thái Dương"),
    ("Thiên Cơ", "Thiên Lương", "Tử Vi", "Thái Âm"),
    ("Thiên Đồng", "Thiên Cơ", "Văn Xương", "Liêm Trinh"),
    ("Thái Âm", "Thiên Đồng", "Thiên Cơ", "Cự Môn"),
    ("Tham Lang", "Thái Âm", "Hữu Bật", "Thiên Cơ"),
    ("Vũ Khúc", "Tham Lang", "Thiên Lương", "Văn Khúc"),
    ("Thái Dương", "Vũ Khúc", "Thái Âm", "Thiên Đồng"),
    ("Cự Môn", "Thái Dương", "Văn Khúc", "Văn Xương"),
    ("Thiên Lương", "Tử Vi", "Tả Phụ", "Vũ Khúc"),
    ("Phá Quân", "Cự Môn", "Thái Âm", "Tham Lang"),
]
HOA = ["Lộc", "Quyền", "Khoa", "Kỵ"]
KY = "ABCD"  # A Lộc, B Quyền, C Khoa, D Kỵ (KTSC L135)

SAO18 = ["Tử Vi", "Thiên Cơ", "Thái Dương", "Vũ Khúc", "Thiên Đồng", "Liêm Trinh",
         "Thiên Phủ", "Thái Âm", "Tham Lang", "Cự Môn", "Thiên Tướng", "Thiên Lương", "Thất Sát", "Phá Quân",
         "Tả Phụ", "Hữu Bật", "Văn Xương", "Văn Khúc"]
NAM_TINH = {"Thiên Cơ", "Thái Dương", "Thiên Đồng", "Thiên Phủ", "Tham Lang", "Thiên Tướng", "Thiên Lương",
            "Thất Sát", "Văn Xương", "Tả Phụ"}
NU_TINH = {"Tử Vi", "Vũ Khúc", "Phá Quân", "Thái Âm", "Cự Môn", "Văn Khúc", "Hữu Bật"}

# Thứ tự cung của Khâm Thiên (đi nghịch): Mệnh 1, Huynh 2 … Phụ 12 (KTSC L330-340)
KT_CUNG = ["Mệnh", "Huynh Đệ", "Phu Thê", "Tử Tức", "Tài Bạch", "Tật Ách", "Thiên Di", "Nô Bộc",
           "Quan Lộc", "Điền Trạch", "Phúc Đức", "Phụ Mẫu"]
NGAN = {"Mệnh": "Mệnh", "Huynh Đệ": "Huynh", "Phu Thê": "Phu", "Tử Tức": "Tử", "Tài Bạch": "Tài",
        "Tật Ách": "Tật", "Thiên Di": "Di", "Nô Bộc": "Nô", "Quan Lộc": "Quan", "Điền Trạch": "Điền",
        "Phúc Đức": "Phúc", "Phụ Mẫu": "Phụ"}
LUC_THAN = {"Mệnh", "Huynh Đệ", "Phu Thê", "Tử Tức", "Nô Bộc", "Phụ Mẫu"}  # KTSC L1586
LOAI_LAI_NHAN = {**{c: "nhân cung" for c in LUC_THAN},  # KTSC L307-313
                 "Tài Bạch": "tài cung", "Phúc Đức": "tài cung", "Điền Trạch": "tài cung",
                 "Quan Lộc": "sự cung", "Tật Ách": "sự cung", "Thiên Di": "sự cung"}
TUYEN = {frozenset(("Mệnh", "Thiên Di")): "vận động tuyến", frozenset(("Huynh Đệ", "Nô Bộc")): "thành tựu tuyến",
         frozenset(("Phu Thê", "Quan Lộc")): "công danh tuyến", frozenset(("Tử Tức", "Điền Trạch")): "biến động tuyến",
         frozenset(("Tài Bạch", "Phúc Đức")): "tài lực tuyến", frozenset(("Tật Ách", "Phụ Mẫu")): "quang minh tuyến"}
TU_MA = {2, 8, 5, 11}   # Dần Thân Tỵ Hợi (sách mã kị, KTSC L1621)
TU_MO = {4, 10, 1, 7}   # Thìn Tuất Sửu Mùi (nhập khố kị, KTSC L1628)


def m12(x):
    return x % 12


def gioi(s):
    return "nam tinh" if s in NAM_TINH else "nữ tinh" if s in NU_TINH else "nam/nữ tinh"  # Liêm Trinh


class Ban:
    """Một bàn 12 cung: vị trí cung (0=Tý) -> tên cung; can từng cung; vị trí sao."""

    def __init__(self, menh, can_cung, sao):
        self.menh = menh
        self.can = can_cung
        self.sao = {s: sao[s] for s in SAO18 if s in sao}
        self.ten = {m12(menh - i): KT_CUNG[i] for i in range(12)}
        self.vi = {v: k for k, v in self.ten.items()}

    def phi(self, p):
        """Phi hóa của cung p: [(hóa, sao, cung nhận)]."""
        return [(HOA[i], s, self.sao[s]) for i, s in enumerate(TU_HOA[self.can[p]]) if s in self.sao]

    def tc(self, p):
        return f"{self.ten[p]} ({CAN[self.can[p]]} {CHI[p]})"


def doi(p):
    return m12(p + 6)


def phan_tich(r, nam_xem=None):
    """r: kết quả laso.lap_la_so (đã áp engine nếu có). Trả về văn bản KHUNG TỨ HÓA."""
    R = r["_raw"]
    yc, yz, nam_gioi = R["yc"], R["yz"], R["nam_gioi"]
    B = Ban(r["menh"], R["can_cung"], r["sao"])
    L = []
    w = L.append
    nh = lambda p: B.ten[p]  # noqa: E731
    ng = lambda p: NGAN[B.ten[p]]  # noqa: E731

    w("== KHUNG TỨ HÓA (phái Khâm Thiên: KTTH, KTSC). Dữ kiện + cờ theo sách, CHƯA phải lời luận ==")
    w("Bảng tứ hóa của phái (KTTH L198-207); tuổi Canh: Thái Âm Khoa, Thiên Đồng Kỵ. Chỉ xét 18 sao.")
    w("Ký hiệu: A Lộc, B Quyền, C Khoa, D Kỵ. Thứ tự cung Khâm Thiên đi nghịch: Mệnh 1, Huynh 2 … Phụ 12.")

    # Lai nhân cung, nguyên thần cung
    cands = [p for p in range(12) if B.can[p] == yc]
    lai = next((p for p in cands if p not in (0, 1)), cands[0])
    bo = [p for p in cands if p != lai]
    w("")
    w(f"Lai nhân cung (cung mang can năm sinh {CAN[yc]}): {B.tc(lai)} — {LOAI_LAI_NHAN[nh(lai)]}"
      + (f"; bỏ {', '.join(B.tc(p) for p in bo)} vì can ở Tý/Sửu không lấy (\"Tý khai thiên, Sửu tịch địa\")"
         if bo else "") + " [KTSC L288-297, KTTH L94-124]")
    w(f"Nguyên thần cung (chi năm sinh {CHI[yz]}): {B.tc(yz)} [KTSC L294-297]")

    # Tứ hóa năm sinh
    w("")
    w("Tứ hóa năm sinh (phát từ lai nhân cung):")
    ns = {}
    for i, s in enumerate(TU_HOA[yc]):
        if s in B.sao:
            p = B.sao[s]
            ns[HOA[i]] = (s, p)
            w(f"  {KY[i]} {HOA[i]:5} {s} ({gioi(s)}) tại {B.tc(p)}")
    if "Lộc" in ns and "Kỵ" in ns:
        (sl, pl), (sk, pk) = ns["Lộc"], ns["Kỵ"]
        g = {gioi(sl), gioi(sk)}
        am_duong = ("cô âm: Lộc–Kỵ toàn nữ tinh, có tượng mà khó thành (KTSC L280-284)" if g == {"nữ tinh"} else
                    "độc dương: Lộc–Kỵ toàn nam tinh (KTSC L1695)" if g == {"nam tinh"} else "có cả âm dương")
        w(f"  Lộc nhân Kỵ quả: {ng(pl)} (Lộc, nhân) → {ng(pk)} (Kỵ, quả); {am_duong} [KTSC L1671-1695]")
    for c in ("Phu Thê", "Điền Trạch"):
        p = B.vi[c]
        ss = [s for s in B.sao if B.sao[s] == p]
        gg = {gioi(s) for s in ss} - {"nam/nữ tinh"}
        tag = ("trống 18 sao" if not ss else "chỉ nữ tinh: cô âm bất trưởng" if gg == {"nữ tinh"} else
               "chỉ nam tinh: độc dương bất sinh" if gg == {"nam tinh"} else "đủ âm dương")
        w(f"  {c}: {', '.join(f'{s} ({gioi(s)})' for s in ss) or '—'} → {tag} [KTSC L1695]")

    # Phi hóa 12 cung
    w("")
    w("Phi hóa 12 cung (can cung → sao hóa → cung nhận). (ly tâm) = tự hóa trong chính cung; "
      "(hướng tâm) = phi vào đối cung [KTSC L42-65]:")
    ly_tam, huong_tam, phi = [], [], {}
    for i in range(12):
        p = B.vi[KT_CUNG[i]]
        items = []
        for hoa, s, q in B.phi(p):
            phi.setdefault(p, []).append((hoa, s, q))
            tag = ""
            if q == p:
                tag = " (ly tâm)"
                ly_tam.append((p, hoa, s))
            elif q == doi(p):
                tag = " (hướng tâm)"
                huong_tam.append((p, hoa, s, q))
            items.append(f"{KY[HOA.index(hoa)]} {s}→{ng(q)}{tag}")
        w(f"  {B.tc(p):22} " + " | ".join(items))

    ns_tai = {}  # cung -> [hóa năm sinh]
    for hoa, (s, p) in ns.items():
        ns_tai.setdefault(p, []).append(hoa)
    tu_hoa_tai = {}
    for p, hoa, s in ly_tam:
        tu_hoa_tai.setdefault(p, []).append(hoa)

    w("")
    w("Tự hóa:")
    for p, hoa, s in ly_tam:
        extra = f"; cung có {', '.join(ns_tai[p])} năm sinh" if p in ns_tai else ""
        w(f"  ly tâm {KY[HOA.index(hoa)]}: {B.tc(p)} tự hóa {hoa} ({s}){extra} — bài xích cung có {hoa} năm sinh "
          f"và đối cung {ng(doi(p))} [KTSC L44-53]")
    for p, hoa, s, q in huong_tam:
        w(f"  hướng tâm {KY[HOA.index(hoa)]}: {B.tc(p)} phi {hoa} ({s}) vào đối cung {ng(q)} — tụ lực về {ng(q)}"
          f" [KTSC L56-65]")
    if not ly_tam and not huong_tam:
        w("  không có")

    # Song tượng / phá tượng (bàn gốc)
    w("")
    w("Song tượng, phá tượng (đơn tượng không cát hung; song tượng mới thành vật) [KTSC L197-217, L1514-1571]:")
    flags = []
    for p in range(12):
        a, t = ns_tai.get(p, []), tu_hoa_tai.get(p, [])
        if len(a) >= 2:
            flags.append(f"{B.tc(p)}: hai hóa năm sinh {'+'.join(a)} cùng cung → song tượng [KTSC L209]")
        for h in a:
            for h2 in t:
                if h == h2:
                    flags.append(f"{B.tc(p)}: {h} năm sinh lại tự hóa {h2} → phá tượng đồng loại cùng cung, mạnh nhất "
                                 f"(lực Kỵ > Lộc > Quyền > Khoa) [KTSC L1522-1531]")
                elif {h, h2} in ({"Lộc", "Kỵ"}, {"Quyền", "Khoa"}):
                    flags.append(f"{B.tc(p)}: {h} năm sinh tự hóa {h2} → phá tượng đồng tổ (Kỵ phá Lộc, Quyền phá Khoa)"
                                 f" [KTSC L1518-1520]")
                else:
                    flags.append(f"{B.tc(p)}: {h} năm sinh + tự hóa {h2} → song tượng [KTSC L205]")
    seen = set()
    for p, hoa, s in ly_tam:
        q = doi(p)
        for h2 in tu_hoa_tai.get(q, []):
            k = frozenset((p, q, hoa))
            if h2 == hoa and k not in seen:
                seen.add(k)
                flags.append(f"{ng(p)}–{ng(q)} ({TUYEN[frozenset((nh(p), nh(q)))]}): cả hai cung tự hóa {hoa} "
                             f"→ phá tượng đối cung [KTSC L1546-1561]")
    for p, hoa, s in ly_tam:
        for h in HOA:
            if h == hoa and h in ns and ns[h][1] != p:
                q = ns[h][1]
                rel = ("đối cung" if q == doi(p) else "tam hợp" if (q - p) % 4 == 0 else
                       "nhất lục cộng tông" if abs(KT_CUNG.index(nh(q)) - KT_CUNG.index(nh(p))) == 5 else "")
                if rel:
                    flags.append(f"{ng(p)} tự hóa {hoa} phá {hoa} năm sinh ở {ng(q)} ({rel}) [KTSC L1546-1571]")
    for f in flags or ["không có"]:
        w("  " + f)

    # Kỵ tinh kỳ phổ (bàn gốc)
    w("")
    w("Kỵ tinh kỳ phổ, bàn gốc [KTSC L1573-1669]:")
    ky_di = {p: q for p, lst in phi.items() for hoa, s, q in lst if hoa == "Kỵ"}
    loc_di = {p: q for p, lst in phi.items() for hoa, s, q in lst if hoa == "Lộc"}
    K = []
    ky_ns = ns.get("Kỵ", (None, None))[1]
    for c in ("Mệnh", "Tài Bạch", "Quan Lộc"):
        p = B.vi[c]
        if ky_di.get(p) == doi(p):
            q = doi(p)
            if ky_ns == q and q not in tu_hoa_tai:
                K.append(f"Nghịch thủy kị: {ng(p)} phi Kỵ vào {ng(q)} có Kỵ năm sinh, {ng(q)} không tự hóa → "
                         f"Kỵ bị chặn rót ngược về; làm được sản xuất, kinh doanh lớn [KTSC L1608-1611]")
            elif ky_ns == q:
                K.append(f"Thủy tiết kị: {ng(p)} phi Kỵ vào {ng(q)} có Kỵ năm sinh nhưng {ng(q)} có tự hóa → "
                         f"phá cách nghịch thủy, hao nhanh [KTSC L1613-1615]")
            else:
                K.append(f"Thủy mệnh kị: {ng(p)} lưu xuất Kỵ vào đối cung {ng(q)} → hợp làm công, dịch vụ, mua bán; "
                         f"không hợp tự lập sản xuất [KTSC L1580, L1608]")
    for p, q in ky_di.items():
        if q == doi(p) and nh(p) not in ("Mệnh", "Tài Bạch", "Quan Lộc"):
            K.append(f"Lưu xuất kị: {ng(p)} phi Kỵ vào đối cung {ng(q)} → ý nghĩa {ng(p)} chảy ra ngoài, khó giữ"
                     f" [KTSC L1577-1580]")
    lt = [p for p in ky_di if nh(p) in LUC_THAN]
    for i, p in enumerate(lt):
        for p2 in lt[i + 1:]:
            if ky_di[p] == p2 and ky_di.get(p2) == p:
                K.append(f"Tuần hoàn kị: {ng(p)} ⇄ {ng(p2)} phi Kỵ cho nhau → có qua có lại, ân oán phân minh"
                         f" [KTSC L1586-1589]")
    for p, q in loc_di.items():
        if q != doi(p) and q != p and ky_di.get(q) == p:
            K.append(f"Thị phi kị: {ng(p)} phi Lộc vào {ng(q)}, {ng(q)} phi Kỵ về {ng(p)} → tốt đi, oán về"
                     f" [KTSC L1597-1602]")
    ps = list(ky_di)
    for i, p in enumerate(ps):
        for p2 in ps[i + 1:]:
            if ky_di[p] == doi(ky_di[p2]) and ky_di[p] != p and ky_di[p2] != p2:
                ten = ("Oán thán kị (Mệnh và Phu)" if {nh(p), nh(p2)} == {"Mệnh", "Phu Thê"} else "Cưu triền kị")
                K.append(f"{ten}: {ng(p)} Kỵ→{ng(ky_di[p])} và {ng(p2)} Kỵ→{ng(ky_di[p2])} xung nhau trên tuyến "
                         f"{ng(ky_di[p])}–{ng(ky_di[p2])} [KTSC L1606]")
    ma = [f"Kỵ năm sinh ở {B.tc(ky_ns)}"] if ky_ns in TU_MA else []
    ma += [f"{B.tc(p)} tự hóa Kỵ" for p, h, s in ly_tam if h == "Kỵ" and p in TU_MA]
    if ma:
        K.append("Sách mã kị: " + "; ".join(ma) + " → bôn ba, gần ít xa nhiều [KTSC L1621-1624]")
    if ky_ns in TU_MO:
        if ky_ns in tu_hoa_tai:
            K.append(f"Tiết khố kị: Kỵ năm sinh ở {B.tc(ky_ns)} (tứ mộ) mà cung có tự hóa → tiền không giữ được"
                     f" [KTSC L1632-1635]")
        else:
            K.append(f"Nhập khố kị: Kỵ năm sinh ở {B.tc(ky_ns)} (tứ mộ), không tự hóa → giữ tài, có ý thiếu nợ"
                     f" [KTSC L1628-1632]")
    pm, pq = B.vi["Mệnh"], B.vi["Quan Lộc"]
    if ky_ns == pm:
        vao = [ng(p) for p, q in ky_di.items() if q == pm and p != pm]
        if vao:
            K.append(f"Mệnh tọa Kỵ năm sinh mà {', '.join(vao)} phi Kỵ nhập Mệnh → cách tuyệt mệnh kị (bàn gốc); "
                     f"nặng nhất khi từ Quan/Điền/Phu [KTSC L1649-1654]")
    if ky_ns == pq:
        vao = [ng(p) for p, q in ky_di.items() if q == pq and nh(p) in ("Thiên Di", "Điền Trạch")]
        if vao:
            K.append(f"Quan tọa Kỵ năm sinh mà {', '.join(vao)} phi Kỵ nhập Quan → hung [KTSC L1662]")
    for c in ("Thiên Di", "Điền Trạch"):
        p = B.vi[c]
        if ky_di.get(p) in (doi(pm), doi(pq)):
            K.append(f"{ng(p)} phi Kỵ xung {'Mệnh' if ky_di[p] == doi(pm) else 'Quan'} (bàn gốc) → "
                     f"điều kiện của tuyệt mệnh kị, xét thêm đại hạn [KTSC L1645-1660]")
    if ky_ns in (lai, yz):
        K.append(f"Kỵ năm sinh ở {'lai nhân' if ky_ns == lai else 'nguyên thần'} cung ({ng(ky_ns)}) → quan hệ "
                 f"thiếu nợ rất lớn [KTSC L1669]")
    if ky_di.get(lai) == doi(yz) or ky_di.get(yz) == doi(lai):
        K.append(f"Lai nhân ({ng(lai)}) và nguyên thần ({ng(yz)}) phi Kỵ xung nhau → giao chiến, dễ tổn hại"
                 f" [KTSC L1669]")
    elif ky_di.get(lai) == yz:
        K.append(f"Lai nhân ({ng(lai)}) phi Kỵ nhập nguyên thần ({ng(yz)}) → hai cung liên lụy cả đời [KTSC L1669]")
    for k in K or ["không có cách nào trong Kỵ tinh kỳ phổ"]:
        w("  " + k)
    w("  (Lưu thủy kị = mọi Kỵ phi sang cung khác không phải đối cung: đọc ở bảng phi hóa [KTSC L1582].)")

    # Đại hạn, lưu niên
    nx = r.get("nam_xem")
    if nx and nx.get("dai_han") is not None:
        dm = nx["dai_han"]
        D = Ban(dm, R["can_cung"], r["sao"])
        w("")
        w(f"Đại hạn hiện tại: đại Mệnh tại {CHI[dm]} (can {CAN[B.can[dm]]}), là bản {nh(dm)}. "
          f"Đại cung = bản cung: " + ", ".join(f"đ.{NGAN[D.ten[p]]}={ng(p)}" for p in
                                               (D.vi[c] for c in KT_CUNG)))
        dky = {}
        for hoa, s, q in D.phi(dm):
            w(f"  Tứ hóa đại hạn {KY[HOA.index(hoa)]} {hoa}: {s} → bản {ng(q)} / đ.{NGAN[D.ten[q]]}")
        for c in KT_CUNG:
            p = D.vi[c]
            for hoa, s, q in D.phi(p):
                if hoa == "Kỵ":
                    dky[c] = q
        DK = []
        if nh(dm) in ("Mệnh", "Tài Bạch", "Quan Lộc") and dky.get("Mệnh") in (B.vi["Phu Thê"], B.vi["Thiên Di"],
                                                                              B.vi["Phúc Đức"]):
            DK.append(f"Phản cung kị (hồi lực): đại hạn ở bản {nh(dm)}, đại Mệnh phi Kỵ vào bản {ng(dky['Mệnh'])} "
                      f"→ xung bản {ng(doi(dky['Mệnh']))}; càng dùng sức càng bị dội [KTSC L1593]")
        for c, q in dky.items():
            if q == pm and ky_ns == pm and c in ("Quan Lộc", "Điền Trạch", "Phu Thê"):
                DK.append(f"Tuyệt mệnh kị: Mệnh tọa Kỵ năm sinh, đ.{NGAN[c]} phi Kỵ nhập bản Mệnh [KTSC L1643, L1654]")
            if q == doi(pm) and c in ("Thiên Di", "Điền Trạch", "Tử Tức", "Mệnh"):
                DK.append(f"đ.{NGAN[c]} phi Kỵ xung bản Mệnh → {'tuyệt mệnh kị' if c in ('Thiên Di', 'Điền Trạch') else 'hạn nặng'}"
                          f" [KTSC L1645, L1660, L1664-1667]")
            if q == doi(pq) and c in ("Thiên Di", "Điền Trạch"):
                DK.append(f"đ.{NGAN[c]} phi Kỵ xung bản Quan → tuyệt mệnh kị, nặng như xung Mệnh [KTSC L1645, L1658]")
            if q == pq and ky_ns == pq and c in ("Thiên Di", "Điền Trạch"):
                DK.append(f"Quan tọa Kỵ năm sinh, đ.{NGAN[c]} phi Kỵ nhập bản Quan → hung [KTSC L1662]")
            if q == doi(B.vi[c]):
                DK.append(f"đ.{NGAN[c]} phi Kỵ xung bản {NGAN[c]} (cấp dưới xung cấp trên) → việc {NGAN[c]} hạn này hung;"
                              f" tìm nguyên nhân ở cung đại hạn phi Lộc tới [KTSC L1686-1690]")
        if dky.get("Tài Bạch") == doi(pm):
            DK.append("đ.Tài phi Kỵ xung bản Mệnh → có lẽ chỉ tổn tài [KTSC L1664]")
        for k in DK or ["không có cờ Kỵ đại hạn nào"]:
            w("  " + k)

        # Lưu niên: lưu Mệnh = cung mang chi năm xem; tứ hóa theo can năm (KTSC L1664)
        xz = (nx["nam"] + 8) % 12
        xc = (nx["nam"] + 6) % 10
        Lb = Ban(xz, R["can_cung"], r["sao"])
        w("")
        w(f"Lưu niên {nx['can_chi']}: lưu Mệnh tại {CHI[xz]} (bản {nh(xz)}, đ.{NGAN[D.ten[xz]]}). "
          f"Tứ hóa lưu niên theo can năm {CAN[xc]}:")
        for i, s in enumerate(TU_HOA[xc]):
            if s in B.sao:
                q = B.sao[s]
                w(f"  {KY[i]} {HOA[i]}: {s} → bản {ng(q)} / đ.{NGAN[D.ten[q]]} / l.{NGAN[Lb.ten[q]]}")
        LK = []
        ly_ky = B.sao.get(TU_HOA[xc][3])
        if ly_ky == doi(pm) or ly_ky == doi(pq):
            LK.append(f"Kỵ lưu niên xung bản {'Mệnh' if ly_ky == doi(pm) else 'Quan'} [KTSC L1647, L1664-1667]")
        if ly_ky == doi(dm):
            LK.append("Kỵ lưu niên xung đại Mệnh (lưu niên xung đại hạn) [KTSC L1641]")
        ldi = Lb.vi["Thiên Di"]
        for hoa, s, q in Lb.phi(ldi):
            if hoa == "Kỵ" and q == doi(dm):
                LK.append(f"Lưu Di ({CHI[ldi]}) phi Kỵ xung đại Mệnh → nguy [KTSC L1662]")
            if hoa == "Kỵ" and q in (doi(pm), doi(pq)):
                LK.append(f"Lưu Di ({CHI[ldi]}) phi Kỵ xung bản {'Mệnh' if q == doi(pm) else 'Quan'} → ứng tai ách"
                          f" [KTSC L1664-1667]")
        for k in LK or ["không có cờ Kỵ lưu niên nào"]:
            w("  " + k)
    return "\n".join(L)
