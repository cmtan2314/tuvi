# Điều phối bài luận: 5 agent + agent chính tổng hợp

Một lá số được luận bởi **5 agent chạy song song**:
- **4 agent khối tam hợp.** Mỗi agent luận trọn một khối 3 cung, cả lớp Tam Hợp lẫn lớp Tứ Hóa, có xét khối xung chiếu.
- **1 agent hạn.** Agent này luận mọi đại hạn, năm xem theo 12 tháng và bảng hạn hung, cũng cả hai lớp.

**Agent chính không tự luận từng cung.** Việc của agent chính là chuẩn bị dữ liệu, giao việc, rồi **tổng hợp**: viết phần I, VII, VIII, gỡ mâu thuẫn giữa các agent, ghép thành bài hoàn chỉnh.

Độ dài: **không giới hạn trên, có mức sàn**. Mỗi phần phải dài hơn mức sàn ở tiêu đề của nó trong luan.md §3 (mức tối đa cũ). Toàn bài trên 10.000 từ.

## 1. Bốn khối tam hợp và bảng phân công

| Agent | Khối (3 cung tam hợp) | Khối xung chiếu phải xét | Viết các phần của luan.md §3 |
|---|---|---|---|
| K1 | **Mệnh – Tài Bạch – Quan Lộc** | Thiên Di – Phúc Đức – Phu Thê | II (Mệnh và Thân: tính cách, ngoại hình, sát tinh ở Mệnh, Tuần Triệt); III.1 sự nghiệp; III.2 tiền bạc (nguồn tiền, giữ tiền, đầu tư) |
| K2 | **Phu Thê – Thiên Di – Phúc Đức** | Quan Lộc – Mệnh – Tài Bạch | III.3 tình duyên, hôn nhân; III.6 Phúc Đức; III.7 Thiên Di (xuất ngoại, quý nhân, đi xa) |
| K3 | **Huynh Đệ – Tật Ách – Điền Trạch** | Nô Bộc – Phụ Mẫu – Tử Tức | III.5 sức khỏe; nhà đất và tài sản tích lũy (phần Điền của III.2); anh chị em (phần Huynh của III.8) |
| K4 | **Tử Tức – Nô Bộc – Phụ Mẫu** | Điền Trạch – Huynh Đệ – Tật Ách | III.4 con cái; cha mẹ, bạn bè, đồng nghiệp, cấp dưới, đối tác (phần còn lại của III.8) |
| H | **Hạn** | cả lá số | IV mọi đại hạn đến khoảng 85 tuổi; V năm đang xem đủ 12 tháng; VI bảng hạn hung |
| Chính | — | — | I tổng quan (kể cả Tứ Hóa tổng quan); VII tổng kết và lời khuyên; VIII ghi chú phương pháp; ghép bài và soát mâu thuẫn |

- Thân cư khối nào thì agent khối đó luận thêm ý nghĩa của Thân. Riêng phần "Thân cư cung nào, hậu vận dồn về đâu" thì K1 luôn viết.
- Mỗi khối được luận **gộp**: ba cung chiếu nhau thành một thế, nên cung nào cũng đọc cùng hai cung kia và cùng khối xung chiếu. Không luận từng cung tách rời.

## 2. Agent chính: chuẩn bị (làm trước khi giao việc)

1. Hỏi cho đủ ngày, tháng, năm, giờ, giới tính, dương hay âm lịch. Giờ sát ranh thì hỏi lại.
2. Tạo thư mục làm việc **trong scratchpad của phiên**, ví dụ `<scratchpad>/luan/<mã>`. Mã nên là ký hiệu không chứa ngày sinh, ví dụ `ls01`.
   - **Không bao giờ ghi ngày giờ sinh hay bài luận của người thật vào thư mục skill hoặc repo git.**
3. Chạy rồi lưu kết quả:
   ```bash
   python3 <skill>/scripts/laso.py <ngày giờ> [--nu] --namxem <năm nay> --quet 35 > <dir>/laso.txt
   ```
   Kiểm dòng `Ghi chú` để chắc là có engine Bắc phái, tức là có đắc hãm. Nếu không có, nói rõ trong bài.
4. Đọc `laso.txt` để nắm khung, rồi giao việc **cùng lúc 5 agent** (một lượt gọi, 5 lệnh Agent song song) theo mẫu ở §4 và §5.

## 3. Agent chính: tổng hợp (sau khi đủ 5 file)

1. **Đọc hết 5 file và 5 bản tóm tắt.**
2. **Soát mâu thuẫn.** Ví dụ: K1 nói tiền tốt ở tuổi 36–45, còn H nói đại hạn đó tiền xấu; hay hai agent đọc cùng một sao hai nghĩa ngược nhau. Với mỗi chỗ:
   - quay lại `laso.txt` và thẻ sách để xác định bên nào đúng;
   - sửa phần sai, hoặc nếu cả hai cùng có lý thì viết một đoạn hòa giải: điều kiện nào thì ứng bên nào;
   - ghi chỗ đã sửa vào phần VIII.
3. **Viết phần I** từ lá số và kết luận của 5 agent. Phần I gồm:
   - thông tin, bản mệnh, cục, âm dương, vòng Thái Tuế;
   - **bản đồ bốn khối tam hợp**: hai trục xung chiếu, khối nào mạnh, khối nào là mắt xích yếu;
   - cách cục chính;
   - Tứ Hóa tổng quan: lai nhân, nguyên thần, Lộc nhân Kỵ quả, các cờ Kỵ lớn;
   - chân dung và đường cong đời.
4. **Viết phần VII:** điểm mạnh, điểm yếu, các mốc tuổi, chiến lược đời. Phần này phải khớp với IV–VI.
5. **Viết phần VIII:** engine và quy ước; hai lớp Tam Hợp và Tứ Hóa; các mâu thuẫn đã gỡ; độ tin từng phần.
6. **Ghép bài** vào `<dir>/bai_luan.md` theo thứ tự: I → K1 → K2 → K3 → K4 → H (IV, V, VI) → VII → VIII. Thống nhất cách gọi sao và cung. Bỏ phần giải nghĩa thuật ngữ bị lặp, chỉ giữ lần giải nghĩa đầu tiên trong bài.
7. Chạy danh sách tự kiểm ở luan.md §6 trên toàn bài, kể cả mức sàn số từ (`wc -w` từng file). Phần nào thiếu thì gửi lại agent đó (SendMessage) để viết thêm, hoặc tự viết bổ sung.
8. **Gửi:** in toàn văn bài trong chat (không tóm tắt) và cho biết đường dẫn file.

## 4. Mẫu prompt cho agent khối tam hợp (K1–K4)

Thay `<…>` rồi gửi. Bốn agent dùng cùng mẫu, chỉ khác khối và phần phải viết.

```
Bạn luận MỘT KHỐI TAM HỢP của một lá số Tử Vi, theo cả hai lớp Tam Hợp và Tứ Hóa (phái Khâm Thiên).
Viết bằng tiếng Việt, cho người không biết Tử Vi, sống ở thời hiện đại.

Skill: <skill> (đọc <skill>/SKILL.md trước).
Lá số + KHUNG LUẬN + KHUNG TỨ HÓA + QUÉT HẠN: <dir>/laso.txt. Mọi vị trí sao, độ sáng, phi hóa phải lấy từ file này, không tự nhẩm.
Khối của bạn: <Kx>: <cung 1> (<can chi>) – <cung 2> (<can chi>) – <cung 3> (<can chi>).
Khối xung chiếu phải xét: <3 cung đối>.
Bạn viết các phần: <danh sách phần theo bảng phân công trong <skill>/references/dieu-phoi.md §1>.

Đọc <skill>/references/luan.md: §1–§2b (cách chuẩn bị, đắc hãm, Tứ Hóa), §3 các phần bạn phụ trách, §4 (dịch sang hiện đại), §5 (quy tắc viết).

Cách làm:
1. Ghi nháp cho từng cung trong khối và khối xung chiếu:
   - Tam Hợp: chính tinh, phụ tinh, độ sáng, sinh khắc với bản mệnh, Tuần Triệt, vòng Thái Tuế, Tràng Sinh, sao giáp, cách cục.
   - Tứ Hóa: hóa năm sinh, tự hóa ly tâm/hướng tâm, cung đó phi Lộc/Quyền/Khoa/Kỵ đi đâu, nhận hóa từ cung nào, các cờ trong KHUNG TỨ HÓA dính tới khối.
2. Tra sách song song bằng <skill>/scripts/tra:
   - chính tinh theo từng cung trong khối; đắc hãm để đối chiếu engine; các cách cục nghi có; sát tinh lớn;
   - mỗi cờ Tứ Hóa dính tới khối (vd `tra -b KTSC tiet kho ky`), hàm nghĩa cung trong KTSC Tiết 7 (vd `tra -b KTSC cung phu the ham nghia`), các mục tương ứng của KTTH (hôn nhân, lục thân, bệnh tật).
   Đọc đúng dòng gốc (Read đường-dẫn:dòng) cho mọi kết luận quan trọng.
3. Luận GỘP cả khối: ba cung chiếu nhau thành một thế; xét khối xung chiếu như mặt đối của thế đó.
   Mỗi nhận định đi đủ chuỗi: dữ kiện → cơ chế → nghĩa đời thường hôm nay → thời điểm (đại hạn/năm kích hoạt) → rủi ro → lời khuyên.
   Viết lớp Tam Hợp trước, lớp Tứ Hóa sau, rồi nói rõ hai lớp cùng chiều hay ngược chiều.
4. Độ dài: KHÔNG giới hạn trên, nhưng có MỨC SÀN: mỗi phần bạn viết phải dài HƠN mức sàn ở tiêu đề của nó
   trong luan.md §3 (II ≥ 1.200 từ, mỗi mục III ≥ 900 từ). Mỗi cung trong khối ≥ 600 từ. Càng chi tiết càng tốt.
   Không gộp ý cho gọn, không bỏ cung nào, không ghi "chưa tra". Đếm bằng `wc -w` trước khi trả lời; thiếu thì viết thêm.
   Dẫn nguồn dạng `TVCN1 L2246`, `KTSC L1630`. Giải nghĩa thuật ngữ ở lần đầu dùng.
5. Thời điểm: nói đại hạn nào (tuổi) kích hoạt khối này. Muốn xem tứ hóa của một đại hạn khác thì chạy
   `python3 <skill>/scripts/laso.py <ngày giờ> [--nu] --namxem <một năm trong hạn đó>` và đọc KHUNG TỨ HÓA.

Ghi bài vào <dir>/<Kx>.md, mở đầu bằng tiêu đề `## Khối <tên khối>`. Không ghi gì vào thư mục skill.
Trả lời cuối (ngắn, để agent chính tổng hợp):
- 5–10 kết luận chính của khối, mỗi ý một dòng, có mốc tuổi nếu có;
- các chỗ còn phân vân hoặc nguồn mâu thuẫn;
- điều gì khối này phụ thuộc vào khối khác (để agent chính đối chiếu).
```

## 5. Mẫu prompt cho agent hạn (H)

```
Bạn luận VẬN HẠN của một lá số Tử Vi, theo cả hai lớp Tam Hợp và Tứ Hóa (phái Khâm Thiên).
Viết bằng tiếng Việt, cho người không biết Tử Vi, sống ở thời hiện đại.

Skill: <skill> (đọc <skill>/SKILL.md trước).
Lá số + KHUNG LUẬN + KHUNG TỨ HÓA + QUÉT HẠN: <dir>/laso.txt. Năm xem: <năm>. Ngày giờ để chạy lại: <tham số laso.py>.
Bạn viết các phần IV (mọi đại hạn đến khoảng 85 tuổi), V (năm đang xem, đủ 12 tháng), VI (bảng hạn hung) của
<skill>/references/luan.md §3. Đọc thêm luan.md §1–§2b, §4, §5.

Cách làm:
1. Với MỖI đại hạn: chạy `python3 <skill>/scripts/laso.py <ngày giờ> [--nu] --namxem <một năm giữa hạn đó>` và đọc
   phần đại hạn trong KHUNG TỨ HÓA (tứ hóa đại hạn, đại Kỵ xung đâu, phản cung kị, tuyệt mệnh kị) cùng KHUNG LUẬN
   (cung hạn, sao, độ sáng, tam hợp chiếu, sao lưu đại vận). Có thể chạy song song nhiều lệnh.
   Mỗi đại hạn viết: lớp Tam Hợp, lớp Tứ Hóa, hai lớp cùng hay ngược chiều, chủ đề 10 năm, mức độ, việc nên làm,
   các năm cao điểm và năm phải phòng. Đại hạn đã qua cũng viết đủ, kèm điểm để người đọc tự kiểm.
2. Năm xem: tiểu hạn, sao lưu, tứ hóa lưu niên và cờ Kỵ lưu niên; từng mặt (việc, tiền, tình, sức khỏe, pháp lý, đi lại);
   đủ 12 tháng, mỗi tháng có cung, sao, việc nên làm, việc nên tránh.
3. Bảng hạn hung: lấy mọi năm có cờ nặng trong QUÉT HẠN (≥ 30 năm), cộng các năm có cờ Kỵ Tứ Hóa nặng
   (chạy `--namxem <năm>` cho từng năm nghi vấn để xem cờ Kỵ lưu niên). Mỗi dòng: năm, tuổi, cờ (cả hai lớp),
   ứng vào việc gì ngày nay, sao giải, mức độ, cách phòng cụ thể.
4. Tra sách cho các cờ và cách quan trọng (tra -b KTSC tuyet menh ky, phan cung ky, …; tra cac han Tam Hợp).
5. Độ dài: KHÔNG giới hạn trên, nhưng có MỨC SÀN: mỗi đại hạn ≥ 450 từ, phần năm xem ≥ 1.800 từ (mỗi tháng ≥ 120 từ),
   bảng hạn hung đủ mọi năm có cờ nặng. Đếm bằng `wc -w` trước khi trả lời; thiếu thì viết thêm. Dẫn nguồn dạng `TVCN1 L1837`, `KTSC L1643`.

Ghi bài vào <dir>/H.md, mở đầu bằng `## IV. Vận hạn trọn đời`. Không ghi gì vào thư mục skill.
Trả lời cuối (ngắn): mức độ từng đại hạn (một dòng mỗi hạn), 5–10 năm hung nhất kèm lý do, các chỗ phân vân.
```
