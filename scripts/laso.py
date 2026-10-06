#!/usr/bin/env python3
"""Lập lá số Tử Vi theo quy tắc an sao của Tử Vi Chỉ Nam (TVCN1 L566-1360).

  python3 laso.py --ngay 18 --thang 2 --nam 1992 --gio 17 --phut 30 --nu
  python3 laso.py --am --ngay 30 --thang 2 --nam 1964 --gio suu        # nhập âm lịch, giờ theo chi
  python3 laso.py ... --namxem 2026     # thêm đại hạn / tiểu hạn / nguyệt hạn tháng Giêng của năm xem
  python3 laso.py ... --json            # dữ liệu thô (để kiểm tra / so sánh)

Mọi vị trí tính theo chỉ số cung: Tý=0, Sửu=1, Dần=2 ... Hợi=11.
Quy ước có thể khác nhau giữa các trường phái được để thành tuỳ chọn, mặc định theo sách:
  - giờ Tý (23h-24h) tính sang ngày hôm sau (TVCN1 L297); --ty-cung-ngay để tắt
  - tháng nhuận: mùng 1-15 tính tháng chính, 16-30 tính tháng sau (TVCN1 L295); --nhuan-thang-truoc để luôn tính tháng chính
"""
import argparse
import json
import math
import sys

CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
CHI_FOLD = ["ty", "suu", "dan", "mao", "thin", "ty2", "ngo", "mui", "than", "dau", "tuat", "hoi"]
CUNG = ["Mệnh", "Phụ Mẫu", "Phúc Đức", "Điền Trạch", "Quan Lộc", "Nô Bộc",
        "Thiên Di", "Tật Ách", "Tài Bạch", "Tử Tức", "Phu Thê", "Huynh Đệ"]
HANH_CUNG = ["Thủy", "Thổ", "Mộc", "Mộc", "Thổ", "Hỏa", "Hỏa", "Thổ", "Kim", "Kim", "Thổ", "Thủy"]
SINH = {"Kim": "Thủy", "Thủy": "Mộc", "Mộc": "Hỏa", "Hỏa": "Thổ", "Thổ": "Kim"}
KHAC = {"Kim": "Mộc", "Mộc": "Thổ", "Thổ": "Thủy", "Thủy": "Hỏa", "Hỏa": "Kim"}

# Nạp âm 30 cặp lục thập hoa giáp (TVCN1 L29-114)
NAP_AM = [
    ("Hải trung", "Kim"), ("Lô trung", "Hỏa"), ("Đại lâm", "Mộc"), ("Lộ bàng", "Thổ"),
    ("Kiếm phong", "Kim"), ("Sơn đầu", "Hỏa"), ("Giản hạ", "Thủy"), ("Thành đầu", "Thổ"),
    ("Bạch lạp", "Kim"), ("Dương liễu", "Mộc"), ("Tuyền trung", "Thủy"), ("Ốc thượng", "Thổ"),
    ("Tích lịch", "Hỏa"), ("Tùng bách", "Mộc"), ("Trường lưu", "Thủy"), ("Sa trung", "Kim"),
    ("Sơn hạ", "Hỏa"), ("Bình địa", "Mộc"), ("Bích thượng", "Thổ"), ("Kim bạch", "Kim"),
    ("Phú đăng", "Hỏa"), ("Thiên hà", "Thủy"), ("Đại dịch", "Thổ"), ("Thoa xuyến", "Kim"),
    ("Tang đố", "Mộc"), ("Đại khê", "Thủy"), ("Sa trung", "Thổ"), ("Thiên thượng", "Hỏa"),
    ("Thạch lựu", "Mộc"), ("Đại hải", "Thủy"),
]
CUC_SO = {"Thủy": 2, "Mộc": 3, "Kim": 4, "Thổ": 5, "Hỏa": 6}
CUC_TEN = {2: "Thủy nhị cục", 3: "Mộc tam cục", 4: "Kim tứ cục", 5: "Thổ ngũ cục", 6: "Hỏa lục cục"}


# ---------------------------------------------------------------- lịch âm (Hồ Ngọc Đức)
def jd_from_date(dd, mm, yy):
    a = (14 - mm) // 12
    y = yy + 4800 - a
    m = mm + 12 * a - 3
    jd = dd + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    if jd < 2299161:
        jd = dd + (153 * m + 2) // 5 + 365 * y + y // 4 - 32083
    return jd


def jd_to_date(jd):
    if jd > 2299160:
        a = jd + 32044
        b = (4 * a + 3) // 146097
        c = a - (b * 146097) // 4
    else:
        b, c = 0, jd + 32082
    d = (4 * c + 3) // 1461
    e = c - (1461 * d) // 4
    m = (5 * e + 2) // 153
    return e - (153 * m + 2) // 5 + 1, m + 3 - 12 * (m // 10), b * 100 + d - 4800 + m // 10


def _new_moon(k):
    T = k / 1236.85
    T2, T3 = T * T, T * T * T
    dr = math.pi / 180
    jd1 = 2415020.75933 + 29.53058868 * k + 0.0001178 * T2 - 0.000000155 * T3
    jd1 = jd1 + 0.00033 * math.sin((166.56 + 132.87 * T - 0.009173 * T2) * dr)
    M = 359.2242 + 29.10535608 * k - 0.0000333 * T2 - 0.00000347 * T3
    Mpr = 306.0253 + 385.81691806 * k + 0.0107306 * T2 + 0.00001236 * T3
    F = 21.2964 + 390.67050646 * k - 0.0016528 * T2 - 0.00000239 * T3
    C1 = (0.1734 - 0.000393 * T) * math.sin(M * dr) + 0.0021 * math.sin(2 * dr * M)
    C1 = C1 - 0.4068 * math.sin(Mpr * dr) + 0.0161 * math.sin(dr * 2 * Mpr)
    C1 = C1 - 0.0004 * math.sin(dr * 3 * Mpr)
    C1 = C1 + 0.0104 * math.sin(dr * 2 * F) - 0.0051 * math.sin(dr * (M + Mpr))
    C1 = C1 - 0.0074 * math.sin(dr * (M - Mpr)) + 0.0004 * math.sin(dr * (2 * F + M))
    C1 = C1 - 0.0004 * math.sin(dr * (2 * F - M)) - 0.0006 * math.sin(dr * (2 * F + Mpr))
    C1 = C1 + 0.0010 * math.sin(dr * (2 * F - Mpr)) + 0.0005 * math.sin(dr * (2 * Mpr + M))
    if T < -11:
        deltat = 0.001 + 0.000839 * T + 0.0002261 * T2 - 0.00000845 * T3 - 0.000000081 * T * T3
    else:
        deltat = -0.000278 + 0.000265 * T + 0.000262 * T2
    return jd1 + C1 - deltat


def _new_moon_day(k, tz):
    return math.floor(_new_moon(k) + 0.5 + tz / 24)


def _sun_longitude(jdn, tz):
    T = (jdn - 0.5 - tz / 24 - 2451545.0) / 36525
    T2 = T * T
    dr = math.pi / 180
    M = 357.52910 + 35999.05030 * T - 0.0001559 * T2 - 0.00000048 * T * T2
    L0 = 280.46645 + 36000.76983 * T + 0.0003032 * T2
    DL = (1.914600 - 0.004817 * T - 0.000014 * T2) * math.sin(dr * M)
    DL = DL + (0.019993 - 0.000101 * T) * math.sin(dr * 2 * M) + 0.000290 * math.sin(dr * 3 * M)
    L = (L0 + DL) * dr
    L = L - math.pi * 2 * math.floor(L / (math.pi * 2))
    return math.floor(L / math.pi * 6)


def _lunar_month11(yy, tz):
    off = jd_from_date(31, 12, yy) - 2415021
    k = math.floor(off / 29.530588853)
    nm = _new_moon_day(k, tz)
    if _sun_longitude(nm, tz) >= 9:
        nm = _new_moon_day(k - 1, tz)
    return nm


def _leap_month_offset(a11, tz):
    k = math.floor((a11 - 2415021.076998695) / 29.530588853 + 0.5)
    i = 1
    arc = _sun_longitude(_new_moon_day(k + i, tz), tz)
    while True:
        last = arc
        i += 1
        arc = _sun_longitude(_new_moon_day(k + i, tz), tz)
        if not (arc != last and i < 14):
            break
    return i - 1


def solar_to_lunar(dd, mm, yy, tz=7.0):
    """-> (ngày, tháng, năm, nhuận)"""
    day_number = jd_from_date(dd, mm, yy)
    k = math.floor((day_number - 2415021.076998695) / 29.530588853)
    month_start = _new_moon_day(k + 1, tz)
    if month_start > day_number:
        month_start = _new_moon_day(k, tz)
    a11 = _lunar_month11(yy, tz)
    b11 = a11
    if a11 >= month_start:
        lunar_year = yy
        a11 = _lunar_month11(yy - 1, tz)
    else:
        lunar_year = yy + 1
        b11 = _lunar_month11(yy + 1, tz)
    lunar_day = day_number - month_start + 1
    diff = math.floor((month_start - a11) / 29)
    leap = 0
    lunar_month = diff + 11
    if b11 - a11 > 365:
        leap_diff = _leap_month_offset(a11, tz)
        if diff >= leap_diff:
            lunar_month = diff + 10
            if diff == leap_diff:
                leap = 1
    if lunar_month > 12:
        lunar_month -= 12
    if lunar_month >= 11 and diff < 4:
        lunar_year -= 1
    return lunar_day, lunar_month, lunar_year, leap


def lunar_to_solar(ld, lm, ly, leap=0, tz=7.0):
    if lm < 11:
        a11, b11 = _lunar_month11(ly - 1, tz), _lunar_month11(ly, tz)
    else:
        a11, b11 = _lunar_month11(ly, tz), _lunar_month11(ly + 1, tz)
    k = math.floor(0.5 + (a11 - 2415021.076998695) / 29.530588853)
    off = lm - 11
    if off < 0:
        off += 12
    if b11 - a11 > 365:
        leap_off = _leap_month_offset(a11, tz)
        leap_month = leap_off - 2
        if leap_month < 0:
            leap_month += 12
        if leap and lm != leap_month:
            raise ValueError(f"Năm {ly} không có tháng {lm} nhuận (tháng nhuận là {leap_month})")
        if leap or off >= leap_off:
            off += 1
    elif leap:
        raise ValueError(f"Năm âm {ly} không có tháng nhuận")
    return jd_to_date(_new_moon_day(k + off, tz) + ld - 1)


# ---------------------------------------------------------------- tiện ích
def m12(x):
    return x % 12


def can_chi(c, z):
    return f"{CAN[c % 10]} {CHI[z % 12]}"


def nap_am(c, z):
    return NAP_AM[((6 * c - 5 * z) % 60) // 2]


def quan_he(a, b):
    """Quan hệ ngũ hành của a đối với b."""
    if a == b:
        return "bình hoà"
    if SINH[a] == b:
        return f"{a} sinh {b}"
    if SINH[b] == a:
        return f"{b} sinh {a}"
    if KHAC[a] == b:
        return f"{a} khắc {b}"
    return f"{b} khắc {a}"


def gio_chi(hour):
    """Giờ đồng hồ -> chỉ số chi. 23h-0h59 = Tý, 1h-2h59 = Sửu ..."""
    return ((hour + 1) // 2) % 12


def parse_gio_am(s):
    s = s.strip().lower()
    import unicodedata
    f = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").replace("đ", "d")
    names = {"ty": None, "suu": 1, "dan": 2, "mao": 3, "meo": 3, "thin": 4, "ngo": 6, "mui": 7,
             "than": 8, "dau": 9, "tuat": 10, "hoi": 11}
    if s in ("tý", "tí"):
        return 0
    if s in ("tỵ", "tị"):
        return 5
    if f.isdigit():
        n = int(f)
        if 1 <= n <= 12:
            return n - 1
    if f in names and names[f] is not None:
        return names[f]
    raise SystemExit("--gio âm lịch: tên chi có dấu (tý, sửu, dần, mão, thìn, tỵ, ngọ, mùi, thân, dậu, tuất, hợi) hoặc số 1-12")


# ---------------------------------------------------------------- an sao
def an_tu_vi(cuc, day):
    """TVCN1 L432-510: tìm x nhỏ nhất để (ngày + x) chia hết cho cục; thương q.
    Từ Dần đếm thuận q-1 cung; x chẵn thì tiến thêm x cung, x lẻ thì lùi x cung."""
    x = (-day) % cuc
    q = (day + x) // cuc
    pos = 2 + q - 1
    return m12(pos + x if x % 2 == 0 else pos - x)


def lap_la_so(ld, lm, ly, h, nam_gioi, namxem=None, canh_ky_dong=False, hoa_linh_cung_chieu=False):
    yc, yz = (ly + 6) % 10, (ly + 8) % 12
    duong = yc % 2 == 0
    thuan = duong == nam_gioi  # dương nam / âm nữ đi thuận (TVCN1 L619, L1335)
    d = 1 if thuan else -1

    menh = m12(2 + (lm - 1) - h)  # TVCN1 L568
    than = m12(2 + (lm - 1) + h)  # TVCN1 L603
    dan_can = (yc * 2 + 2) % 10   # Ngũ hổ độn: can của cung Dần
    can_cung = [(dan_can + m12(p - 2)) % 10 for p in range(12)]
    cung_chuc = {m12(menh + i): CUNG[i] for i in range(12)}  # 12 cung tính thuận (TVCN1 L596)

    ban_menh = nap_am(yc, yz)
    menh_napam = nap_am(can_cung[menh], menh)
    cuc = CUC_SO[menh_napam[1]]

    S = {p: [] for p in range(12)}

    def put(name, pos):
        S[m12(pos)].append(name)

    # Chính tinh (TVCN1 L607-609)
    tv = an_tu_vi(cuc, ld)
    tp = m12(4 - tv)
    chinh = {
        "Tử Vi": tv, "Thiên Cơ": tv - 1, "Thái Dương": tv - 3, "Vũ Khúc": tv - 4,
        "Thiên Đồng": tv - 5, "Liêm Trinh": tv + 4,
        "Thiên Phủ": tp, "Thái Âm": tp + 1, "Tham Lang": tp + 2, "Cự Môn": tp + 3,
        "Thiên Tướng": tp + 4, "Thiên Lương": tp + 5, "Thất Sát": tp + 6, "Phá Quân": tp + 10,
    }
    chinh = {k: m12(v) for k, v in chinh.items()}

    pos = {}  # tên sao -> cung, dùng cho Tứ Hóa và kiểm tra

    def star(name, p):
        p = m12(p)
        pos[name] = p
        put(name, p)

    for k, v in chinh.items():
        star(k, v)

    # Tràng sinh (TVCN1 L611-619)
    ts_start = {"Thủy": 8, "Thổ": 8, "Hỏa": 2, "Mộc": 11, "Kim": 5}[menh_napam[1]]
    TS = ["Tràng Sinh", "Mộc Dục", "Quan Đới", "Lâm Quan", "Đế Vượng", "Suy", "Bệnh", "Tử",
          "Mộ", "Tuyệt", "Thai", "Dưỡng"]
    trang_sinh = {m12(ts_start + d * i): TS[i] for i in range(12)}

    # Thái Tuế, luôn thuận (TVCN1 L741); Thiên Không ở cung sau Thái Tuế (L745)
    TT = ["Thái Tuế", "Thiếu Dương", "Tang Môn", "Thiếu Âm", "Quan Phù", "Tử Phù", "Tuế Phá",
          "Long Đức", "Bạch Hổ", "Phúc Đức", "Điếu Khách", "Trực Phù"]
    for i, n in enumerate(TT):
        star(n, yz + i)
    star("Thiên Không", yz + 1)

    # Lộc Tồn, Kình, Đà, vòng Bác Sĩ (L749-772)
    loc = [2, 3, 5, 6, 5, 6, 8, 9, 11, 0][yc]
    star("Lộc Tồn", loc)
    star("Kình Dương", loc + 1)
    star("Đà La", loc - 1)
    BS = ["Bác Sĩ", "Lực Sĩ", "Thanh Long", "Tiểu Hao", "Tướng Quân", "Tấu Thư", "Phi Liêm",
          "Hỷ Thần", "Bệnh Phù", "Đại Hao", "Phục Binh", "Quan Phủ"]
    for i, n in enumerate(BS):
        star(n, loc + d * i)

    # Khôi Việt (L776-800)
    khoi, viet = {0: (1, 7), 4: (1, 7), 1: (0, 8), 5: (0, 8), 2: (11, 9), 3: (11, 9),
                  8: (3, 5), 9: (3, 5), 6: (6, 2), 7: (6, 2)}[yc]
    star("Thiên Khôi", khoi)
    star("Thiên Việt", viet)

    # Tả Hữu (tháng), Xương Khúc (giờ), Không Kiếp (giờ) (L804-812)
    star("Tả Phụ", 4 + (lm - 1))
    star("Hữu Bật", 10 - (lm - 1))
    star("Văn Xương", 10 - h)
    star("Văn Khúc", 4 + h)
    star("Địa Không", 11 - h)
    star("Địa Kiếp", 11 + h)

    # Tứ Hóa (L819-837)
    TU_HOA = [
        ("Liêm Trinh", "Phá Quân", "Vũ Khúc", "Thái Dương"),
        ("Thiên Cơ", "Thiên Lương", "Tử Vi", "Thái Âm"),
        ("Thiên Đồng", "Thiên Cơ", "Văn Xương", "Liêm Trinh"),
        ("Thái Âm", "Thiên Đồng", "Thiên Cơ", "Cự Môn"),
        ("Tham Lang", "Thái Âm", "Hữu Bật", "Thiên Cơ"),
        ("Vũ Khúc", "Tham Lang", "Thiên Lương", "Văn Khúc"),
        ("Thái Dương", "Vũ Khúc", "Thiên Đồng", "Thái Âm"),
        ("Cự Môn", "Thái Dương", "Văn Khúc", "Văn Xương"),
        ("Thiên Lương", "Tử Vi", "Tả Phụ", "Vũ Khúc"),
        ("Phá Quân", "Cự Môn", "Thái Âm", "Tham Lang"),
    ]
    if canh_ky_dong:  # thuyết Canh: Nhật Vũ Âm Đồng (lá số mẫu TVCN1 trang 132, TT08 L216)
        TU_HOA[6] = ("Thái Dương", "Vũ Khúc", "Thái Âm", "Thiên Đồng")
    for hoa, sao in zip(("Hóa Lộc", "Hóa Quyền", "Hóa Khoa", "Hóa Kỵ"), TU_HOA[yc]):
        star(hoa, pos[sao])

    # Sao theo tam hợp tuổi (L839-930, L1083-1099)
    nhom = yz % 4  # 0: Thân Tý Thìn, 1: Tỵ Dậu Sửu, 2: Dần Ngọ Tuất, 3: Hợi Mão Mùi
    star("Thiên Mã", {0: 2, 1: 11, 2: 8, 3: 5}[nhom])
    star("Hoa Cái", {0: 4, 1: 1, 2: 10, 3: 7}[nhom])
    star("Đào Hoa", {0: 9, 1: 6, 2: 3, 3: 0}[nhom])
    star("Kiếp Sát", {0: 5, 1: 2, 2: 11, 3: 8}[nhom])
    # Phá Toái (L1111-1123)
    star("Phá Toái", {0: 5, 1: 1, 2: 9}[yz % 3])
    # Cô Thần Quả Tú theo phương (L1044-1058)
    phuong = ((yz + 1) % 12) // 3  # 0: Hợi Tý Sửu, 1: Dần Mão Thìn, 2: Tỵ Ngọ Mùi, 3: Thân Dậu Tuất
    star("Cô Thần", {0: 2, 1: 5, 2: 8, 3: 11}[phuong])
    star("Quả Tú", {0: 10, 1: 1, 2: 4, 3: 7}[phuong])

    # Sao theo chi năm (L900-904, L1011-1013, L1071, L1103)
    star("Long Trì", 4 + yz)
    star("Phượng Các", 10 - yz)
    star("Giải Thần", 10 - yz)
    star("Hồng Loan", 3 - yz)
    star("Thiên Hỷ", 3 - yz + 6)
    star("Thiên Đức", 9 + yz)
    star("Nguyệt Đức", 5 + yz)
    star("Thiên Khốc", 6 - yz)
    star("Thiên Hư", 6 + yz)
    star("Thiên Tài", menh + yz)   # L1019
    star("Thiên Thọ", than + yz)

    # Sao theo tháng (L1032-1036, L1107), Đẩu Quân (L1040)
    star("Thiên Hình", 9 + (lm - 1))
    star("Thiên Riêu", 1 + (lm - 1))
    star("Thiên Y", 1 + (lm - 1))
    star("Thiên Giải", 8 + (lm - 1))
    star("Đẩu Quân", yz - (lm - 1) + h)

    # Sao theo ngày (L892-896): Ân Quang/Thiên Quý, Tam Thai/Bát Tọa
    star("Ân Quang", pos["Văn Xương"] + (ld - 1) - 1)
    star("Thiên Quý", pos["Văn Khúc"] - (ld - 1) + 1)
    star("Tam Thai", pos["Tả Phụ"] + (ld - 1))
    star("Bát Tọa", pos["Hữu Bật"] - (ld - 1))
    # Thai Phụ, Phong Cáo (L1023); Quốc Ấn, Đường Phù (L1028)
    star("Thai Phụ", pos["Văn Khúc"] + 2)
    star("Phong Cáo", pos["Văn Khúc"] - 2)
    star("Quốc Ấn", loc + 8)
    star("Đường Phù", loc - 7)

    # Hỏa Linh (L1062-1067): Dương nam/Âm nữ Hỏa thuận Linh nghịch, ngược lại thì đảo chiều
    hoa0, linh0 = {2: (1, 3), 0: (2, 10), 1: (3, 10), 3: (9, 10)}[nhom]
    star("Hỏa Tinh", hoa0 + (h if hoa_linh_cung_chieu else d * h))
    star("Linh Tinh", linh0 + (h if hoa_linh_cung_chieu else -d * h))

    # Thiên Thương ở Nô Bộc, Thiên Sứ ở Tật Ách (L1075-1079)
    star("Thiên Thương", menh + 5)
    star("Thiên Sứ", menh + 7)

    # Thiên Quan, Thiên Phúc quý nhân theo can (L932-1009)
    star("Thiên Quan", [7, 4, 5, 2, 3, 9, 11, 9, 10, 6][yc])
    star("Thiên Phúc", [9, 8, 0, 11, 3, 2, 6, 5, 6, 5][yc])
    # Lưu niên Văn tinh = Lộc Tồn + 3 (L1158-1187, bảng OCR hỏng, xem an-sao.md)
    star("Văn Tinh", loc + 3)
    # Thiên La, Địa Võng cố định
    star("Thiên La", 4)
    star("Địa Võng", 10)

    # Tuần (L1148-1154), Triệt (L1127-1144)
    tuan_start = (yz - yc) % 12
    tuan = (m12(tuan_start - 2), m12(tuan_start - 1))
    triet = {0: (8, 9), 1: (6, 7), 2: (4, 5), 3: (2, 3), 4: (0, 1)}[yc % 5]

    # Đại hạn (L1203, L1325): bắt đầu ở Mệnh = số cục, mỗi cung 10 năm
    dai_han = {m12(menh + d * i): cuc + 10 * i for i in range(12)}
    # Tiểu hạn (L1193-1197): nam thuận, nữ nghịch
    th_start = {2: 4, 0: 10, 1: 7, 3: 1}[nhom]
    th_dir = 1 if nam_gioi else -1
    tieu_han = {m12(th_start + th_dir * i): m12(yz + i) for i in range(12)}

    out = {
        "am_lich": {"ngay": ld, "thang": lm, "nam": ly},
        "nam": can_chi(yc, yz), "gio": CHI[h],
        "am_duong": ("Dương" if duong else "Âm") + (" Nam" if nam_gioi else " Nữ"),
        "chieu": "thuận" if thuan else "nghịch",
        "ban_menh": f"{ban_menh[0]} {ban_menh[1]}", "hanh_menh": ban_menh[1],
        "cuc": CUC_TEN[cuc], "cuc_so": cuc, "hanh_cuc": menh_napam[1],
        "menh": menh, "than": than, "than_cu": cung_chuc[than],
        "tuan": tuan, "triet": triet,
        "cung": [],
        "sao": pos,
    }
    for p in range(12):
        out["cung"].append({
            "chi": CHI[p], "can_chi": can_chi(can_cung[p], p), "chuc": cung_chuc[p],
            "hanh": HANH_CUNG[p],
            "chinh": [s for s in S[p] if s in chinh],
            "phu": [s for s in S[p] if s not in chinh],
            "trang_sinh": trang_sinh[p], "dai_han": dai_han[p], "tieu_han": CHI[tieu_han[p]],
            "tuan": p in tuan, "triet": p in triet,
        })

    out["_raw"] = {"yc": yc, "yz": yz, "nam_gioi": nam_gioi, "duong": duong, "d": d,
                   "can_cung": can_cung, "chinh": chinh, "trang_sinh": trang_sinh,
                   "cung_chuc": cung_chuc, "dai_han": dai_han, "tieu_han": tieu_han, "S": S,
                   "tu_hoa": TU_HOA}
    if namxem:
        tuoi = namxem - ly + 1
        xz = (namxem + 8) % 12
        dh = next(p for p in range(12) if dai_han[p] <= tuoi < dai_han[p] + 10) if tuoi >= cuc else None
        thc = next(p for p in range(12) if tieu_han[p] == xz)
        # Nguyệt hạn tháng Giêng (L1325): từ cung tiểu hạn gọi tháng Giêng, nghịch đến tháng sinh,
        # rồi gọi đó là giờ Tý, thuận đến giờ sinh
        nh1 = m12(thc - (lm - 1) + h)
        xc = (namxem + 6) % 10
        out["nam_xem"] = {
            "nam": namxem, "can_chi": can_chi(xc, xz), "tuoi_am": tuoi,
            "dai_han": dh, "tieu_han": thc, "thang_gieng": nh1,
            "luu": luu_nien(xc, xz, pos, TU_HOA),
        }
    return out


def luu_nien(xc, xz, pos, tu_hoa):
    """Sao lưu của năm xem. Sách không có bảng riêng: an theo ĐÚNG quy tắc sao năm sinh,
    thay can chi năm sinh bằng can chi năm xem (Thái Tuế theo chi, Lộc Kình Đà và Tứ Hóa theo can,
    Mã theo tam hợp chi, Tang Hổ theo vòng Thái Tuế, Khốc Hư theo chi)."""
    loc = [2, 3, 5, 6, 5, 6, 8, 9, 11, 0][xc]
    L = {
        "L.Thái Tuế": xz, "L.Tang Môn": xz + 2, "L.Bạch Hổ": xz + 8, "L.Tuế Phá": xz + 6,
        "L.Lộc Tồn": loc, "L.Kình Dương": loc + 1, "L.Đà La": loc - 1,
        "L.Thiên Mã": {0: 2, 1: 11, 2: 8, 3: 5}[xz % 4],
        "L.Thiên Khốc": 6 - xz, "L.Thiên Hư": 6 + xz,
    }
    for hoa, sao in zip(("L.Hóa Lộc", "L.Hóa Quyền", "L.Hóa Khoa", "L.Hóa Kỵ"), tu_hoa[xc]):
        L[hoa] = pos[sao]
    return {k: m12(v) for k, v in L.items()}


def ap_engine(r, e):
    """Lấy vị trí sao + độ sáng từ engine Bắc phái (scripts/engine.py) đè lên lá số Python.
    Python phải được lập cùng quy ước (Hỏa Linh cùng chiều, Canh Khoa Âm Kỵ Đồng, nhuận = tháng chính).
    Khung (Mệnh, Thân, cục, đại/tiểu hạn) phải khớp; không khớp -> lỗi, không đoán."""
    import engine as E
    R = r["_raw"]
    pe = E.vi_tri(e)
    menh_e = next(p for p, c in e["cung"].items() if c["chuc"].upper().startswith("MỆNH"))
    if menh_e != r["menh"] or pe.get("Tử Vi", (None,))[0] != r["sao"]["Tử Vi"]:
        raise RuntimeError(f"engine lệch khung: Mệnh {CHI[menh_e]} vs {CHI[r['menh']]}")
    lech = {}
    for ten, (p, _) in pe.items():
        if ten in r["sao"] and r["sao"][ten] != p:
            lech[ten] = (r["sao"][ten], p)
        r["sao"][ten] = p
    r["sang"] = {ten: s for ten, (_, s) in pe.items() if s}
    r["lech_quy_uoc"] = lech  # sao Bắc phái an khác sách (Thương Sứ, Khôi Việt, Thiên Quan...)
    S = {p: [] for p in range(12)}
    for ten, p in r["sao"].items():
        S[p].append(ten)
    R["S"] = S
    for p in range(12):
        c, ce = r["cung"][p], e["cung"][p]
        c["chinh"] = [t for t, _ in ce["chinh"]]
        c["phu"] = [t for t in S[p] if t not in R["chinh"] and t not in c["chinh"]]
        c["phi_hoa"] = ce["phi_hoa"]
        c["luu_bp"] = [f"{t}{' (' + s + ')' if s else ''}" for t, s in ce["luu"]]
        if ce["trang_sinh"]:
            c["trang_sinh"] = ce["trang_sinh"]
    return r


def sang(r, ten):
    """'Đà La' -> 'Đà La(hãm)' nếu có độ sáng."""
    s = r.get("sang", {}).get(ten)
    return f"{ten}({s})" if s else ten


def quet_han(r, nam0, so_nam, ly):
    """Quét từng năm: đại hạn, tiểu hạn, sát tinh gốc + lưu chạm vào hạn. Chỉ GẮN CỜ, không phán.
    Cờ theo TVCN1 L1837-1851: trùng phùng đại/tiểu hạn; Thương Sứ; Kình Đà + Thái Tuế; Không Kiếp."""
    R = r["_raw"]
    cc, S, sao = R["cung_chuc"], R["S"], r["sao"]
    out = []
    for y in range(nam0, nam0 + so_nam):
        tuoi = y - ly + 1
        if tuoi < r["cuc_so"]:
            continue
        xc, xz = (y + 6) % 10, (y + 8) % 12
        dh = next(p for p in range(12) if R["dai_han"][p] <= tuoi < R["dai_han"][p] + 10)
        th = next(p for p in range(12) if R["tieu_han"][p] == xz)
        luu = luu_nien(xc, xz, sao, R["tu_hoa"])
        flags = []
        if dh == th:
            flags.append("đại tiểu hạn TRÙNG PHÙNG")
        vung = {th, *chieu(th)["tam_hop"], chieu(th)["xung"]}  # tiểu hạn + tam phương tứ chính

        for s in ("Kình Dương", "Đà La", "Địa Không", "Địa Kiếp", "Hỏa Tinh", "Linh Tinh", "Hóa Kỵ", "Thiên Hình"):
            if sao[s] in vung:
                flags.append(f"{s} {'tại' if sao[s] == th else 'chiếu'}")
        for k in ("L.Kình Dương", "L.Đà La", "L.Hóa Kỵ", "L.Tang Môn", "L.Bạch Hổ", "L.Thái Tuế"):
            # Tang Môn lưu = chi năm + 2 trùng tiểu hạn một cách hệ thống ở một số tuổi -> chỉ cờ khi đè đại hạn
            if luu[k] == dh:
                flags.append(f"{k} ở đại hạn")
            elif luu[k] == th and k != "L.Tang Môn":
                flags.append(f"{k} ở tiểu hạn")
        for s in ("Thiên Thương", "Thiên Sứ"):
            if sao[s] == th and sao[s] == dh:
                flags.append(f"{s}: đại tiểu hạn cùng gặp (TVCN1 L1839)")
            elif sao[s] == th:
                flags.append(f"{s} ở tiểu hạn")
        if luu["L.Thái Tuế"] == th or "Thái Tuế" in S[th]:
            if sao["Kình Dương"] in vung or sao["Đà La"] in vung:
                flags.append("Thái Tuế + Kình/Đà (TVCN1 L1851)")
        cat = [s for s in ("Hóa Lộc", "Hóa Quyền", "Hóa Khoa", "Lộc Tồn", "Tử Vi", "Thiên Phủ", "Thiên Giải",
                           "Giải Thần") if sao[s] in vung]
        cat += [k for k in ("L.Hóa Lộc", "L.Lộc Tồn", "L.Hóa Khoa") if luu[k] in (th, dh)]
        out.append(f"{y} {can_chi(xc, xz):<9} {tuoi:>3}t ĐH {cc[dh]:<10} TH {cc[th]:<10}"
                   f" | hung: {'; '.join(flags) or '-'} | giải/cát: {', '.join(cat) or '-'}")
    return "\n".join(out)



# ---------------------------------------------------------------- khung luận
NAM_DAU = {"Thiên Phủ", "Thiên Cơ", "Thái Dương", "Liêm Trinh", "Thiên Lương", "Thất Sát", "Thiên Tướng"}
BAC_DAU = {"Vũ Khúc", "Thái Âm", "Thiên Đồng", "Tham Lang", "Cự Môn", "Phá Quân"}  # TVCN1 L1415-2196
NHOM_TT = {  # vòng Thái Tuế chia 4 bộ tam hợp (TT04 L338-367, TT07 L322-331)
    0: "Thái Tuế–Quan Phù–Bạch Hổ (chính vị: trách vụ nặng, được đền công; TT04 L338-340)",
    1: "Thiếu Dương–Tử Phù–Phúc Đức (tinh khôn, được tam đức; TT04 L363-367)",
    2: "Tang Môn–Tuế Phá–Điếu Khách (phá hư, phải tranh đấu, vẫn hơn vị trí 'thiếu'; TT07 L322-331)",
    3: "Thiếu Âm–Long Đức–Trực Phù (thật thà, hay thua thiệt; TT04 L363-367)",
}
SAT = {"Kình Dương", "Đà La", "Địa Không", "Địa Kiếp", "Hỏa Tinh", "Linh Tinh", "Thiên Hình", "Hóa Kỵ",
       "Thiên Không", "Kiếp Sát"}
CAT = {"Tả Phụ", "Hữu Bật", "Văn Xương", "Văn Khúc", "Thiên Khôi", "Thiên Việt", "Hóa Lộc", "Hóa Quyền",
       "Hóa Khoa", "Lộc Tồn", "Thiên Mã", "Long Trì", "Phượng Các", "Ân Quang", "Thiên Quý"}


def chieu(p):
    """Tam phương tứ chính + nhị hợp + giáp của cung p."""
    return {"tam_hop": [m12(p + 4), m12(p + 8)], "xung": m12(p + 6),
            "nhi_hop": m12(1 - p), "giap": [m12(p - 1), m12(p + 1)]}


def khung_luan(r):
    """Các dữ kiện cấu trúc phải có trước khi luận (SKILL.md mục Luận). Không phán, chỉ tính."""
    R = r["_raw"]
    yz, cc, S = R["yz"], R["cung_chuc"], R["S"]
    L = []

    def ten(p):
        c = r["cung"][p]
        return f"{c['chuc']}({c['chi']}): {', '.join(sang(r, t) for t in c['chinh']) or 'VCĐ'}"

    m = r["menh"]
    tuoi_duong = R["duong"]
    cung_duong = m % 2 == 0
    L.append("== KHUNG LUẬN (dữ kiện tính sẵn, chưa phải lời phán) ==")
    L.append(f"Âm dương: tuổi {'dương' if tuoi_duong else 'âm'}, Mệnh ở cung {'dương' if cung_duong else 'âm'}"
             f" → {'THUẬN lý' if tuoi_duong == cung_duong else 'NGHỊCH lý'} (TT09 L8-10)")
    vt = (m - yz) % 4
    L.append(f"Mệnh trong vòng Thái Tuế: sao {next(s for s in S[m] if s in ('Thái Tuế','Thiếu Dương','Tang Môn','Thiếu Âm','Quan Phù','Tử Phù','Tuế Phá','Long Đức','Bạch Hổ','Phúc Đức','Điếu Khách','Trực Phù'))}"
             f" → bộ {NHOM_TT[vt]}")
    L.append(f"Tràng Sinh: Mệnh ở {R['trang_sinh'][m]}, Thân ở {R['trang_sinh'][r['than']]}")
    hoa = {k: r["sao"][k] for k in ("Hóa Lộc", "Hóa Quyền", "Hóa Khoa", "Hóa Kỵ")}
    L.append("Tứ Hóa: " + "; ".join(f"{k} → {cc[v]}({CHI[v]})" for k, v in hoa.items()))
    L.append("")
    for i in range(12):
        p = m12(m + i)
        c, ch = r["cung"][p], chieu(p)
        hl = quan_he(c["hanh"], r["hanh_menh"])
        sat = [s for s in S[p] if s in SAT]
        cat = [s for s in S[p] if s in CAT]
        tt = ("Tuần " if c["tuan"] else "") + ("Triệt" if c["triet"] else "")
        L.append(f"[{c['chuc']} · {c['chi']} · {c['hanh']}, {hl} với bản mệnh{' · ' + tt.strip() if tt else ''}]")
        L.append(f"   thủ: {', '.join(sang(r, t) for t in c['chinh']) or 'VÔ CHÍNH DIỆU → mượn xung chiếu ' + ten(ch['xung'])}"
                 f" | cát: {', '.join(sang(r, t) for t in cat) or '-'} | sát: {', '.join(sang(r, t) for t in sat) or '-'}")
        L.append(f"   tam hợp: {ten(ch['tam_hop'][0])} + {ten(ch['tam_hop'][1])} | xung: {ten(ch['xung'])}"
                 f" | nhị hợp: {ten(ch['nhi_hop'])} | giáp: {ten(ch['giap'][0])} & {ten(ch['giap'][1])}")
    L.append("")
    L.append("Đại hạn (tuổi âm · cung · chính tinh · Nam/Bắc đẩu; TVCN1 L1839: "
             f"{'Dương nam/Âm nữ hợp Nam đẩu' if R['d'] == 1 else 'Âm nam/Dương nữ hợp Bắc đẩu'}):")
    for i in range(12):
        p = m12(m + R["d"] * i)
        c = r["cung"][p]
        nd = [s for s in c["chinh"] if s in NAM_DAU]
        bd = [s for s in c["chinh"] if s in BAC_DAU]
        tag = (f" Nam đẩu: {', '.join(nd)}" if nd else "") + (f" Bắc đẩu: {', '.join(bd)}" if bd else "")
        L.append(f"   {c['dai_han']:>3}-{c['dai_han'] + 9:<3} {c['chuc']:<10} {c['chi']:<4} "
                 f"{', '.join(c['chinh']) or 'VCĐ'}{' ·' + tag if tag else ''}"
                 f"{' ·Tuần' if c['tuan'] else ''}{' ·Triệt' if c['triet'] else ''}")
    if "nam_xem" in r:
        x = r["nam_xem"]
        L.append("")
        L.append(f"Sao lưu năm {x['nam']} {x['can_chi']} (an theo quy tắc sao năm sinh với can chi năm xem;"
                 " sách không có bảng riêng):")
        by = {}
        for k, v in x["luu"].items():
            by.setdefault(v, []).append(k)
        for p in sorted(by, key=lambda q: (q - m) % 12):
            mark = (" ← ĐẠI HẠN" if p == x["dai_han"] else "") + (" ← TIỂU HẠN" if p == x["tieu_han"] else "")
            L.append(f"   {cc[p]:<10} {CHI[p]:<4} {', '.join(by[p])}{mark}")
        th = x["tieu_han"]
        ch = chieu(th)
        L.append(f"   Tiểu hạn {cc[th]}({CHI[th]}) chiếu: tam hợp {ten(ch['tam_hop'][0])} + {ten(ch['tam_hop'][1])}"
                 f" | xung {ten(ch['xung'])}")
        # Nguyệt hạn: tháng Giêng ở cung tính sẵn, các tháng sau đi thuận (TVCN1 L1325)
        L.append("Nguyệt hạn (TVCN1 L1325 chỉ cho tháng Giêng; các tháng sau đi thuận như giờ/năm): " + "; ".join(
            f"T{i + 1} {cc[m12(x['thang_gieng'] + i)]}({CHI[m12(x['thang_gieng'] + i)]})" for i in range(12)))
    return "\n".join(L)


# ---------------------------------------------------------------- in
def in_la_so(r, meta):
    L = []
    al = r["am_lich"]
    L.append(f"LÁ SỐ TỬ VI · {meta}")
    L.append(f"Âm lịch: ngày {al['ngay']} tháng {al['thang']} năm {r['nam']} ({al['nam']}), giờ {r['gio']}")
    L.append(f"{r['am_duong']} (đi {r['chieu']}) · Bản mệnh: {r['ban_menh']} · Cục: {r['cuc']}"
             f" · {quan_he(r['hanh_cuc'], r['hanh_menh'])} (cục so với mệnh)")
    m, t = r["cung"][r["menh"]], r["cung"][r["than"]]
    L.append(f"Mệnh tại {m['chi']} ({m['hanh']}, {quan_he(m['hanh'], r['hanh_menh'])} so với bản mệnh)"
             f" · Thân tại {t['chi']} = Thân cư {r['than_cu']}")
    L.append(f"Tuần: {CHI[r['tuan'][0]]}-{CHI[r['tuan'][1]]} · Triệt: {CHI[r['triet'][0]]}-{CHI[r['triet'][1]]}")
    if "nam_xem" in r:
        x = r["nam_xem"]
        dh = f"{CHI[x['dai_han']]} ({r['cung'][x['dai_han']]['chuc']})" if x["dai_han"] is not None else "chưa vào đại hạn"
        L.append(f"Năm xem {x['nam']} {x['can_chi']} · {x['tuoi_am']} tuổi âm · đại hạn: {dh} · tiểu hạn: "
                 f"{CHI[x['tieu_han']]} ({r['cung'][x['tieu_han']]['chuc']}) · tháng Giêng tại {CHI[x['thang_gieng']]}")
    L.append("")
    for i in range(12):
        p = m12(r["menh"] + i)
        c = r["cung"][p]
        tag = " [THÂN]" if p == r["than"] else ""
        tt = (" ·Tuần" if c["tuan"] else "") + (" ·Triệt" if c["triet"] else "")
        L.append(f"{c['chuc']:<10} {c['can_chi']:<10} {c['hanh']:<4} ĐH {c['dai_han']:<3} TH {c['tieu_han']:<4}"
                 f" {c['trang_sinh']}{tag}{tt}")
        L.append(f"    Chính: {', '.join(sang(r, t) for t in c['chinh']) or '(vô chính diệu)'}")
        L.append(f"    Phụ:   {', '.join(sang(r, t) for t in c['phu'])}")
        if c.get("phi_hoa"):
            L.append(f"    Phi hóa: {' | '.join(c['phi_hoa'])}")
        if c.get("luu_bp"):
            L.append(f"    Lưu (Bắc phái): {', '.join(c['luu_bp'])}")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ngay", type=int, required=True)
    ap.add_argument("--thang", type=int, required=True)
    ap.add_argument("--nam", type=int, required=True)
    ap.add_argument("--gio", required=True, help="dương lịch: giờ 0-23; âm lịch (--am): tên chi hoặc 1-12")
    ap.add_argument("--phut", type=int, default=0)
    ap.add_argument("--nu", action="store_true", help="nữ (mặc định nam)")
    ap.add_argument("--am", action="store_true", help="ngày nhập là âm lịch")
    ap.add_argument("--nhuan", action="store_true", help="tháng âm nhập là tháng nhuận")
    ap.add_argument("--namxem", type=int)
    ap.add_argument("--tz", type=float, default=7.0, help="múi giờ khi đổi lịch (mặc định +7)")
    ap.add_argument("--ty-cung-ngay", action="store_true", help="giờ Tý muộn (23h) vẫn tính ngày hiện tại")
    ap.add_argument("--nhuan-thang-truoc", action="store_true", help="tháng nhuận luôn tính là tháng chính")
    ap.add_argument("--canh-ky-dong", action="store_true",
                    help="tuổi Canh: Khoa Thái Âm, Kỵ Thiên Đồng (mặc định theo bảng sách: Khoa Đồng, Kỵ Âm)")
    ap.add_argument("--hoa-linh-cung-chieu", action="store_true",
                    help="Hỏa Linh cùng đi thuận (Bắc phái); mặc định theo sách: ngược chiều nhau")
    ap.add_argument("--engine", choices=["auto", "bacphai", "sach"], default="auto",
                    help="bacphai: vị trí + đắc hãm từ engine tuvibacphai (cần node); sach: chỉ Python theo "
                         "Tử Vi Chỉ Nam; auto (mặc định): bacphai nếu chạy được, không thì sach")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--gon", action="store_true", help="chỉ in lá số, bỏ khung luận")
    ap.add_argument("--quet", type=int, metavar="N",
                    help="quét hạn N năm từ --namxem (hoặc từ năm sinh), gắn cờ hung/cát từng năm")
    a = ap.parse_args()

    notes = []
    use_bp = False
    if a.engine != "sach":
        import engine as E
        ok, why = E.san_sang()
        if ok:
            use_bp = True
            # Bắc phái: Hỏa Linh cùng chiều, Canh Khoa Âm Kỵ Đồng, tháng nhuận tính tháng chính
            a.hoa_linh_cung_chieu = a.canh_ky_dong = a.nhuan_thang_truoc = True
        elif a.engine == "bacphai":
            sys.exit(f"Không chạy được engine Bắc phái: {why}")
        else:
            notes.append(f"KHÔNG có đắc hãm: engine Bắc phái không chạy được ({why}); dùng Python theo sách")
    if a.am:
        h = parse_gio_am(a.gio)
        ld, lm, ly, leap = a.ngay, a.thang, a.nam, int(a.nhuan)
        sd = lunar_to_solar(ld, lm, ly, leap, a.tz)
        hour = 2 * h  # giờ giữa canh giờ, để gọi engine
        meta = f"âm lịch nhập {ld}/{lm}{' nhuận' if leap else ''}/{ly}, dương lịch {sd[0]}/{sd[1]}/{sd[2]}"
    else:
        hour = int(a.gio)
        h = gio_chi(hour)
        dd, mm, yy = a.ngay, a.thang, a.nam
        if hour == 23 and not a.ty_cung_ngay:
            dd, mm, yy = jd_to_date(jd_from_date(dd, mm, yy) + 1)
            notes.append("sinh sau 23h: giờ Tý tính sang ngày hôm sau (TVCN1 L297)")
        ld, lm, ly, leap = solar_to_lunar(dd, mm, yy, a.tz)
        sd = (dd, mm, yy)
        meta = f"dương lịch {a.ngay}/{a.thang}/{a.nam} {hour:02d}:{a.phut:02d}"
    if leap:
        if a.nhuan_thang_truoc or ld <= 15:
            notes.append(f"tháng {lm} nhuận, tính như tháng {lm}")
        else:
            notes.append(f"tháng {lm} nhuận ngày {ld} > 15: tính sang tháng {lm % 12 + 1} (TVCN1 L295)")
            lm = lm % 12 + 1
    meta += " · " + ("nữ" if a.nu else "nam")

    r = lap_la_so(ld, lm, ly, h, not a.nu, a.namxem, a.canh_ky_dong, a.hoa_linh_cung_chieu)
    if use_bp:
        e = E.chay(sd[0], sd[1], sd[2], 0 if hour == 23 else hour, a.phut, a.nu, namxem=a.namxem)
        ap_engine(r, e)
        notes.append("engine Bắc phái (tuvibacphai): vị trí sao + đắc hãm (miếu/vượng/đắc/bình/hãm), phi hóa,"
                     " sao lưu Bắc phái; khung luận + sao lưu L.* + quét hạn do Python tính và đã đối chiếu khung")
        if r["lech_quy_uoc"]:
            notes.append("sao Bắc phái an khác sách (quy ước trường phái, xem an-sao.md §7): " + "; ".join(
                f"{t} sách {CHI[a_]} → BP {CHI[b_]}" for t, (a_, b_) in r["lech_quy_uoc"].items()))
    elif a.canh_ky_dong:
        notes.append("Tứ Hóa tuổi Canh theo thuyết Khoa Âm / Kỵ Đồng")
    if a.hoa_linh_cung_chieu and not use_bp:
        notes.append("Hỏa Linh an cùng chiều thuận (Bắc phái)")
    r["ghi_chu"] = notes
    if a.json:
        r.pop("_raw")
        print(json.dumps(r, ensure_ascii=False, indent=1))
        return
    print(in_la_so(r, meta))
    for n in notes:
        print("Ghi chú:", n)
    if not a.gon:
        print()
        print(khung_luan(r))
        import khamthien
        print()
        print(khamthien.phan_tich(r))
    if a.quet:
        print()
        print(f"== QUÉT HẠN {a.quet} NĂM (cờ dữ kiện; hung = sát tinh tại/chiếu tiểu hạn, sao lưu đè đại/tiểu hạn) ==")
        print(quet_han(r, a.namxem or ly, a.quet, ly))


if __name__ == "__main__":
    main()
