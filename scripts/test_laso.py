#!/usr/bin/env python3
"""Kiểm bộ an sao bằng chính ví dụ trong sách. Chạy: python3 test_laso.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from laso import CHI, jd_from_date, lap_la_so, lunar_to_solar, solar_to_lunar  # noqa: E402

fails = 0


def check(name, got, want):
    global fails
    ok = got == want
    fails += not ok
    print(("OK  " if ok else "SAI ") + name + ("" if ok else f": được {got!r}, sách {want!r}"))


def cung_co(r, chi, *sao):
    """Cung `chi` phải có đủ các sao."""
    p = CHI.index(chi)
    have = set(r["cung"][p]["chinh"] + r["cung"][p]["phu"])
    return [s for s in sao if s not in have]


# Lịch: TVCN2 L2310-2340
check("1/10/1981 = 4/9 Tân Dậu, thứ Năm", (solar_to_lunar(1, 10, 1981), (jd_from_date(1, 10, 1981) + 1) % 7), ((4, 9, 1981, 0), 4))
check("15/7/1960 = 22/6 Canh Tý, thứ Sáu", (solar_to_lunar(15, 7, 1960), (jd_from_date(15, 7, 1960) + 1) % 7), ((22, 6, 1960, 0), 5))
check("đổi ngược 4/9 Tân Dậu", lunar_to_solar(4, 9, 1981), (1, 10, 1981))

# Lá số cụ Phạm Văn Toán: Giáp Thìn, 30/2, giờ Sửu, nam (TVCN1 L654-737, L1350-1364)
r = lap_la_so(30, 2, 1964, 1, True, namxem=1964 + 67)
check("Mệnh Dần, Thân Thìn (Thân cư Phúc)", (CHI[r["menh"]], CHI[r["than"]], r["than_cu"]), ("Dần", "Thìn", "Phúc Đức"))
check("Hỏa lục cục", r["cuc"], "Hỏa lục cục")
check("Tử Vi Ngọ, Thiên Phủ Tuất", (CHI[r["sao"]["Tử Vi"]], CHI[r["sao"]["Thiên Phủ"]]), ("Ngọ", "Tuất"))
check("đại hạn 46 ở Ngọ", r["cung"][CHI.index("Ngọ")]["dai_han"], 46)
check("Thê có Bạch Hổ", cung_co(r, "Tý", "Bạch Hổ"), [])
check("Bào có Cự, Đồng", cung_co(r, "Sửu", "Cự Môn", "Thiên Đồng"), [])
check("Tử Tức có Thái Âm, Hồng Loan", cung_co(r, "Hợi", "Thái Âm", "Hồng Loan"), [])
check("Phúc có Thanh Long, Hoa Cái, Thất Sát", cung_co(r, "Thìn", "Thanh Long", "Hoa Cái", "Thất Sát"), [])
check("Di có Phá Quân, Hóa Quyền", cung_co(r, "Thân", "Phá Quân", "Hóa Quyền"), [])
x = r["nam_xem"]
check("68 tuổi: tiểu hạn Tỵ", CHI[x["tieu_han"]], "Tỵ")
check("tiểu hạn Tỵ có Cơ, Tả, Thiên Không", cung_co(r, "Tỵ", "Thiên Cơ", "Tả Phụ", "Thiên Không"), [])
check("đại hạn Thân", CHI[x["dai_han"]], "Thân")
check("tháng tư tới cung Thân", CHI[(x["thang_gieng"] + 3) % 12], "Thân")

# Số Trạng sư: Canh Tuất, 6/8, giờ Sửu, Dương Nam (TVCN1 trang 132, L6707-6778)
r = lap_la_so(6, 8, 1910, 1, True, canh_ky_dong=True)
check("Kim Mệnh, Thủy nhị cục", (r["hanh_menh"], r["cuc"]), ("Kim", "Thủy nhị cục"))
book = {
    "Thân": ["Liêm Trinh", "Thiên Mã", "Điếu Khách", "Lộc Tồn", "Bác Sĩ", "Thiên Khốc", "Thiên Thọ", "Thiên Y", "Thiên Riêu"],
    "Dậu": ["Lực Sĩ", "Văn Xương", "Kình Dương"],
    "Tuất": ["Phá Quân", "Thái Tuế", "Thanh Long", "Bát Tọa", "Hoa Cái", "Địa Không"],
    "Hợi": ["Thiên Đồng", "Thiên Quan", "Hóa Kỵ", "Tả Phụ", "Thiên Không", "Tiểu Hao", "Cô Thần"],
    "Tý": ["Thiên Phủ", "Vũ Khúc", "Tướng Quân", "Phượng Các", "Hóa Quyền", "Tang Môn"],
    "Sửu": ["Thái Âm", "Thái Dương", "Hóa Khoa", "Hóa Lộc", "Ân Quang", "Thiên Quý"],
    "Dần": ["Tham Lang", "Thiên Việt", "Long Trì"],
    "Mão": ["Thiên Cơ", "Cự Môn", "Đào Hoa", "Hữu Bật", "Hỷ Thần"],
    "Thìn": ["Tử Vi", "Thiên Tướng", "Thiên Hình", "Tam Thai", "Quốc Ấn", "Đẩu Quân"],
    "Tỵ": ["Thiên Lương", "Hồng Loan", "Văn Khúc", "Đại Hao", "Long Đức"],
    "Ngọ": ["Thất Sát", "Thiên Phúc", "Bạch Hổ", "Phục Binh", "Thiên Khôi"],
    "Mùi": ["Đà La", "Phúc Đức", "Quả Tú"],
}
for chi, sao in book.items():
    check(f"Trạng sư, cung {chi}", cung_co(r, chi, *sao), [])
check("Tuần Dần-Mão, Triệt Ngọ-Mùi", (r["tuan"], r["triet"]), ((2, 3), (6, 7)))

print("\nTẤT CẢ ĐÚNG" if not fails else f"\n{fails} chỗ sai")
sys.exit(1 if fails else 0)
