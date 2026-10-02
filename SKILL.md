---
name: tu-vi
description: Lập và luận lá số Tử Vi Đẩu Số; tra sách Tử Vi (Tử Vi Nghiệm Lý Toàn Thư – Thiên Lương tập 1–9, Tử Vi Chỉ Nam – Song An). Use when the user gives a birth date/time and wants a Tử Vi chart (lá số, an sao, 12 cung, đại hạn, tiểu hạn, năm xem), asks about a sao/cung/cách cục/đắc hãm/vòng Thái Tuế/Tuần Triệt/Tứ Hóa, or wants a claim checked against these books. Not for Tứ Trụ / Bát Tự (use tu-tru).
---

# Tử Vi: lập lá số, tra sách, luận có lý

`<skill>` là thư mục chứa file SKILL.md này (khi skill được nạp, Claude Code ghi nó ở dòng "Base directory for this skill"). Mọi đường dẫn dưới đây đều tính từ `<skill>`. Các script tự tìm dữ liệu theo vị trí của chính chúng, nên chép cả thư mục sang máy khác là chạy được.

Cần có:
- **python3** (bắt buộc);
- **node** cùng `jsdom` cho engine Bắc phái. Engine cho **đắc hãm**, phi hóa và sao lưu đại vận. Cài trên máy mới: `cd <skill>/engine && npm install`. Node lấy theo thứ tự: biến `TUVI_NODE`, file `engine/node`, rồi `node` trong PATH. Không có node thì `laso.py` tự quay về engine Python theo sách, nhưng **không có đắc hãm**.

```bash
python3 <skill>/scripts/laso.py --ngay 18 --thang 2 --nam 1992 --gio 17 --phut 30 [--nu] --namxem 2026 --quet 25   # lập lá số + khung luận + quét hạn
python3 <skill>/scripts/tra kinh duong mieu dia                                                         # tra sách
python3 <skill>/scripts/kiemtra                                                                         # tự kiểm cả skill
```

## 4 luật không được phá

1. **Không an sao và không chấm đắc hãm bằng trí nhớ.** Mọi vị trí và độ sáng của sao phải lấy từ `laso.py`. Hai engine kiểm chéo lẫn nhau: Python đạt 30 phép thử lấy từ lá số mẫu trong sách, và khớp engine Bắc phái trên 200/200 lá số ngẫu nhiên, ngoài các quy ước trường phái đã biết.
2. **Không đọc cả file sách** (sách dài tới 9.800 dòng). Dùng `tra` (khoảng 30ms), rồi `Read` đúng dòng mà nó in ra.
3. **Suy luận trước, trích sách sau.** Kết luận phải đi từ cấu trúc lá số (xem mục Luận). Sách chỉ là bằng chứng.
4. **Sách sai hoặc tự mâu thuẫn thì theo lý, và nói rõ:** chọn gì, vì sao, dẫn cả hai nguồn.

Trả lời bằng tiếng Việt, viết thẳng trong chat. Dẫn nguồn theo dạng `TVCN1 L2246` hoặc `TT03 L342`.

## Quy trình

**A. Người dùng đưa ngày giờ sinh: luận ĐẦY ĐỦ, không tóm tắt**
1. Cần đủ ngày, tháng, năm, giờ, giới tính, và biết là dương hay âm lịch. Thiếu giới tính thì hỏi. Giờ sinh sát ranh canh giờ (ví dụ 12h55) thì lập cả hai lá số, hoặc hỏi lại.
2. Chạy `laso.py ... --namxem <năm nay> --quet 20`. Lệnh in ra lá số, **KHUNG LUẬN** (tam phương tứ chính từng cung, âm dương, vòng Thái Tuế, Tứ Hóa, đại hạn, sao lưu, nguyệt hạn) và **QUÉT HẠN** (cờ hung, cát từng năm).
3. **Đọc `<skill>/references/luan.md` rồi viết đúng khuôn trong đó.** Bài gồm 8 phần: tổng quan và cách cục, tính cách, từng lĩnh vực (nghề, tiền, hôn nhân, con, sức khỏe…), mọi đại hạn, năm xem theo 12 tháng, bảng hạn hung, lời khuyên, ghi chú phương pháp. Thường **6.000–10.000 từ**. Mọi sao đều có độ sáng. Mọi lời sách cổ được **dịch sang hoàn cảnh hiện đại** (luan.md §4). Giải nghĩa thuật ngữ cho người không biết Tử Vi.
4. Trước khi viết phải tra (chạy song song): chính tinh theo 12 cung, đắc hãm theo sách để đối chiếu với engine, các cách cục nghi có, các sát tinh lớn, mục nghề nghiệp. Bài đạt yêu cầu không được có các lỗi sau:
   - chỉ dán nhãn sao ("có Lộc nên có tiền") mà thiếu cơ chế, thời điểm và lời khuyên;
   - có mục "hạn chế: chưa tra…".

**B. Hỏi về sao, cung hoặc cách cục**
1. Chạy `tra <vài từ đặc trưng>`. Có thể chạy song song nhiều lệnh `tra` cho các khía cạnh khác nhau.
2. Thẻ đủ thì trả lời ngay. Kết luận quan trọng thì `Read` câu gốc theo `đường-dẫn:dòng` mà `tra` in ra.
3. Hai sách nói khác nhau thì nêu cả hai, rồi giải thích bên nào có lý hơn.

**C. Hỏi cách an một sao:** đọc `<skill>/references/an-sao.md`. File này có công thức từng sao kèm nguồn, các lỗi của sách và cách đã xử lý.

## laso.py: lập lá số

| Tùy chọn | Ý nghĩa |
|---|---|
| `--ngay --thang --nam --gio [--phut]` | Mặc định là dương lịch, giờ từ 0 đến 23 |
| `--am --gio sửu` | Ngày nhập là âm lịch; giờ ghi tên chi hoặc số 1–12. Tháng nhuận thì thêm `--nhuan` |
| `--nu` | Nữ (mặc định là nam) |
| `--namxem 2026` | Tuổi âm, đại hạn, tiểu hạn và cung tháng Giêng của năm xem |
| `--quet 20` | Quét 20 năm kể từ năm xem: mỗi năm một dòng gồm đại hạn, tiểu hạn, cờ hung (sát tinh tại hoặc chiếu, sao lưu đè lên hạn, Thương Sứ, trùng phùng) và cát giải |
| `--engine auto/bacphai/sach` | `auto` (mặc định): dùng engine Bắc phái nếu chạy được, không thì Python theo sách. `sach`: luôn dùng Python theo Tử Vi Chỉ Nam, không có đắc hãm |
| `--gon` | Chỉ in lá số, bỏ khung luận |
| `--json` | Xuất dữ liệu thô |
| `--ty-cung-ngay` | Sinh lúc 23h vẫn tính là ngày đó. Mặc định tính sang ngày hôm sau (TVCN1 L297) |
| `--nhuan-thang-truoc` | Tháng nhuận luôn tính là tháng chính. Mặc định: ngày 1–15 tính tháng chính, 16–30 tính tháng sau |
| `--canh-ky-dong` | Tuổi Canh: Khoa Âm, Kỵ Đồng. Mặc định là Khoa Đồng, Kỵ Âm |
| `--hoa-linh-cung-chieu` | Hỏa và Linh cùng đi thuận (Bắc phái). Mặc định theo sách: hai sao đi ngược chiều nhau |

Bốn dòng cuối của bảng là các quy ước khác nhau giữa trường phái, và chỉ có tác dụng khi chạy `--engine sach`.

**Engine Bắc phái (mặc định).** Engine chạy code của tuvibacphai trong `engine/`. Python lập lá số song song, so khung (Mệnh, Tử Vi), rồi lấy vị trí và độ sáng từ engine. Quy ước của Bắc phái:
- Hỏa Linh cùng chiều.
- Tuổi Canh: Khoa Âm, Kỵ Đồng.
- Tháng nhuận tính là tháng chính.
- Thương/Sứ đổi chỗ cho âm nam và dương nữ.
- Khôi/Việt chia theo can âm hay dương.
- Thiên Quan khác bảng ở tuổi Tân và Kỷ.

Các sao lệch sách được in ở dòng `Ghi chú: sao Bắc phái an khác sách`. Muốn so với cách an theo sách thì chạy thêm `--engine sach`.

**Độ sáng** xếp theo thứ tự `miếu > vượng > đắc > bình > nhàn > hãm`. Đây là bảng của Bắc phái, nên đôi chỗ lệch sách Việt; ví dụ Thiên Đồng ở Dần engine chấm `nhàn`, còn TVCN1 L2141 khen Đồng Lương ở Dần là "tốt nhất". Khi lệch thì **suy luận theo `luan.md` §2** (ngũ hành sao so với cung, bộ sao, độ rõ của câu sách) rồi nói rõ đã chọn gì.

Kết quả gồm: âm dương, chiều đi, bản mệnh, cục và quan hệ sinh khắc, Mệnh, Thân cư, Tuần, Triệt. Mỗi cung có can chi, hành, đại hạn, tiểu hạn, sao vòng Tràng Sinh, chính tinh và phụ tinh (khoảng 90 sao).

Chạy `--engine sach`, hoặc máy không có node, thì kết quả **không có đắc hãm**. Khi đó phải tra từng sao, ví dụ `tra thai duong mieu ham`, và nói rõ điều này trong bài.

Có hai bộ sao lưu:
- `L.*` trong khung luận do Python an theo đúng quy tắc của sao năm sinh, chỉ thay can chi năm sinh bằng can chi năm xem. Sách không có bảng riêng cho sao lưu, nên khi dùng phải nói rõ điều này.
- Dòng `Lưu (Bắc phái)` là sao lưu của engine: `Đv.` cho đại vận, `L.` cho lưu niên, `N.` cho lưu nguyệt.

## tra: tra sách

Gõ không dấu cũng được, và kết quả chịu được lỗi dấu do OCR. Kết quả có hai phần:
- `=== THẺ`: quy tắc đã tóm tắt và sửa chính tả. Mỗi ý có `[Lnnn]` trỏ về dòng trong sách gốc. Thẻ dài thì chỉ in các ý khớp từ tra.
- `[n] GỐC`: đoạn trích nguyên văn sách, kèm `đường-dẫn:dòng` và trang scan `pNNN`.

| Tùy chọn | Tác dụng |
|---|---|
| `-b TT03` | Chỉ tra trong một sách |
| `-k 10` / `-t 4` | Thêm số trích đoạn gốc (mặc định 5) / số thẻ (mặc định 2) |
| `--goc` / `--the` | Chỉ tra sách gốc / chỉ tra thẻ |
| `-f` | In nguyên văn cả đoạn gốc và cả thẻ dài |
| `'"hoa ky" OR "hoa ki"'` | Dùng cú pháp FTS5 thô |

Mẹo:
- Dùng 2–4 từ đặc trưng, ví dụ `thien hinh dan`. Đừng gõ cả câu hỏi.
- Không thấy kết quả thì bớt từ, hoặc thử cách viết khác: `ky`/`ki`, `ty`/`ti`.
- Nghi OCR sai mà máy có ảnh scan hay PDF gốc thì xem trang `pNNN` tương ứng. Skill không mang theo ảnh hay PDF.

| Mã | Sách | Dùng khi |
|---|---|---|
| TVCN1, TVCN2 | Tử Vi Chỉ Nam (Song An Đỗ Văn Lưu) | Tra cứu chuẩn: ý nghĩa sao theo cung, miếu hãm, cách cục, hạn, nghề nghiệp, phú Lê Quý Đôn (TVCN2 L1656). Chữ khá sạch |
| TT01–TT09 (không có TT06) | Tử Vi Nghiệm Lý Toàn Thư (Thiên Lương) | Nguyên lý: âm dương, vòng Thái Tuế, Tài Thọ, Thương Sứ, nhị hợp, ngoại lệ, lá số người thật. OCR bẩn, trang scan không theo thứ tự bài |
| LICH, LICH2, LICH3 | Bảng lịch vạn niên | Không tra. Đổi lịch bằng `laso.py` |

## Luận: kỷ luật suy luận

Lá số là một hệ có cơ chế: ngũ hành, âm dương, tam hợp, xung chiếu, các vòng sao. **Mọi kết luận phải truy được về cơ chế đó.**

1. **Dựng cấu trúc trước, theo thứ tự:**
   1. Mệnh, Thân và chính tinh của hai cung đó.
   2. **Tam phương tứ chính**: cung xét, hai cung tam hợp, cung xung chiếu; thêm cung nhị hợp (TVCN1 L1298) và hai cung giáp.
   3. Ngũ hành: bản mệnh so với cục, với hành cung Mệnh, với hành từng sao (TVCN1 L1207, L1319).
   4. Âm dương: tuổi âm hay dương so với cung âm hay dương mà Mệnh đóng.
   5. Vị trí của Mệnh trong vòng Thái Tuế (Thái Tuế, Tuế Phá, Thiếu Dương…). Bộ TVNL coi đây là gốc.
   6. Tuần, Triệt, đắc hãm. Sau cùng mới xét đại hạn, tiểu hạn.
2. **Không luận một sao đứng riêng.** Phải xét sao đồng cung, sao chiếu, sao giáp và sao giải. Chính TVCN1 L1366 nhận rằng câu "Kiếp Không lâm Tài" từng sai, vì người xem bỏ qua đại hạn và sao giải.
3. **Phú chỉ là câu vần nói gộp.** Chỉ dẫn câu phú khi nó gọi đúng tên điều đã suy ra. Không lấy câu phú làm kết luận.
4. **Khi sách sai, kiểm lần lượt:**
   1. Nhất quán nội tại: quy tắc có cùng khuôn với các quy tắc anh em không?
   2. Đối chiếu sách khác.
   3. Đối chiếu ví dụ đã giải trong sách.
   4. Đối chiếu cơ chế ngũ hành, âm dương.

   Các trường hợp đã gặp:
   - `references/an-sao.md` §6 ghi 7 trường hợp, ví dụ lá số in sai ở TVCN1 trang 126, câu Thiên Hình bị đảo ở TT09 L105.
   - Bảng viết tắt hành sao trong TVCN1 bị OCR trộn cột, nên tin phần giải thích riêng của từng sao: Thiên Phủ thuộc Thổ (L1999), Văn Khúc thuộc Thủy (L1826), Tuế Phá thuộc Hỏa (L2542).
   - Đắc hãm của Đà La: TVCN1 L2281 chép bảng của Kình, trong đó có cả Tý Ngọ Mão Dậu, nơi Đà không bao giờ đứng được. Engine Bắc phái chấm hãm. TT03 L344-354 lại coi Đà ở Dần Thân Tỵ Hợi hợp Mệnh Kim là đắc cách. Phải cân cả ba nguồn, xem `luan.md` §7.
   - Một câu sách nêu vị trí mà sao **không thể đứng được** theo cách an sao là dấu hiệu chép sai. Đối chiếu bằng `laso.py`.
   - Chỗ in sai đã sửa được đánh dấu ngay trong thẻ. Chỗ chưa chắc ghi `(?)`.
5. **Hai bộ sách, hai lối.** TVCN theo phú cổ. TVNL lý giải bằng âm dương và Thái Tuế, hay nêu ngoại lệ. Khi hai bộ lệch nhau, nêu cả hai rồi để cấu trúc lá số quyết định.
6. **Phụ Mẫu và Huynh Đệ:** TVCN1 tự nhận phần này "sai 7–8 phần" (TVCN1 L5830 trở đi). Không phán chắc ở hai cung này.
7. **Áp dụng vào đời sống hiện đại.** Sách viết cho xã hội cũ, phải dịch theo *bản chất của sao* chứ không dịch từng chữ. Ví dụ: "làm quan" là có vị trí quản lý hoặc vào công chức; "đầy tớ" là cấp dưới, đồng nghiệp; "ruộng" là bất động sản; "chết đường" là tai nạn giao thông. Bảng đối chiếu và bảng nghề theo chính tinh nằm ở `luan.md` §4. Khi diễn giải phải nói rõ đó là suy luận.

## Khi có lỗi

| Triệu chứng | Cách xử lý |
|---|---|
| Không chắc skill còn chạy đúng | Chạy `python3 <skill>/scripts/kiemtra`. Nó in `SKILL OK`, hoặc chỉ ra đúng phần hỏng |
| Index thiếu, hỏng, hoặc cũ hơn sách/thẻ | Không cần làm gì: `tra` tự dựng lại (khoảng 0,4 giây, có báo ra stderr) |
| `tra` báo "Không thấy" | Bớt từ, đổi cách viết, bỏ `-b` |
| `Ghi chú: KHÔNG có đắc hãm` | Engine Bắc phái không chạy được: thiếu node hoặc jsdom. Cài node rồi chạy `npm install` trong `<skill>/engine`, hoặc đặt `TUVI_NODE`. Chạy `kiemtra` để xem lý do |
| `engine lệch khung` | Hai engine cho Mệnh hoặc Tử Vi khác nhau. Không dùng kết quả. Chạy `doichieu.py` và kiểm lại cách đổi lịch |
| Kết quả `laso.py` nghi sai so với sách | Chạy `test_laso.py`. Đối chiếu sao đó trong `an-sao.md`. Kiểm lại xem có đang dùng quy ước trường phái khác không. Nếu sách sai, xử lý theo Luận mục 4 |

## Bảo trì

Skill gồm:
- `scripts/`;
- `engine/`: code Bắc phái và `package.json`. Không đưa `node_modules` và link `node` vào git;
- `references/books/`: sách dạng .md;
- `references/the/`: thẻ;
- `references/an-sao.md`, `references/luan.md`.

File `references/tuvi.db` có thể xóa, vì nó được dựng lại tự động. Chép cả thư mục sang máy khác rồi chạy `npm install` trong `engine/` là dùng được.

- **Sửa sách hoặc thẻ:** không phải làm gì thêm, lần tra sau sẽ tự dựng lại index.
- **Sửa `laso.py` hoặc `engine/`:** chạy `kiemtra`, phải ra `SKILL OK`. Lệnh này gồm cả `doichieu.py`, so hai engine trên nhiều lá số ngẫu nhiên. Phép thử mới thì thêm vào `test_laso.py`, lấy từ lá số mẫu trong sách.
- **Sửa chính tả sách:** giữ nguyên số dòng, vì các thẻ trỏ vào sách bằng `[Lnnn]`. Không tự động "sửa dấu" hàng loạt: bản sửa tự động từng đổi tên sao, ví dụ Tham thành Thân.
- **Làm lại một thẻ:** giữ đúng khuôn. Mỗi mục là `## Tiêu đề · L… · trang …`, mỗi ý có `[Lnnn]`, cuối thẻ có `## Từ khoá`.
