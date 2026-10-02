# Cách lập lá số Tử Vi (an sao)

Cài đặt: `scripts/laso.py`. Kiểm: `scripts/test_laso.py` (30 phép thử lấy từ ví dụ trong sách, đều đạt).
Nguồn chính: TVCN1 L25-1366 ("Cách lấy số Tử Vi"). Ký hiệu cung: Tý=0 … Hợi=11; `m` tháng âm (1-12),
`h` chỉ số giờ (Tý=0), `d` ngày âm, `yc`/`yz` can/chi năm. "Thuận" = Dương nam, Âm nữ.

## 1. Lịch và đầu vào

| Bước | Quy tắc | Nguồn |
|---|---|---|
| Dương → âm | Thuật toán Hồ Ngọc Đức, múi giờ +7. Khớp 2 ví dụ đổi lịch của sách (1/10/1981, 15/7/1960) | TVCN2 L2310-2340 |
| Năm | Theo năm âm (qua Tết), không theo Lập Xuân | — |
| Giờ Tý | 23h-0h59. Sinh 23h tính sang ngày hôm sau | TVCN1 L297 |
| Tháng nhuận | Mùng 1-15 tính tháng chính, 16-30 tính tháng sau | TVCN1 L295 |

## 2. Khung lá số

| Mục | Quy tắc | Nguồn |
|---|---|---|
| Mệnh | Dần + (m-1) - h | L568 |
| Thân | Dần + (m-1) + h | L603 |
| 12 cung | Từ Mệnh đi thuận: Mệnh, Phụ, Phúc, Điền, Quan, Nô, Di, Tật, Tài, Tử, Phối, Bào | L596 |
| Can cung | Ngũ hổ độn: can của Dần = (2·yc+2) mod 10; Tý, Sửu mang can như Dần, Mão | — |
| Cục | Nạp âm can chi cung Mệnh. Thủy 2, Mộc 3, Kim 4, Thổ 5, Hỏa 6 (đã đối chiếu bảng L297-432) | L297 |
| Đại hạn | Bắt đầu ở Mệnh = số cục, mỗi cung 10 năm, thuận/nghịch theo âm dương | L1203, L1325 |
| Tiểu hạn | Dần Ngọ Tuất từ Thìn, Thân Tý Thìn từ Tuất, Tỵ Dậu Sửu từ Mùi, Hợi Mão Mùi từ Sửu; nam thuận, nữ nghịch | L1193-1197 |
| Nguyệt hạn | Từ cung tiểu hạn gọi tháng Giêng, nghịch đến tháng sinh, rồi gọi giờ Tý, thuận đến giờ sinh | L1325 |

## 3. Chính tinh

- **Tử Vi:** tìm x nhỏ nhất để (d+x) chia hết cho cục; q = (d+x)/cục. Từ Dần tiến q-1 cung. x chẵn thì tiến thêm x, x lẻ thì lùi x. Đã đối chiếu các mốc còn đọc được của bảng L432-510.
- **Nhóm Tử Vi (đi nghịch):** Cơ -1, Nhật -3, Vũ -4, Đồng -5, Liêm +4 (L607).
- **Thiên Phủ** = (4 - Tử Vi) mod 12, đối xứng qua trục Dần-Thân (L609, L623).
- **Nhóm Thiên Phủ (đi thuận):** Âm +1, Tham +2, Cự +3, Tướng +4, Lương +5, Sát +6, Phá +10 (L609).

## 4. Các vòng sao

- **Tràng Sinh:** khởi theo hành cục. Thủy và Thổ ở Thân, Hỏa ở Dần, Mộc ở Hợi, Kim ở Tỵ. Đi thuận/nghịch theo âm dương (L611-619).
- **Thái Tuế:** khởi ở chi năm, luôn đi thuận: Thái Tuế, Thiếu Dương, Tang Môn, Thiếu Âm, Quan Phù, Tử Phù, Tuế Phá, Long Đức, Bạch Hổ, Phúc Đức, Điếu Khách, Trực Phù. Thiên Không cùng cung Thiếu Dương (L741-745).
- **Lộc Tồn:** Giáp Dần, Ất Mão, Bính và Mậu Tỵ, Đinh và Kỷ Ngọ, Canh Thân, Tân Dậu, Nhâm Hợi, Quý Tý. Kình = Lộc +1, Đà = Lộc -1. Vòng Bác Sĩ khởi tại Lộc Tồn, đi thuận/nghịch theo âm dương (L749-772).

## 5. Phụ tinh

| Sao | Quy tắc | Nguồn |
|---|---|---|
| Khôi / Việt | Giáp Mậu: Sửu/Mùi · Ất Kỷ: Tý/Thân · Bính Đinh: Hợi/Dậu · Canh Tân: Ngọ/Dần · Nhâm Quý: Mão/Tỵ | L776; TT08 L237-245 |
| Tả / Hữu | Thìn + (m-1) / Tuất - (m-1) | L804 |
| Xương / Khúc | Tuất - h / Thìn + h | L808 |
| Địa Không / Địa Kiếp | Hợi - h / Hợi + h | L812 |
| Tứ Hóa | Giáp: Liêm Phá Vũ Dương · Ất: Cơ Lương Tử Âm · Bính: Đồng Cơ Xương Liêm · Đinh: Âm Đồng Cơ Cự · Mậu: Tham Âm Hữu Cơ · Kỷ: Vũ Tham Lương Khúc · Canh: Dương Vũ Đồng Âm · Tân: Cự Dương Khúc Xương · Nhâm: Lương Tử Tả Vũ · Quý: Phá Cự Âm Tham (theo thứ tự Lộc Quyền Khoa Kỵ) | L819-837 |
| Mã / Cái / Đào / Kiếp Sát | Tam hợp tuổi Thân Tý Thìn: Dần / Thìn / Dậu / Tỵ · Dần Ngọ Tuất: Thân / Tuất / Mão / Hợi · Tỵ Dậu Sửu: Hợi / Sửu / Ngọ / Dần · Hợi Mão Mùi: Tỵ / Mùi / Tý / Thân | L839-930, L1083 |
| Cô Thần / Quả Tú | Hợi Tý Sửu: Dần/Tuất · Dần Mão Thìn: Tỵ/Sửu · Tỵ Ngọ Mùi: Thân/Thìn · Thân Dậu Tuất: Hợi/Mùi | L1044 |
| Phá Toái | Tý Ngọ Mão Dậu: Tỵ · Dần Thân Tỵ Hợi: Dậu · Thìn Tuất Sửu Mùi: Sửu | L1111 |
| Long Trì / Phượng Các (= Giải Thần) | Thìn + yz / Tuất - yz | L900, L1103 |
| Hồng Loan / Thiên Hỷ | Mão - yz / đối cung | L904 |
| Thiên Đức / Nguyệt Đức | Dậu + yz / Tỵ + yz (sách in nhầm cả hai là "Nguyệt Đức") | L1013 |
| Khốc / Hư | Ngọ - yz / Ngọ + yz | L1071 |
| Thiên Tài / Thiên Thọ | Mệnh + yz / Thân + yz | L1019 |
| Hình / Riêu, Y / Thiên Giải | Dậu + (m-1) / Sửu + (m-1) / Thân + (m-1) | L1032-1036, L1107 |
| Đẩu Quân | Thái Tuế - (m-1) + h | L1040 |
| Ân Quang / Thiên Quý | Xương + d - 2 / Khúc - d + 2 | L892 |
| Tam Thai / Bát Tọa | Tả + d - 1 / Hữu - d + 1 | L896 |
| Thai Phụ / Phong Cáo | Khúc + 2 / Khúc - 2 | L1023 |
| Quốc Ấn / Đường Phù | Lộc + 8 / Lộc - 7 | L1028 |
| Hỏa / Linh | Gốc theo tam hợp tuổi: Dần Ngọ Tuất Sửu/Mão · Thân Tý Thìn Dần/Tuất · Tỵ Dậu Sửu Mão/Tuất · Hợi Mão Mùi Dậu/Tuất. Dương nam, Âm nữ: Hỏa thuận, Linh nghịch; trường hợp còn lại đảo chiều | L1062-1067 |
| Thiên Thương / Thiên Sứ | Cố định ở Nô / Tật | L1075-1079 |
| Thiên Quan | Giáp Mùi, Ất Thìn, Bính Tỵ, Đinh Dần, Mậu Mão, Kỷ Dậu, Canh Hợi, Tân Dậu, Nhâm Tuất, Quý Ngọ | L932 |
| Thiên Phúc | Giáp Dậu, Ất Thân, Bính Tý, Đinh Hợi, Mậu Mão, Kỷ Dần, Canh Ngọ, Tân Tỵ, Nhâm Ngọ, Quý Tỵ | L975 |
| Lưu niên Văn Tinh | Lộc + 3 | L1158 |
| Thiên La / Địa Võng | Cố định ở Thìn / Tuất | — |
| Tuần | Tuần giáp chứa năm sinh, lấy hai chi trống: (yz - yc) - 2 và (yz - yc) - 1 | L1148 |
| Triệt | Giáp Kỷ: Thân Dậu · Ất Canh: Ngọ Mùi · Bính Tân: Thìn Tỵ · Đinh Nhâm: Dần Mão · Mậu Quý: Tý Sửu | L1127 |

## 6. Chỗ sách mơ hồ hoặc sai, và cách đã xử lý

1. **Thiên Quý, "lùi lại một cung".** Câu chữ đọc được hai nghĩa. Em chọn Khúc - d + 2 vì ba lý do:
   - Mọi cặp sao trong sách đều đối xứng qua trục Sửu-Mùi (vị trí cộng lại ≡ 2): Tả/Hữu, Xương/Khúc, Thai/Tọa. Ân Quang/Thiên Quý cũng phải theo quy luật đó.
   - Code Bắc phái trong `source/` cũng tính như vậy.
   - Lá số trang 132 xác nhận: Quang, Quý ở Sửu.
2. **Bảng Lưu niên Văn Tinh bị OCR hỏng**, có chỗ đọc Tân ra "Tị". Chín can còn lại đều theo đúng quy luật Lộc + 3, và Tý/Tị là lỗi OCR hay gặp. Vì vậy em chọn Tân → Tý.
3. **Bảng Hỏa/Linh** ở L1064-1067 có câu lặp và tự mâu thuẫn, kiểu "Linh nghịch… và Linh thuận". Đoạn duy nhất viết đầy đủ là đoạn đầu (Dần Ngọ Tuất). Em lấy quy tắc của đoạn đó áp dụng cho cả bốn nhóm.
4. **Ngũ hành sao.** Bảng viết tắt ở L1415-1792 ghi Thiên Phủ là Thủy, Văn Khúc là Mộc. Phần giải nghĩa từng sao lại ghi Thiên Phủ là Thổ (L1999) và Văn Khúc là Thủy (L2221). Em theo phần giải nghĩa vì phần này viết đầy đủ và nhất quán.
5. **Lá số mẫu trang 126 (Canh Tuất, 20/5, giờ Thìn) tự mâu thuẫn.**
   - Lộc Tồn, Kình, Đà và Cục đều theo tuổi Canh.
   - Tứ Hóa, Thiên Quan, Thiên Phúc, Tuần, Triệt lại theo tuổi Giáp.
   - Sách ghi "Thổ Mệnh", trong khi Canh Tuất là Kim.

   Đây là lỗi vẽ lá số. Không dùng làm chuẩn.
6. **Tứ Hóa tuổi Canh** có hai thuyết:
   - Bảng sách (L831) và TT08 (L216-226): Khoa ở Đồng, Kỵ ở Âm. Đây là mặc định.
   - Lá số mẫu trang 132: Khoa ở Âm, Kỵ ở Đồng. Dùng tuỳ chọn `--canh-ky-dong`.

   Khi luận lá số tuổi Canh, nói rõ đang dùng thuyết nào.
7. **TT09 L74-107 ("học phái Thiên Lương")** nói an Văn Xương theo tháng, Tả Phù theo giờ. Thực ra đó chỉ là quy tắc cũ tính lại theo vị trí so với cung Mệnh:
   - Xương = Mệnh + (9 - m) = Tuất - h.
   - Tả = Mệnh + (2 + h) = Thìn + (m - 1).

   Vị trí sao không đổi. Bảng Thiên Hình theo Thân cùng trang khớp công thức cũ với giờ Sửu và giờ Mùi. Riêng câu "giờ Tý → Phụ Mẫu, giờ Ngọ → Tật" (L105) bị đảo: công thức cho giờ Tý → Tật, giờ Ngọ → Phụ Mẫu. Chính TT09 ở L122 và L425 cũng viết "sinh giờ Tý (tức là Ách có Thiên Hình)", "giờ Tỵ: Mệnh có Thiên Hình", khớp công thức. Vậy L105 là chỗ sách tự mâu thuẫn.

## 7. Biến thể trường phái

Code an sao của tuvibacphai (Bắc phái, file lasotuvi.js; không đi kèm skill) khác sách ở các điểm sau:

- **Hỏa/Linh:** mặc định cả hai đi thuận. Dùng `--hoa-linh-cung-chieu` để chọn cách này.
- **Thương/Sứ:** đổi chỗ cho người âm nam, dương nữ. Sách giữ cố định, và bài Thương Sứ của TT03 (L386-397) chỉ đúng khi cố định, nên không làm tuỳ chọn.
- **Sao không có trong sách:** Lưu Hà (Giáp Dậu, Ất Tuất, Bính Mùi, Đinh Thân, Mậu Tỵ, Kỷ Ngọ, Canh Mão, Tân Thìn, Nhâm Hợi, Quý Dần), Thiên Trù, Địa Giải, Thiên Nguyệt, Âm Sát…

Khôi Việt kiểu Tàu ("Giáp Mậu Canh ở Sửu Mùi") được TT08 L247 nhắc tới, nhưng sách không theo.

## 8. Chưa có trong `laso.py`

- Miếu, vượng, đắc, hãm của chính tinh: sách không có bảng đầy đủ. Tra theo từng sao: `tra <tên sao> mieu ham`.
- Lưu niên tinh (lưu Thái Tuế, lưu Lộc…), Mệnh chủ, Thân chủ.
