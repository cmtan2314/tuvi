# Khuôn bài luận lá số (bắt buộc)

Người đọc không biết Tử Vi và sống ở **thời hiện đại**. Một bài đạt yêu cầu phải:
- **đủ**: mọi phần ở mục 2;
- **hai lớp**: lớp Tam Hợp (sao, đắc hãm, cách cục) và lớp **Tứ Hóa** (phi hóa, tự hóa, Kỵ; mục 2b) trong *mọi* phần của bài;
- **sâu**: mỗi nhận định có chuỗi *dữ kiện → cơ chế → ý nghĩa đời thường → thời điểm → lời khuyên*;
- **cân**: mọi sao đều xét đắc hay hãm. Chỗ nào nguồn mâu thuẫn thì suy luận rồi nói rõ đã chọn gì, vì sao;
- **hiện đại**: dịch lời sách cổ sang hoàn cảnh ngày nay (mục 4);
- **không giới hạn trên, có mức sàn**: mỗi phần phải dài **hơn** mức sàn ghi ở tiêu đề của nó (mức tối đa cũ). Toàn bài tối thiểu **10.000 từ**; với 5 agent thì thường trên 20.000 từ. Không cắt bớt vì sợ dài, không gộp ý cho gọn;
- **dễ hiểu**: thuật ngữ nào cũng giải nghĩa ngay lần đầu xuất hiện.

Không được:
- gửi bản tóm tắt rồi hỏi "muốn xem sâu phần nào";
- ghi "hạn chế: chưa tra miếu hãm" hoặc "chưa đọc nguyên văn". Những việc đó phải **làm xong trước khi viết**.

## 1. Chuẩn bị (làm xong mới viết)

1. Chạy `python3 <skill>/scripts/laso.py ... --namxem <năm nay> --quet 25`. Lệnh in ra bốn thứ:
   - **Lá số.** Mặc định dùng engine Bắc phái: mỗi sao có độ sáng *miếu > vượng > đắc > bình > nhàn > hãm*, kèm phi hóa và sao lưu Bắc phái (Đv. đại vận, L. lưu niên).
   - **KHUNG LUẬN**: âm dương, vòng Thái Tuế, Tràng Sinh, Tứ Hóa, tam phương tứ chính từng cung (kèm độ sáng), đại hạn, sao lưu, nguyệt hạn.
   - **KHUNG TỨ HÓA** (phái Khâm Thiên): lai nhân cung, nguyên thần cung, tứ hóa năm sinh kèm nam/nữ tinh, phi hóa 12 cung có tên sao, tự hóa ly tâm và hướng tâm, song tượng và phá tượng, các cách Kỵ, tứ hóa đại hạn và lưu niên kèm cờ. Khung tính trên đúng vị trí sao của engine.
   - **QUÉT HẠN**: cờ hung và cát cho từng năm.

   Đọc dòng `Ghi chú` để biết đang dùng engine nào và những sao nào Bắc phái an khác sách.
2. Tra song song (mỗi lệnh khoảng 30ms). Tối thiểu cần tra:
   - mỗi chính tinh ở 12 cung, kèm tên cung: `tra cu mon quan loc`, `tra thai duong tai bach`, `tra thien co phu the`…;
   - đắc hay hãm theo sách của từng chính tinh và sát tinh quan trọng, để đối chiếu với engine: `tra thien dong dan`, `tra da la ham`;
   - các **cách cục** nghi có (cụm sao ở tam hợp): `tra thach trung an ngoc`, `tra co nguyet dong luong`, `tra vo chinh dieu`…;
   - các sát tinh lớn ở Mệnh, Thân và những cung hạn sắp tới;
   - mục "nghề nghiệp" (TVCN2 L1298-1652) theo các sao ở Quan Lộc và Mệnh;
   - **mỗi cờ trong KHUNG TỨ HÓA**: đọc thẻ của cách đó, ví dụ `tra -b KTSC tiet kho ky`, `tra -b KTSC thuy menh ky`, `tra -b KTSC pha tuong`; hàm nghĩa cung có lai nhân, ví dụ `tra -b KTSC lai nhan tat ach`; mục hôn nhân, lục thân, bệnh tật của KTTH khi luận các phần đó.
3. Ghi nháp cho từng cung (đủ 12 cung rồi mới viết):
   - sao gì, độ sáng theo engine và theo sách, có khớp nhau không;
   - sinh khắc với bản mệnh;
   - tam hợp và xung chiếu;
   - Tuần, Triệt;
   - **Tứ Hóa**: cung có hóa năm sinh nào, tự hóa gì, nhận Lộc/Kỵ từ cung nào, phi Lộc/Kỵ đi đâu;
   - kết luận cân được.

## 2. Đắc hãm: dùng thế nào, khi lệch thì làm gì

- **Độ sáng là trọng số, không phải nhãn tốt/xấu.**
  - Chính tinh miếu hoặc vượng: tính chất tốt của sao trội, hợp với nghề đúng "chất" của sao.
  - Chính tinh hãm: mặt trái của sao trội (Cự hãm thì thị phi, Tham hãm thì sa đà, Phá hãm thì phá tán).
  - Sát tinh đắc địa (Kình, Đà, Không, Kiếp, Hỏa, Linh): thành dũng khí, quả quyết, dám làm.
  - Sát tinh hãm: thành tai họa (TT03 L342).
- **Engine và sách lệch nhau.** Engine dùng bảng Bắc phái, sách Việt (TVCN, TVNL) có bảng khác. Ví dụ: Thiên Đồng ở Dần, engine chấm `nhàn`, còn TVCN1 L2141 nói Đồng Lương ở Dần Thân là "tốt nhất". Gặp chỗ lệch thì suy luận theo thứ tự sau, rồi nói rõ đã chọn gì:
  1. **Cơ chế ngũ hành của sao so với cung.** Sao được cung sinh, hoặc cùng hành với cung, thì vững. Sao bị cung khắc thì yếu. Ví dụ: Thiên Đồng hành Thủy ở Dần hành Mộc thì sinh xuất, tức hao sức; Thiên Lương hành Mộc ở Dần là cùng hành, tức vững.
  2. **Bộ sao đứng chung.** Đồng Lương ở Dần là một bộ: Lương miếu gánh cho Đồng. Sách khen *cả bộ*, engine chấm *từng sao*. Hai bên không hẳn trái nhau.
  3. **Sách Việt có nói rõ vị trí đó không.** Nói rõ và có lý do thì nặng ký hơn bảng chung chung.
  4. **Sao có thể đứng ở cung đó không.** Câu sách nêu vị trí mà sao không thể đứng được là câu chép sai (ví dụ Đà La, xem mục 7).
  5. Kết luận theo **mức** (mạnh / vừa / yếu), không theo đúng/sai tuyệt đối.
- **Hóa giải và gia tăng.**
  - Tuần, Triệt: làm sao tốt giảm, sao xấu bớt hại.
  - Hóa Lộc, Quyền, Khoa và Tả Hữu, Xương Khúc, Khôi Việt: nâng sao lên.
  - Hóa Kỵ, Không Kiếp: kéo sao xuống.

  Ghi rõ sao đang được nâng hay bị kéo bởi cái gì.

## 2b. Tứ Hóa (phái Khâm Thiên): dùng thế nào

Dữ kiện lấy ở KHUNG TỨ HÓA, không tự nhẩm. Cách đọc:
- **Hóa năm sinh là "thể", tự hóa và phi hóa là "dụng"** (KTSC L1675). Hóa năm sinh nói việc gốc của đời; tự hóa nói việc đó động ra sao; phi hóa nói nó chảy về đâu.
- **Đơn tượng không cát hung, song tượng mới thành việc** (KTSC L197-217). Một Hóa Lộc đứng một mình chỉ là khuynh hướng. Kết luận cát hung chỉ đưa ra khi có song tượng: hai hóa cùng cung, hóa năm sinh gặp tự hóa, hay Lộc ở cung này mà Kỵ ở cung kia cùng một tổ.
- **Lộc nhân Kỵ quả**: thấy Lộc thì đi tìm Kỵ. Lộc ở đâu là chỗ duyên khởi, Kỵ ở đâu là chỗ kết quả, chỗ "nợ" (KTSC L1671-1690).
- **Lai nhân cung** là chốt khởi động của đời. Viết nó vào phần I và đọc hàm nghĩa theo cung (KTSC Tiết 6–7).
- **Kỵ là trục chính để báo hạn.** Đọc cờ Kỵ của bàn gốc, đại hạn, lưu niên theo nguyên tắc cấp dưới xung cấp trên: lưu niên xung đại hạn, đại hạn xung bản mệnh (KTSC L1641).
- **Không trộn hai phái thành một câu kết.** Viết lớp Tam Hợp trước, lớp Tứ Hóa sau, rồi nói rõ hai lớp **cùng chiều** (tăng độ tin) hay **ngược chiều** (giải thích vì sao, lớp nào nặng hơn ở việc này). Ví dụ: Tam Hợp thấy Tài có Lộc Tồn, Tứ Hóa thấy tiết khố kị; kết luận là kiếm được nhưng khó giữ, rồi chỉ ra cơ chế của từng lớp.
- **Thuật ngữ Khâm Thiên khác Tam Hợp.** "Tứ chính", "tam phương" trong sách Khâm Thiên mang nghĩa khác (KTSC L468-470). Ngũ hành sao theo can là của riêng phái này. Giải nghĩa mọi thuật ngữ cho người đọc: lai nhân, tự hóa ly tâm, hướng tâm, các cách Kỵ.
- Cờ trong khung chỉ là **điều kiện đủ theo sách**. Mỗi cờ phải tra thẻ, đọc đúng nghĩa, rồi dịch sang đời sống hiện đại như mục 4.

## 3. Các phần của bài

Bài được viết bởi nhiều agent theo **khối tam hợp** (xem `dieu-phoi.md`). Các phần dưới đây là **yêu cầu nội dung**; bảng phân công trong `dieu-phoi.md` cho biết agent nào viết phần nào. Bài hoàn chỉnh xếp theo thứ tự: I → bốn khối tam hợp (chứa II, III) → IV → V → VI → VII → VIII.

### I. Tổng quan lá số (tối thiểu 600 từ)
- Ngày giờ âm dương lịch, âm dương nam nữ, chiều đi.
- Bản mệnh và cục kèm giải nghĩa hình ảnh. Ví dụ: "Bạch Lạp Kim là kim trong nến, chất quý nhưng cần lửa luyện; Hỏa lục cục khắc Kim, nghĩa là môi trường ép mình phải rèn".
- Thuận lý hay nghịch lý âm dương. Vị trí Mệnh trong vòng Thái Tuế và ý nghĩa đối với thái độ sống.
- **Cách cục chính**: tên cách, vì sao thành, cái gì phá hoặc giảm cách, mức độ thành cách, dẫn nguồn.
- **Tứ Hóa tổng quan**: lai nhân cung và nguyên thần cung (đời xoay quanh việc gì); bốn hóa năm sinh nằm ở đâu, nam hay nữ tinh; trục Lộc nhân Kỵ quả; cung tự hóa nhiều nhất; các cờ Kỵ lớn của bàn gốc.
- **Chân dung** 6–10 câu: người này là ai, mạnh ở đâu, yếu ở đâu, đời đi theo đường cong nào (sớm hay muộn, lên hay xuống).

### II. Mệnh và Thân: tính cách, con người (tối thiểu 1.200 từ)
- Chính tinh thủ Mệnh và độ sáng. Mệnh vô chính diệu thì nói mượn sao nào, theo quy tắc nào (TVCN2 L1117-1126), cộng với tam hợp.
- Tính cách cụ thể, chia thành các mặt:
  - cách suy nghĩ;
  - cách giao tiếp;
  - phản ứng khi áp lực;
  - điểm mù;
  - thói quen tiêu tiền;
  - cách yêu;
  - cách làm việc nhóm.

  Mỗi mặt phải gắn với sao cụ thể.
- Ngoại hình theo sao thủ Mệnh (TVCN1 L2765-2909).
- Thân cư cung nào: hậu vận (sau khoảng 30–35 tuổi) dồn trọng tâm về đâu.
- Từng sát tinh ở Mệnh: đắc hay hãm, hợp hay khắc bản mệnh, có được chế không. Kết luận là hại hay thành lợi.
- Tuần, Triệt ở Mệnh hoặc Thân: tác động lên tuổi trẻ, và lúc nào thì "mở".

### III. Từng lĩnh vực (mỗi mục tối thiểu 900 từ)
Trình tự cho mỗi mục: **sao thủ (độ sáng) → tam hợp, xung chiếu → sinh khắc → cách → lớp Tứ Hóa → nghĩa đời thường hôm nay → thời điểm (đại hạn hay năm nào kích hoạt) → rủi ro → lời khuyên hành động**.

Lớp Tứ Hóa của mỗi mục: cung chủ có hóa năm sinh hay tự hóa gì; phi Lộc, Kỵ đi đâu; nhận Lộc, Kỵ từ cung nào; cờ liên quan. Gợi ý theo mục:
- sự nghiệp: thủy mệnh kị, nghịch thủy kị, thủy tiết kị (hợp làm công hay tự lập); Mệnh và Quan phi hóa vào lục nội hay lục ngoại (KTSC L324);
- tiền: tuyến Tài–Phúc, Điền là kho; nhập khố kị, tiết khố kị; Tài phi Kỵ đi đâu là tiền chảy về đâu (lưu thủy kị);
- hôn nhân: Phu Thê và Điền đủ âm dương hay cô âm, độc dương; Phu tự hóa; Mệnh và Phu phi hóa cho nhau (thị phi kị, oán thán kị); Lộc tự hóa Lộc ở Phu dễ ngoại tình (KTSC L1526-1531); xem thêm mục hôn nhân của KTTH;
- con cái, lục thân: tuần hoàn kị, thị phi kị giữa các lục thân cung;
- sức khỏe: Kỵ vào Tật hoặc xung Tật; mục lục thân và sức khỏe của KTTH (Huynh, Nô, Phúc là cung then chốt);
- Thiên Di: sách mã kị (bôn ba, xa quê).

1. **Sự nghiệp (Quan Lộc + Mệnh + Thiên Di).**
   - 5–8 **nghề hoặc vị trí cụ thể của thời nay**, mỗi nghề kèm lý do lấy từ sao.
   - Hợp làm chủ hay làm thuê; làm cho nhà nước, tập đoàn, startup hay tự do.
   - Môi trường hợp. Kiểu sếp và đồng nghiệp hợp.
   - Lộ trình theo từng đại hạn: lúc nào học, lúc nào bứt lên, lúc nào nên đổi hướng.
   - Rủi ro nghề nghiệp: pháp lý, thị phi, kiệt sức.
2. **Tiền bạc (Tài Bạch + Điền Trạch + Phúc).**
   - Tiền đến từ đâu: lương, chuyên môn, kinh doanh, đầu tư hay may rủi.
   - Giữ được tiền hay không. Kiểu chi tiêu.
   - Có hợp đầu tư chứng khoán, crypto, bất động sản không. Có nên cho vay, đứng tên, bảo lãnh không.
   - Giai đoạn kiếm nhiều, giai đoạn hao, theo tuổi.
   - Nhà đất: lúc nào mua được, mua kiểu nào.
3. **Tình duyên, hôn nhân (Phu Thê + Phúc + Đào Hồng Hỷ).**
   - Người phối ngẫu: tính cách, nghề có thể, hoàn cảnh, ngoại hình.
   - Gặp nhau thế nào: qua công việc, học hành, mạng hay đi xa.
   - Khoảng tuổi cưới hợp, theo đại hạn và các năm có Hồng, Hỷ, Đào chiếu.
   - Mâu thuẫn dễ gặp; nguy cơ đổ vỡ, ngoại tình, ly thân; điều kiện để giữ.
   - Lời khuyên cụ thể.
4. **Con cái (Tử Tức).** Đông hay ít, lúc nào có con dễ, quan hệ cha mẹ – con, con có hợp không. Thời nay có chuyện sinh muộn, hiếm muộn, hỗ trợ sinh sản: nói khi lá số có chỉ báo.
5. **Sức khỏe (Tật Ách + Mệnh + hạn).**
   - Bộ phận yếu theo sao và ngũ hành (TVCN1 có mục Giải Ách theo từng sao), dịch sang bệnh danh hiện đại khi đủ cơ sở.
   - Tuổi cần phòng. Nguy cơ tai nạn: giao thông, dao kéo hay phẫu thuật, sông nước.
   - Lối sống nên giữ.
6. **Phúc Đức.** Phúc dòng họ, tổ tiên, sự che chở, tâm linh. Tuổi thọ nếu sách có cách tính.
7. **Thiên Di.** Ra ngoài gặp quý nhân hay tiểu nhân; có hợp xuất ngoại, định cư, làm việc xa nhà không.
8. **Cha mẹ, anh em, bạn bè, đồng nghiệp, cấp dưới (Phụ Mẫu, Huynh Đệ, Nô Bộc).** Luận đủ, nhưng nói rõ độ tin thấp (TVCN1 tự nhận phần này "sai 7–8 phần"). Thời nay, Nô Bộc là đồng nghiệp, cấp dưới, đối tác, bạn bè, cả mạng lưới quan hệ.

### IV. Vận hạn trọn đời: từng đại hạn 10 năm (mỗi hạn tối thiểu 450 từ)
Viết **tất cả** các đại hạn đến khoảng 85 tuổi. Đại hạn đã qua cũng viết đủ, kèm các điểm cụ thể để người đọc tự kiểm độ đúng.

Mỗi đại hạn gồm:
- cung, sao thủ và độ sáng, tam hợp chiếu;
- hành cung so với bản mệnh; Nam hay Bắc đẩu so với âm dương (TVCN1 L1839); Tuần, Triệt;
- sao lưu đại vận Bắc phái (dòng `Lưu (Bắc phái)`, tiền tố `Đv.`), nếu có;
- **tứ hóa đại hạn**: bốn hóa theo can của đại Mệnh rơi vào bản cung nào; đại Kỵ xung bản cung nào; cờ phản cung kị, tuyệt mệnh kị. KHUNG TỨ HÓA chỉ in sẵn đại hạn hiện tại. Đại hạn khác thì chạy lại `laso.py` với `--namxem` rơi vào hạn đó;
- **chủ đề** của 10 năm và **mức độ**: tốt / khá / trung bình / xấu / rất xấu, kèm lý do;
- việc nên làm trong hạn: học gì, đầu tư gì, cưới hay chưa, đổi việc hay chưa;
- những năm cao điểm và năm phải đề phòng trong hạn, lấy từ QUÉT HẠN.

### V. Năm đang xem (tối thiểu 1.800 từ)
- **Tứ hóa lưu niên**: bốn hóa theo can năm rơi vào bản, đại và lưu cung nào; cờ Kỵ lưu niên (xung đại Mệnh, xung bản Mệnh hay Quan, lưu Di phi Kỵ).
- Đại hạn, tiểu hạn, sao lưu đè lên đâu. Có hai bộ sao lưu: `L.*` do Python an theo quy tắc sao năm sinh, và `L.`/`N.` của Bắc phái.
- Năm đó ở từng mặt: công việc, tiền, tình cảm, sức khỏe, pháp lý, đi lại.
- **Từng tháng trong 12 tháng** theo nguyệt hạn. Mỗi tháng ghi cung, sao đáng chú ý, nên làm gì, tránh gì.
- Danh sách việc nên làm và việc nên tránh, cụ thể đến mức người đọc làm theo được.

### VI. Bảng hạn hung (bắt buộc; quét 25 năm trở lên)
Lập bảng các năm có cờ nặng trong QUÉT HẠN. Cờ nặng gồm:
- đại tiểu hạn trùng phùng có sát;
- Kình Đà gặp Thái Tuế;
- Thương Sứ, nhất là khi đại tiểu hạn cùng gặp;
- Không Kiếp tại hạn;
- lưu Kình hoặc lưu Kỵ đè lên đại hạn;
- cờ Kỵ của Tứ Hóa: tuyệt mệnh kị, phản cung kị, đại hoặc lưu Kỵ xung bản Mệnh hay Quan (chạy `laso.py --namxem <năm>` cho các năm nghi vấn).

Mỗi dòng của bảng gồm:
- năm và tuổi;
- cờ gì;
- **ứng vào việc gì ngày nay**: Hình là kiện tụng, phẫu thuật, tai nạn dao kéo; Kỵ là thị phi, scandal mạng, hợp đồng trục trặc; Kình Đà là tai nạn, va chạm; Tang Hổ là tang, ốm, viện phí; Không Kiếp là mất tiền, lừa đảo, đầu tư hỏng; Mã gặp sát là tai nạn giao thông;
- sao giải nào có mặt;
- mức độ;
- cách phòng **cụ thể**: bảo hiểm, khám định kỳ, không ký bảo lãnh, không lái xe đêm…

Nói thẳng, không né, nhưng không dọa.

### VII. Tổng kết và lời khuyên (tối thiểu 600 từ)
- 5 điểm mạnh nên tận dụng, 5 điểm yếu phải phòng.
- Các mốc tuổi quan trọng nhất.
- Một "chiến lược đời" cụ thể: học gì, làm gì, cưới khi nào, tích lũy ra sao.

### VIII. Ghi chú phương pháp
- Engine và các quy ước đã dùng. Hai lớp: Tam Hợp (TVCN, TVNL) và Tứ Hóa phái Khâm Thiên (KTTH, KTSC), dùng bảng tứ hóa của phái, tuổi Canh Khoa Âm Kỵ Đồng.
- Những chỗ sách hoặc engine mâu thuẫn, và đã chọn theo hướng nào, vì sao.
- Độ tin của từng phần.

## 4. Áp dụng vào thời hiện đại

Sách viết cho xã hội nông nghiệp và quan trường cũ. Phải **dịch theo bản chất của sao**, không dịch từng chữ. Bảng dưới đây là suy luận từ tính chất ngũ hành và chức năng của sao. Khi dùng thì nói là "ngày nay có thể hiểu là…".

| Lời sách | Ngày nay |
|---|---|
| làm quan, đỗ đạt | thăng chức, có vị trí quản lý trong tổ chức; đỗ bằng cấp, chứng chỉ; trúng tuyển công chức |
| quan võ, võ cách | quân đội, công an, an ninh; nghề kỹ thuật nặng; thể thao; ngành cạnh tranh mạnh (sales, trading) |
| đầy tớ, tôi tớ | nhân viên cấp dưới, đồng nghiệp, đối tác, khách hàng thân |
| ruộng, mẫu, sào | bất động sản, tài sản lớn |
| buôn bán | kinh doanh, thương mại điện tử, khởi nghiệp |
| kiện tụng, quan tụng | tranh chấp pháp lý, thuế, hợp đồng, kỷ luật nơi làm việc |
| chết đuối, chết đường | tai nạn sông nước, tai nạn giao thông |
| tà ma, điên cuồng | áp lực tâm lý, mất ngủ, trầm cảm, nghiện |
| đa dâm, lẳng lơ (nữ mệnh) | đời sống tình cảm phức tạp, dễ bị hấp dẫn, dễ vướng chuyện tình. Viết trung tính, không phán xét giới |
| khắc chồng, sát vợ | hôn nhân dễ căng thẳng, dễ chia tay, ly thân, hoặc hai người sống xa nhau |
| bỏ làng, ly hương | chuyển thành phố, đi làm xa, du học, định cư nước ngoài |
| hiếm con, cầu tự | sinh muộn, hiếm muộn, có thể cần hỗ trợ y tế |

Chính tinh và nghề thời nay. Đây là gợi ý, phải cân thêm độ sáng và các sao đi kèm:

| Sao | Bản chất | Nghề và vai trò ngày nay |
|---|---|---|
| Tử Vi | đế tinh, điều hành | lãnh đạo, quản lý cấp cao, chủ doanh nghiệp |
| Thiên Cơ | mưu trí, máy móc | kỹ sư, IT, phân tích dữ liệu, chiến lược, cơ khí chính xác, tư vấn |
| Thái Dương | phát sáng, công khai | truyền thông, giáo dục, chính trị, điện lực, ngoại giao, người có tiếng |
| Vũ Khúc | tài tinh, kim khí | tài chính, ngân hàng, kế toán, kim loại, cơ khí, quân sự kỹ thuật |
| Thiên Đồng | hưởng thụ, hòa | dịch vụ, chăm sóc khách hàng, F&B, du lịch, phúc lợi, tâm lý trẻ em |
| Liêm Trinh | kỷ luật, tù tinh | pháp chế, kiểm toán, thanh tra, điện tử, quân đội, chính trị nội bộ |
| Thiên Phủ | kho, giữ của | quản lý tài sản, ngân hàng, kho vận, hành chính, bảo hiểm |
| Thái Âm | âm nhu, điền sản | bất động sản, tài chính, thiết kế, nghệ thuật, chăm sóc, công việc ban đêm |
| Tham Lang | dục vọng, giao tế | kinh doanh, sales, giải trí, ẩm thực, làm đẹp, quan hệ công chúng |
| Cự Môn | miệng, ám tinh | luật sư, giảng dạy, MC, sales, tư vấn, nghiên cứu, y (chẩn đoán) |
| Thiên Tướng | ấn, phò tá | hành chính, nhân sự, ngoại giao, thư ký cấp cao, thời trang |
| Thiên Lương | ấm che, thọ | y, dược, bảo hiểm, giáo dục, công tác xã hội, thanh tra |
| Thất Sát | tướng tinh, đơn độc | quân sự, ngoại khoa, quản lý khủng hoảng, khởi nghiệp mạo hiểm |
| Phá Quân | phá cũ, đổi mới | khởi nghiệp, cải tổ, vận tải, xây dựng hay phá dỡ, công nghệ đột phá |
| Xương Khúc | văn, nghệ | viết lách, content, thiết kế, âm nhạc, giáo dục |
| Thiên Mã | di chuyển | logistics, xuất nhập khẩu, du lịch, lái xe, làm việc từ xa, đi công tác nhiều |
| Hóa Kỵ | vướng mắc, thị phi | ngày nay còn là scandal mạng, bị review xấu, hợp đồng kẹt |

## 5. Quy tắc viết

- **Chuỗi lý do cho mọi nhận định.** Ví dụ: "Cự Môn (vượng) ở Tý có Hóa Lộc (dữ kiện), là cách 'thạch trung ẩn ngọc', tức ngọc trong đá, cần Khoa Lộc và Thái Dương ở Thìn soi sáng (TT04 L199-201) (cơ chế). Ở đây Lộc ở tại chỗ, Thái Dương (vượng) Hóa Quyền ở Thìn chiếu về, nên cách thành. Nhưng Thái Dương bị Triệt nên ánh sáng đến muộn (cơ chế phá). Kết quả là năng lực chuyên môn, ăn nói, phân tích rất mạnh nhưng được công nhận chậm, cần bằng cấp hoặc chứng chỉ làm 'đá mài' (ý nghĩa). Thời điểm bung là đại hạn Tài Bạch 46–55, sớm hơn nếu có năm lưu Lộc nhập Quan (thời điểm)."
- **Giải nghĩa thuật ngữ ngay lần đầu**: tam hợp, xung chiếu, vô chính diệu, Tuần, Triệt, miếu, vượng, đắc, hãm, đại hạn, tiểu hạn, sao lưu…
- **Dẫn nguồn** ở các ý then chốt, ví dụ `TVCN1 L2141`. Không để chú thích nguồn lấn át lời văn.
- **Độ chắc**: chắc (nhiều yếu tố cùng chỉ một hướng), khá, thấp (chỉ một yếu tố, hoặc thuộc cung Phụ Mẫu, Huynh Đệ).
- **Cân mâu thuẫn trong lá số.** Khi sao tốt và sao xấu cùng có mặt, bên nào sáng hơn, hợp bản mệnh hơn, được tam hợp ủng hộ hơn thì thắng. Nói rõ kết quả cân.
- **Câu cụ thể.** Viết "khoảng 36–45 tuổi (đại hạn Tử Tức)". Không viết "về sau".
- Dùng tiêu đề, bảng, gạch đầu dòng, nhưng phần giải thích phải là văn xuôi đủ ý.

## 6. Tự kiểm trước khi gửi

- [ ] Đủ các phần I–VIII. Đủ 12 cung. Đủ các đại hạn đến khoảng 85 tuổi. Năm xem có đủ 12 tháng. Có bảng hạn hung.
- [ ] Mỗi chính tinh và sát tinh được nhắc tới đều có độ sáng. Chỗ engine lệch sách đã được suy luận theo mục 2.
- [ ] Đã nêu cách cục chính, kèm nguồn. Không sót cách lớn: đã `tra` các cụm chính tinh ở tam hợp Mệnh, Quan, Tài.
- [ ] Mọi lời sách cổ đã được dịch sang hoàn cảnh hiện đại (mục 4).
- [ ] Không có câu nào chỉ là nhãn sao, thiếu cơ chế, thời điểm và lời khuyên.
- [ ] Không có mục "hạn chế: chưa tra…". Việc nào cần tra thì đã tra.
- [ ] Mọi vị trí sao lấy từ `laso.py`, không tự nhẩm.
- [ ] Mỗi phần đạt mức sàn số từ ở tiêu đề; toàn bài trên 10.000 từ (đếm bằng `wc -w`).
- [ ] Phần I và mọi mục ở III, IV, V đều có lớp Tứ Hóa. Mỗi cờ trong KHUNG TỨ HÓA đã được tra thẻ và dùng, hoặc nói rõ vì sao bỏ. Đã chỉ ra chỗ hai lớp cùng chiều hay ngược chiều.

## 7. Ví dụ về độ sâu (lá số mẫu, đã ẩn danh)

Bài luận **sai**: "Quan Lộc có Cự Môn Hóa Lộc: nghề dùng miệng lưỡi, có Lộc nên kiếm tiền được." Bài này đã bỏ sót những điểm sau.

- **Cách thạch trung ẩn ngọc.** Cự Môn (vượng) ở Tý có Hóa Lộc tại chỗ, Thái Dương (vượng) Hóa Quyền ở Thìn chiếu về (TT04 L199-201; TVCN1 L3087: "tuổi Thủy, Kim, Mộc gặp Cự Tý Ngọ + Khoa Quyền Lộc thì đỗ và làm nên to"). Người này Mệnh Kim, nên hợp. Đây là cách lớn nhất của lá số. Ngày nay ứng với luật, tư vấn, giảng dạy, phân tích, nghiên cứu, truyền thông chuyên môn.
- **Mệnh ở Thân vô chính diệu, tam hợp Cự Nhật, xung chiếu Đồng Lương** (TVCN2 L1117). Mệnh hội cả bộ Cơ Nguyệt Đồng Lương và Cự Nhật, tức dòng "mặt trắng" trọng trí tuệ (TT01 L317).
- **Đồng Lương ở Dần: engine chấm Đồng `nhàn`, Lương `miếu`; TVCN1 L2141 nói Đồng Lương ở Dần Thân "tốt nhất".** Hai bên lệch nhau, phải cân như sau.
  - Thiên Đồng hành Thủy ở cung Dần hành Mộc, Thủy sinh Mộc nên Đồng tiết khí và yếu. Điểm này engine đúng.
  - Thiên Lương hành Mộc ở cung Mộc, cùng hành nên vững, gánh được cả bộ.
  - Kết luận: phúc hậu, có quý nhân, có tướng thọ. Nhưng phần "hưởng" của Thiên Đồng yếu, nên đời không nhàn, phải tự làm.
- **Mệnh có Tuần, lại vô chính diệu.** TVCN2 L1109 nói Mệnh có Tuần thì *cần* vô chính diệu, nên đây là điểm lợi. Cộng với "Tuần Triệt niên đầu thiếu niên tân khổ": thời trẻ chật vật, sau mới thông.
- **Đà La ở Mệnh Kim, cung Thân. Engine chấm `hãm`, TVCN1 L2281 cũng nói hãm, chỉ TT03 L344-354 coi là đắc cách.** Phải cân như sau.
  - Câu của TVCN1 chép nguyên bảng Kình Dương, có cả Tý Ngọ Mão Dậu, là những cung Đà La **không bao giờ đứng được** vì Đà luôn ở ngay trước Lộc Tồn. Câu này kém tin.
  - Nhưng engine Bắc phái, một nguồn độc lập, cũng chấm hãm.
  - Về cơ chế: Đà hành Kim ở cung Kim là cùng hành, và hợp với Mệnh Kim. Đây là mặt tốt mà TT03 nhấn mạnh.
  - Kết luận: Đà ở đây *nửa đắc nửa hãm*. Tính lì, quả quyết, chịu đựng là thật. Mặt trái là chậm chạp, hay ôm việc, dễ vướng chuyện kéo dài. Thêm Tuần và Địa Kiếp (đắc), mặt phát giảm đi.
- **Địa Kiếp (đắc) ở Mệnh, Địa Không (đắc) ở Di.** Cách "đắc tam không" chỉ dành cho Mệnh Hỏa (TVCN2 L1121, TT04 L562), không áp được ở đây. Với Mệnh Kim, Không Kiếp là trở lực (TT04 L552). Tuần đã che bớt, và Không Kiếp đắc nên thành tính dám nghĩ khác, dám làm. Rủi ro là các quyết định tiền bạc liều lĩnh.
- **Âm nam, Mệnh ở cung dương nên nghịch lý; Mệnh ở vị trí Thiếu Âm.** Người thật thà, hay chịu thiệt. Lợi ích đến qua phúc tinh và người giúp, không đến qua tranh giành (TT09 L8-28; TT04 L363-367).
- **Năm xem.**
  - Đại hạn ở Phu Thê (Ngọ, có Thiên Cơ miếu) trùng lưu Thái Tuế, lưu Kình Dương và lưu Hóa Quyền.
  - Tiểu hạn ở Mệnh có Đà (hãm) và Kiếp (đắc) tại chỗ. Thiên Hình và Hỏa Tinh (hãm) từ Quan chiếu về (vị trí Hỏa Tinh theo Bắc phái). Lưu Tang Môn và lưu Thiên Mã cũng ở Mệnh.
  - Năm động: đổi chỗ, đổi việc, có biến về tình cảm.
  - Hóa Lộc, Hóa Quyền ở tam hợp tiểu hạn là phần cứu giải.
  - Phải viết đủ 12 tháng.
