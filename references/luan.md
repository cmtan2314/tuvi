# Khuôn bài luận lá số (bắt buộc)

Người đọc không biết Tử Vi. Một bài luận đạt yêu cầu phải:

- **đủ** mọi phần ở mục 2;
- **sâu**: mỗi nhận định đều có chuỗi lý do;
- **dài**: thường 3.000–6.000 từ cho một lá số đầy đủ;
- **dễ hiểu**: thuật ngữ nào cũng giải nghĩa ngay lần đầu xuất hiện.

Không gửi một bản tóm tắt rồi hỏi "anh muốn xem sâu phần nào". Phải làm đủ ngay từ đầu.

## 1. Chuẩn bị (làm xong mới viết)

1. Chạy `python3 <skill>/scripts/laso.py ... --namxem <năm nay> --quet 15`. Lệnh in ra ba thứ:
   - lá số;
   - **KHUNG LUẬN**: âm dương, vòng Thái Tuế, Tràng Sinh, Tứ Hóa, tam phương tứ chính của từng cung, đại hạn, sao lưu, nguyệt hạn;
   - **QUÉT HẠN**: cờ hung và cát của từng năm.
2. Tra song song (mỗi lệnh khoảng 30ms). Tối thiểu cần tra:
   - mỗi chính tinh ở Mệnh, Thân, Quan, Tài, Phu Thê, Phúc, Tật kèm tên cung, ví dụ `tra cu mon quan loc`, `tra thai duong tai bach`;
   - các **cách cục** nghi có (cụm sao ở tam hợp): `tra thach trung an ngoc`, `tra co nguyet dong luong`, `tra vo chinh dieu`…;
   - các sát tinh lớn đóng ở Mệnh, Thân và các cung hạn sắp tới, ví dụ `tra dia kiep menh`, `tra da la`;
   - đắc hay hãm của từng chính tinh ở vị trí của nó, ví dụ `tra thien co ngo`. `laso.py` chưa có bảng miếu hãm, phải tra.
3. Ghi nháp cho mỗi cung: sao gì, đắc hay hãm, sinh khắc với bản mệnh, tam hợp chiếu gì, có Tuần Triệt không. **Có nháp đủ 12 cung rồi mới viết.**

## 2. Các phần của bài (theo thứ tự này)

### I. Tóm tắt lá số (khoảng 300 từ)
- Ngày giờ âm dương lịch, âm dương nam nữ, chiều đi.
- Bản mệnh và cục, kèm giải nghĩa. Ví dụ: "Bạch Lạp Kim, tức kim trong nến: chất quý nhưng cần lửa luyện. Hỏa lục cục khắc Kim, tức môi trường sống ép mình, phải rèn mới thành."
- Thuận lý hay nghịch lý âm dương, và điều đó nghĩa là gì.
- Vị trí của Mệnh trong vòng Thái Tuế, và ý nghĩa đối với thái độ sống.
- **Cách cục chính**: tên cách, vì sao thành, cái gì phá hoặc giảm cách, có dẫn nguồn.
- Một đoạn "chân dung" 4–6 câu: người này là ai, mạnh ở đâu, yếu ở đâu.

### II. Mệnh và Thân: tính cách, con người (500–800 từ)
- Chính tinh thủ Mệnh. Nếu Mệnh vô chính diệu thì nói mượn sao nào, theo quy tắc nào (TVCN2 L1117-1126), cộng với tam hợp.
- Tính cách cụ thể và hành vi đời thường. Không viết chung chung kiểu "thông minh, hiền". Phải nói thông minh kiểu gì, hiền đến mức nào, nóng hay lạnh, quyết đoán hay do dự, giao tiếp ra sao, khi bị dồn thì phản ứng thế nào.
- Ngoại hình theo sao thủ Mệnh (TVCN1 L2765-2909).
- Thân cư cung nào và nghĩa là gì: hậu vận trọng về đâu.
- Sát tinh ở Mệnh: đắc hay hãm, hợp hay khắc bản mệnh, có được chế không (Tuần Triệt, cát tinh). Kết luận là sát tinh làm hại hay hóa thành lợi.
- Tuần hoặc Triệt ở Mệnh hay Thân: tác động đến tuổi trẻ và thời điểm "mở".

### III. Từng lĩnh vực (mỗi mục 250–500 từ)
Mỗi mục đều theo trình tự: **sao thủ → tam hợp/xung chiếu → sinh khắc, đắc hãm → cách → nghĩa đời thường → thời điểm (đại hạn nào kích hoạt) → lời khuyên**.

1. **Sự nghiệp (Quan Lộc).** Nghề hợp, nêu 3–5 nghề hoặc lĩnh vực **cụ thể** kèm lý do. Hợp làm chủ hay làm thuê, khu vực công hay tư. Mốc thăng tiến theo đại hạn. Rủi ro nghề nghiệp. Kết hợp TVCN1 "nghề nghiệp" (TVCN2 L1298-1652).
2. **Tiền bạc (Tài Bạch + Điền Trạch).** Tiền đến từ đâu: lương, buôn bán, chuyên môn hay may rủi. Giữ được hay không. Giai đoạn kiếm được, giai đoạn hao. Có nên đầu tư, đứng tên, cho vay không. Nhà đất có hay không, lúc nào có.
3. **Tình duyên, hôn nhân (Phu Thê).** Người phối ngẫu: tính cách, ngoại hình, hoàn cảnh. Cưới sớm hay muộn, nêu khoảng tuổi theo đại hạn và tiểu hạn có Hồng Loan, Thiên Hỷ, Đào Hoa. Mâu thuẫn dễ gặp. Nguy cơ đổ vỡ và điều kiện để giữ. Lời khuyên cụ thể.
4. **Con cái (Tử Tức).** Đông hay ít, trai hay gái nếu sách có nói, con có hợp không, lúc nào có con dễ.
5. **Sức khỏe (Tật Ách).** Bộ phận yếu theo sao và ngũ hành (TVCN1 có phần Giải Ách theo từng sao). Tuổi cần phòng. Nguy cơ tai nạn nếu có Kình, Đà, Hình, Hỏa, Linh hoặc Thương Sứ.
6. **Phúc Đức.** Phúc dòng họ, mồ mả, sự che chở. Tuổi thọ, nếu sách có cách tính.
7. **Cha mẹ, anh em, bạn bè, cấp dưới (Phụ Mẫu, Huynh Đệ, Nô Bộc).** Luận đủ, nhưng nói rõ độ tin thấp (TVCN1 tự nhận phần này sai 7–8 phần).
8. **Thiên Di.** Ra ngoài thì gặp gì, có nên đi xa hay xuất ngoại không, quý nhân hay tiểu nhân.

### IV. Vận hạn trọn đời: từng đại hạn 10 năm (mỗi hạn 120–250 từ)
Viết **tất cả** các đại hạn từ hiện tại đến khoảng 85 tuổi. Đại hạn đã qua thì chỉ cần 1–2 câu đối chiếu, để người đọc tự kiểm độ đúng. Mỗi đại hạn cần nêu:
- cung, sao thủ, tam hợp chiếu;
- hành cung so với bản mệnh;
- Nam hay Bắc đẩu so với âm dương của người (TVCN1 L1839);
- Tuần Triệt;
- chủ đề chính của 10 năm: tiền, nghề, gia đình hay sức khỏe;
- đánh giá **mức độ**: tốt / khá / trung bình / xấu / rất xấu, kèm lý do;
- những năm cao điểm và năm cần đề phòng trong hạn đó, lấy từ QUÉT HẠN.

### V. Năm đang xem: chi tiết (600–1.000 từ)
- Đại hạn, tiểu hạn, sao lưu (Thái Tuế, Lộc, Kình, Đà, Tứ Hóa, Mã, Tang, Hổ, Khốc, Hư) đè lên đâu. Nói rõ sao lưu được an theo quy tắc sao năm sinh, sách không có bảng riêng.
- Năm đó tốt hay xấu ở từng mặt: công việc, tiền, tình cảm, sức khỏe, pháp lý.
- **Từng tháng** theo nguyệt hạn: tháng nào thuận, tháng nào phải cẩn thận, vì sao.
- Việc nên làm và việc nên tránh, cụ thể.

### VI. Hạn hung: liệt kê riêng (bắt buộc)
Lập bảng các năm có cờ nặng trong QUÉT HẠN (quét 15–30 năm). Cờ nặng gồm:
- đại hạn và tiểu hạn trùng phùng có sát tinh;
- Kình Đà gặp Thái Tuế;
- Thiên Thương hoặc Thiên Sứ, nhất là khi đại hạn và tiểu hạn cùng gặp;
- Không Kiếp tại hạn;
- lưu Kình hoặc lưu Kỵ đè lên đại hạn.

Mỗi năm trong bảng ghi: cờ gì, ứng vào việc gì (theo sao: Hình là kiện tụng hay dao kéo; Kỵ là thị phi; Kình Đà là tai nạn; Tang Hổ là tang hay ốm…), sao giải nào có mặt, mức độ, cách phòng.

Nói thẳng, không né, nhưng không dọa: luôn kèm sao giải và việc cụ thể có thể làm.

### VII. Tổng kết và lời khuyên (200–400 từ)
3–5 điểm mạnh nên tận dụng, 3–5 điểm yếu phải phòng, và các mốc tuổi quan trọng nhất.

### VIII. Ghi chú phương pháp (ngắn)
- Các quy ước đã dùng.
- Những chỗ sách mâu thuẫn và đã chọn theo hướng nào.
- Độ tin của từng phần.

## 3. Quy tắc viết

- **Chuỗi lý do cho mọi nhận định**, theo dạng *dữ kiện → cơ chế → ý nghĩa*. Ví dụ: "Cự Môn ở Tý có Hóa Lộc (dữ kiện), là cách 'thạch trung ẩn ngọc', tức ngọc trong đá, cần Khoa Lộc và Thái Dương ở Thìn soi sáng (TT04 L199-201) (cơ chế). Ở đây có Hóa Lộc tại chỗ, Thái Dương Hóa Quyền ở Thìn chiếu về, nên cách thành. Nhưng Thái Dương bị Triệt (cơ chế phá) → tài năng bộc lộ chậm, cần qua thời gian dồi mài (ý nghĩa)."
- **Giải nghĩa thuật ngữ ngay lần đầu**: tam hợp, xung chiếu, vô chính diệu, Tuần, Triệt, đắc địa, hãm địa, đại hạn, tiểu hạn, sao lưu…
- **Dẫn nguồn** cho các ý then chốt (`TVCN1 L2141`), nhưng đừng để chú thích nguồn lấn át lời văn.
- **Ghi rõ độ chắc** khi cần: chắc (nhiều yếu tố cùng chỉ một hướng), khá, thấp (chỉ một yếu tố, hoặc thuộc cung Phụ Mẫu, Huynh Đệ).
- **Mâu thuẫn trong lá số**: khi sao tốt và sao xấu cùng có mặt, phải cân. Bên nào đắc địa hơn, hợp bản mệnh hơn, được tam hợp ủng hộ hơn thì thắng. Nói rõ kết quả cân.
- **Câu cụ thể, không mơ hồ.** Viết "từ khoảng 36 tuổi (đại hạn Tử Tức) tiền mới ổn". Không viết "về sau ổn".
- Dùng tiêu đề, bảng và gạch đầu dòng để dễ đọc. Văn xuôi đủ ý, không viết kiểu điện tín.

## 4. Tự kiểm trước khi gửi

- [ ] Đủ các phần I–VIII. Đủ 12 cung. Đủ các đại hạn đến khoảng 85 tuổi.
- [ ] Đã nêu cách cục chính và dẫn nguồn. Không bỏ sót cách lớn: chạy `tra` theo cụm chính tinh ở tam hợp Mệnh, Quan, Tài.
- [ ] Mỗi sát tinh ở Mệnh, Thân và các cung hạn đều đã cân đắc hay hãm, có được chế hay không.
- [ ] Năm xem có phân tích từng tháng. Có bảng hạn hung.
- [ ] Không còn câu nào chỉ là nhãn sao, kiểu "có Lộc nên kiếm tiền được", mà thiếu cơ chế và thời điểm.
- [ ] Không có lời phán nào dựa vào vị trí sao tự nhẩm. Mọi vị trí lấy từ `laso.py`.

## 5. Ví dụ về độ sâu (nam, 14/5/2001, 18h, Tân Tỵ)

Một bài luận viết **sai** về lá số này: "Quan Lộc có Cự Môn Hóa Lộc: nghề dùng miệng lưỡi, có Lộc nên kiếm tiền được."
Bài đó đã bỏ sót:

- **Cách thạch trung ẩn ngọc.** Cự Môn ở Tý có Hóa Lộc tại chỗ, Thái Dương Hóa Quyền ở Thìn chiếu về (TT04 L199-201; TVCN1 L3087: "tuổi Thủy, Kim, Mộc gặp Cự Tý Ngọ + Khoa Quyền Lộc thì đỗ và làm nên to"). Mệnh Kim nên hợp. Đây là cách lớn nhất của lá số, cần nói ngay ở phần I.
- **Mệnh Thân vô chính diệu nằm trong bộ Cự Nhật.** Tam hợp gồm Tý (Cự) và Thìn (Nhật), xung chiếu là Dần (Đồng Lương). Theo TVCN2 L1117, Mệnh ở Thân mượn chính tinh ở Dần. Như vậy Mệnh hội đủ bộ **Cơ Nguyệt Đồng Lương và Cự Nhật**, tức dòng chính tinh "mặt trắng", trọng trí tuệ, hợp với chuyên môn, công chức, giáo dục, pháp lý (TT01 L317).
- **Mệnh có Tuần, lại vô chính diệu.** TVCN2 L1109 nói Mệnh có Tuần thì *cần* vô chính diệu "mới mong mát mặt", nên đây là điểm lợi. Kết hợp với "Tuần Triệt niên đầu thiếu niên tân khổ", ý đúng là: thời trẻ chật vật, sau mới thông.
- **Đà La (Kim) ở Mệnh Kim, cung Thân: hai sách nói ngược nhau, phải cân.**
  - TT03 L354 và L344 coi "Mệnh Kim có Đà La ở Dần Thân Tỵ Hợi" là vô chính diệu đắc cách: sát tinh hợp hành với Mệnh.
  - TVCN2 L1121-1122 cũng nói vô chính diệu có hung tinh đồng hành bản mệnh, Mệnh Kim hoặc Hỏa, thì tốt, nhưng phải *tránh Tuần Triệt*.
  - TVCN1 L2281 lại nói Đà La ở Dần Thân Tỵ Hợi là hãm. Câu này chép nguyên bảng của Kình Dương, trong đó có cả Tý Ngọ Mão Dậu, là những cung Đà La **không bao giờ đứng được** (Đà luôn ở cung ngay trước Lộc Tồn). Vì vậy câu này kém tin cậy hơn.
  - Kết luận: Đà ở đây có mặt tốt, vì hợp hành Kim và đóng ở cung Kim. Nhưng mặt tốt ấy bị Tuần làm yếu và bị Địa Kiếp kéo xuống. Tính quả quyết, lì đòn có thật, còn "phát" thì chậm. Phải viết đủ cả hai mặt, không kết luận một chiều.
- **Địa Kiếp ở Mệnh, Địa Không ở Di.** Cách "đắc tam không" chỉ dành cho Mệnh Hỏa (TVCN2 L1121, TT04 L562), nên không áp dụng được. Với Mệnh Kim, Không Kiếp là trở lực (TT04 L552: "Kim Mệnh gặp Không Kiếp... phải có Triệt"). Ở đây Tuần đã che bớt.
- **Âm nam, Mệnh ở cung dương nên nghịch lý; Mệnh ở vị trí Thiếu Âm.** Người thật thà, hay chịu thiệt. Lợi ích thường đến qua phúc tinh và qua người giúp, không đến qua tranh giành (TT09 L8-28; TT04 L363-367).
- **Năm 2026.** Đại hạn ở Phu Thê (Ngọ) trùng lưu Thái Tuế, lưu Kình Dương và lưu Hóa Quyền, cộng với Hỏa Tinh và Thiên Không gốc. Tiểu hạn ở Mệnh có Đà và Kiếp tại chỗ, Thiên Hình từ Quan chiếu về, lưu Tang Môn và lưu Thiên Mã cũng ở đó. Năm này động mạnh: đổi chỗ, đổi việc, tình cảm có biến. Phải nêu từng tháng, và nói rõ Hóa Lộc, Hóa Quyền ở tam hợp tiểu hạn là phần cứu giải.
