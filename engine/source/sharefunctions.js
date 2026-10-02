var tru = new Array("Năm", "Tháng", "Ngày", "Giờ");
var nguhanh = new Array("Mộc", "Hỏa", "Thổ", "Kim", "Thủy");
var dd = 1500;
 var lineskip = 22;
var myColor = ['green', 'red', 'yellow', 'grey', 'black'];
var ts = new Array();
ts[1] = "T. Sinh";
ts[2] = "Mộc Dục";
ts[3] = "Quan Đới";
ts[4] = "L. Quan";
ts[5] = "Đế V.";
ts[6] = "Suy";
ts[7] = "Bệnh";
ts[8] = "Tử";
ts[9] = "Mộ";
ts[10] = "Tuyệt";
ts[11] = "Thai";
ts[12] = "Dưỡng";
var muoithan = new Array(10);
muoithan[0] = "Tỷ";
muoithan[1] = "Kiếp";
muoithan[2] = "Thực";
muoithan[3] = "Thương";
muoithan[4] = "T. Tài";
muoithan[5] = "Tài";
muoithan[6] = "T. Quan";
muoithan[7] = "Quan";
muoithan[8] = "Thiên Ấn";
muoithan[9] = "Ấn";

var PI = Math.PI;

var can = new Array();
can[1] = "Giáp";
can[2] = "Ất";
can[3] = "Bính";
can[4] = "Đinh";
can[5] = "Mậu";
can[6] = "Kỷ";
can[7] = "Canh";
can[8] = "Tân";
can[9] = "Nhâm";
can[10] = "Quý";
can[11] = "Giáp";
can[12] = "Ất";
can[0] = "Quý";

var ccan = new Array();
ccan[1] = "G.";
ccan[2] = "Ấ.";
ccan[3] = "B.";
ccan[4] = "Đ.";
ccan[5] = "M.";
ccan[6] = "K.";
ccan[7] = "C.";
ccan[8] = "T.";
ccan[9] = "N.";
ccan[10] = "Q.";
ccan[11] = ".";
ccan[12] = "Ấ.";
ccan[0] = "Quý";

var canth = new Array();
canth[1] = "9";
canth[2] = "8";
canth[3] = "7";
canth[4] = "6";
canth[5] = "5";
canth[6] = "9";
canth[7] = "8";
canth[8] = "7";
canth[9] = "6";
canth[10] = "5";
canth[11] = "9";
canth[12] = "8";
canth[0] = "Quý";

var chi = new Array();
chi[1] = "Tý";
chi[2] = "Sửu";
chi[3] = "Dần";
chi[4] = "Mão";
chi[5] = "Thìn";
chi[6] = "Tỵ";
chi[7] = "Ngọ";
chi[8] = "Mùi";
chi[9] = "Thân";
chi[10] = "Dậu";
chi[11] = "Tuất";
chi[12] = "Hợi";
chi[0] = "Hợi";
var chith = new Array();
chith[1] = "9";
chith[2] = "8";
chith[3] = "7";
chith[4] = "6";
chith[5] = "5";
chith[6] = "4";
chith[7] = "9";
chith[8] = "8";
chith[9] = "7";
chith[10] = "6";
chith[11] = "5";
chith[12] = "4";
chith[0] = "Hợi";

var sao = new Array();
sao[1] = "TỬ VI ";
sao[2] = "LIÊM TRINH. ";
sao[3] = "THIÊN ĐỒNG ";
sao[4] = "VŨ KHÚC.-";
sao[5] = "THÁI DƯƠNG ";
sao[6] = "THIÊN CƠ ";
sao[7] = "THIÊN PHỦ ";
sao[8] = "THÁI ÂM ";
sao[9] = "THAM LANG.+";
sao[10] = "CỰ MÔN.+";
sao[11] = "THIÊN TƯỚNG ";
sao[12] = "THIÊN LƯƠNG ";
sao[13] = "THẤT SÁT ";
sao[14] = "PHÁ QUÂN. ";

var ngaytuan = new Array();
ngaytuan[1] = "Chủ Nhật";
ngaytuan[2] = "Thứ Hai";
ngaytuan[3] = "Thứ Ba";
ngaytuan[4] = "Thứ Tư";
ngaytuan[5] = "Thứ Năm";
ngaytuan[6] = "Thứ Sáu";
ngaytuan[7] = "Thứ Bảy";

var xemnhuan;
var trinhan = 1;

var menh = 1;
var l = 17;

var saothem;
var vitrithem;
var translatePos;
var saothem1;
var remember;
var vitrithem1;
var saothem2;
var vitrithem2;
var saothem3;
var vitrithem3;
// Thang.le
// Date: 17/12/2012
// Function convert year to name year(lunar)

var loc, ky;
var image4me;
//=========MAIN PROGRAM

var hanh = new Array();
hanh[2] = "Thủy Nhị Cục";
hanh[3] = "Mộc Tam Cục";
hanh[4] = "Kim Tứ Cục";
hanh[5] = "Thổ Ngũ Cục";
hanh[6] = "Hỏa Lục Cục";

var tinhhe = new Array(12);
for (var i = 1; i < 13; i++)
    tinhhe[i] = new Array(12);
for (var i = 1; i < 13; i++)
    for (var j = 1; j < 13; j++)
        tinhhe[i][j] = "Mệnh Vô Chính Diệu";
tinhhe[5][5] = "Tử vi Tí Ngọ quan hệ tinh thần / vật chất";
tinhhe[5][7] = "Phá quân Dần Thân phản kháng / thuận tòng";
tinhhe[5][9] = "Liêm Phủ Thìn Tuất cảm tình / lý trí";
tinhhe[5][10] = "Thái âm Tị Hợi hướng ngoại / hướng nội";
tinhhe[5][11] = "Tham lang Tí Ngọ ham muốn vật chất / tinh thần";
tinhhe[5][12] = "Đồng Cự Sửu Mùi sáng sủa / âm ám";
tinhhe[5][1] = "Vũ Tướng Dần Thân quá cương / quá nhu";
tinhhe[5][2] = "Nhật Lương Mão Dậu tường hòa / cô kị";
tinhhe[5][3] = "Thất sát Thìn Tuất lý tưởng / ảo tưởng";
tinhhe[5][5] = "Thiên cơ Tị Hợi quyền biến / cơ mưu";

tinhhe[6][6] = "Tử Phá Sửu Mùi bất ổn / an định ";
tinhhe[6][8] = "Thiên phủ Mão Dậu trì trọng / cẩn thận";
tinhhe[6][9] = "Thái âm Thìn Tuất mục tiêu / manh động";
tinhhe[6][10] = "Liêm Tham Tị Hợi tình cảm / vật dục";
tinhhe[6][11] = "Cự môn Tí Ngọ anh hoa nội liễm / nội tâm nghi kị";
tinhhe[6][12] = "Thiên tướng Sửu Mùi ưu nhã / dung tục";
tinhhe[6][1] = "Đồng Lương Dần Thân lãng mạn / nguyên tắc";
tinhhe[6][2] = "Vũ Sát Mão Dậu quyết đoạn / đoản lự";
tinhhe[6][3] = "Thái dương Thìn Tuất bất tha luy / tha luy";
tinhhe[6][5] = "Thiên cơ Tí Ngọ dương cương / âm nhu";

tinhhe[1][1] = "Tử Phủ Dần Thân chủ động / bị động";
tinhhe[1][2] = "Thái âm Mão Dậu kiên cường / bạc nhược";
tinhhe[1][3] = "Tham lang Thìn Tuất kiên nhẫn / táo tiến";
tinhhe[1][4] = "Cự môn Tị Hợi thâm trầm / xung động";
tinhhe[1][5] = "Liêm Tướng Tí Ngọ cương nghị / thúy nhược";
tinhhe[1][6] = "Thiên lương Sửu Mùi chính trực / tinh minh";
tinhhe[1][7] = "Thất sát Dần Thân cô cao / uy quyền";
tinhhe[1][8] = "Thiên đồng Mão Dậu không hư / sung thật";
tinhhe[1][9] = "Vũ khúc Thìn Tuất nhân tuần / tiến thủ";
tinhhe[1][10] = "Thái dương Tị Hợi Tích cực / tiêu cực";
tinhhe[1][11] = "Phá quân Tí Ngọ ngoan hiêu / quả cảm";
tinhhe[1][12] = "Thiên cơ Sửu Mùi thượng tiến / hạ du";

tinhhe[2][2] = "Tử Tham Mão Dậu vật dục / tình dục ";
tinhhe[2][3] = "Cự môn Thìn Tuất kích phát / tao kị";
tinhhe[2][4] = "Thiên tướng Tị Hợi khai sáng lực / nhân nhân thành sự";
tinhhe[2][5] = "Thiên lương Tí Ngọ cô khắc / dung hòa";
tinhhe[2][6] = "Liêm Sát Sửu Mùi phấn phát / cương lệ";
tinhhe[2][9] = "Thiên đồng Thìn Tuất khoáng đạt / đoản chí";
tinhhe[2][10] = "Vũ Phá Tị Hợi thích ứng / phản ảo";
tinhhe[2][11] = "Thái dương Tí Ngọ hư phù / trầm ổn";
tinhhe[2][12] = "Thiên phủ Sửu Mùi khiêm hòa / khiếp nhược.";
tinhhe[2][1] = "Cơ Âm Dần Thân lý trí / tình tự";

tinhhe[3][3] = "Tử Tướng Thìn Tuất hữu tình / vô tình";
tinhhe[3][4] = "Thiên lương Tị Hợi phù đãng / ổn định";
tinhhe[3][5] = "Thất sát Tí Ngọ quyền uy / khắc kị";
tinhhe[3][7] = "Liêm trinh Dần Thân mẫn cảm / đạp thật";
tinhhe[3][9] = "Phá quân Thìn Tuất thiên khô / điều hòa";
tinhhe[3][10] = "Thiên đồng Tị Hợi bạc nhược / kiên cường";
tinhhe[3][11] = "Vũ Phủ Tí Ngọ sanh tài / lý tài";
tinhhe[3][12] = "Âm Dương Sửu Mùi khai láng / trầm uất.";
tinhhe[3][1] = "Tham Lang Dần Thân vật dục / tình dục";
tinhhe[3][2] = "Cơ Cự Mão Dậu ổn trọng / phù bạc";

tinhhe[4][4] = "Tử Sát Tị Hợi quyền uy / chuyên quyền";
tinhhe[4][8] = "Liêm Phá Mão Dậu phụng công / tư lợi";
tinhhe[4][10] = "Thiên phủ Tị Hợi tường hòa / quyền thuật";
tinhhe[4][11] = "Đồng Âm Tí Ngọ Tích cực / tiêu cực";
tinhhe[4][12] = "Vũ Tham Sửu Mùi dục vọng / dã tâm";
tinhhe[4][1] = "Cự Nhật Dần Thân đắc trợ / cô lập";
tinhhe[4][2] = "Thiên tướng Mão Dậu chính trực / tuần tư";
tinhhe[4][3] = "Cơ Lương Thìn Tuất tiêm khắc / minh đoạn";

var pp = new Array(12);
for (i = 1; i < 13; i++)
    pp[i] = new Array(12);

var size = Math.min(screen.width / 1200, 1);

var tue = new Array();
tue[1] = "Thái Tuế";
tue[2] = "Hối Khí ";
tue[3] = "Tang Môn";
tue[4] = "Thiếu Âm";
tue[5] = "Quan Phù";
tue[6] = "Tử Phù";
tue[7] = "Tuế Phá";
tue[8] = "Long Đức";
tue[9] = "Bạch Hổ";
tue[10] = "Thiên Đức";
tue[11] = "Điếu Khách";
tue[12] = "Trực Phù";

var nh = new Array(11);
for (i = 1; i < 13; i++)
    nh[i] = new Array(12);

nh[1][1] = nh[2][2] = "Hải Trung Kim";
nh[3][3] = nh[4][4] = "Lư Trung Hỏa";
nh[5][5] = nh[6][6] = "Đại Lâm Mộc";
nh[7][7] = nh[8][8] = "Lộ Bàng Thổ";
nh[9][9] = nh[10][10] = "Kiếm Phong Kim";
nh[1][11] = nh[2][12] = "Sơn Đầu Hỏa";
nh[3][1] = nh[4][2] = "Giản Hạ Thủy";
nh[5][3] = nh[6][4] = "Thành Đầu Thổ";
nh[7][5] = nh[8][6] = "Bạch Lạp Kim";
nh[9][7] = nh[10][8] = "Dương Liễu Mộc";
nh[1][9] = nh[2][10] = "Tinh Tuyền Thủy";
nh[3][11] = nh[4][12] = "Ốc Thượng Thổ";
nh[5][1] = nh[6][2] = "Tích Lịch Hỏa";
nh[7][3] = nh[8][4] = "Tùng Bách Mộc";
nh[9][5] = nh[10][6] = "Trường Lưu Thủy";
nh[1][7] = nh[2][8] = "Sa Trung Kim";
nh[3][9] = nh[4][10] = "Sơn Hạ Hỏa";
nh[5][11] = nh[6][12] = "Bình Địa Mộc";
nh[7][1] = nh[8][2] = "Bích Thượng Thổ";
nh[9][3] = nh[10][4] = "Kim Bá Kim";
nh[1][5] = nh[2][6] = "Phú Đăng Hỏa";
nh[3][7] = nh[4][8] = "Thiên Hà Thủy";
nh[5][9] = nh[6][10] = "Đại Dịch Thổ";
nh[7][11] = nh[8][12] = "Thoa Xuyến Kim";
nh[9][1] = nh[10][2] = "Tang Đố Mộc";
nh[1][3] = nh[2][4] = "Đại Khuê Thủy";
nh[3][5] = nh[4][6] = "Sa Trung Thổ";
nh[5][7] = nh[6][8] = "Thiên Thượng Hỏa";
nh[7][9] = nh[8][10] = "Thạch Lựu Mộc";
nh[9][11] = nh[10][12] = "Đại Hải Thủy";

var sizesize;

var id_thaitue = 1;
var id_tapdieu = 1;
var id_tuongtinh = 1;
var ID_LUUNHAT = 1;
var ID_LUUTHOI = 1;
var id_luunien = 0;
var id_luunguyet = 0;
var id_luudaivan = 0;

var temppp;
var id_phieuphieu = 0;
var id_vdttl = 0;
var id_vdttlhl = 0;
var ID_VEPHIEUPHIEU;
var id_diaban = 0;

var id_phieuphieuvan = 0;

var m;
var mm;
var dd;
var y;
var yy;
var a;
var muigio = 7;
var jd;
var flag = new Array();
var flug = new Array();
var flg = new Array();
var phiky = new Array();
var philoc = new Array();
var ctieuvan = new Array();
var chitieuvan = new Array();
var timeZone = 7;
var nx;

var phutxem;

var cantang = new Array(12);

for (var i = 1; i <= 12; i++)
    cantang[i] = new Array(3);

for (var i = 1; i <= 12; i++)
    for (var j = 0; j <= 3; j++)
        cantang[i][j] = 0;

cantang[1][0] = 1;
cantang[1][1] = 10;
cantang[10][0] = 1;
cantang[10][1] = 8;

cantang[4][0] = 1;
cantang[4][1] = 2;
cantang[7][0] = 2;
cantang[7][1] = 4;
cantang[7][2] = 6;

cantang[2][0] = 3;
cantang[2][1] = 6;
cantang[2][3] = 8;
cantang[2][2] = 10;

cantang[3][0] = 3;
cantang[3][1] = 1;
cantang[3][3] = 3;
cantang[3][2] = 5;

cantang[5][0] = 3;
cantang[5][1] = 5;
cantang[5][3] = 10;
cantang[5][2] = 2;

cantang[6][0] = 3;
cantang[6][1] = 3;
cantang[6][3] = 5;
cantang[6][2] = 7;

cantang[8][0] = 3;
cantang[8][1] = 6;
cantang[8][3] = 2;
cantang[8][2] = 4;

cantang[9][0] = 3;
cantang[9][1] = 7;
cantang[9][3] = 9;
cantang[9][2] = 5;
cantang[11][0] = 3;
cantang[11][1] = 5;
cantang[11][3] = 4;
cantang[11][2] = 8;

cantang[12][0] = 2;
cantang[12][1] = 9;
cantang[12][2] = 1;



var tennguoi;
var gioitinh;
//DL
var ngaydl;
var thangdl;
var namdl;
var giodl;

//AL

var nam, gio;
var ngay;
var thang;
var gio;
var dvtutrunam;

var cannam, chinam, canthang, chithang, canngay, chingay, cangio, chigio;
var thangtk; //CAN CHI

var canthangtk, chithangtk;
//==========================năm xem===============================


var jd, jdxem;

//DL
var ngayxemdl;
var thangxemdl;
var namxemdl;
var gioxemdl;

//DL
// var ngayxemdl = parseInt(document.getElementById('ID_LUUNHATDL').value);
//  var thangxemdl = parseInt(document.getElementById('ID_THANGXEMDL').value);
//var namxemdl = parseInt(document.getElementById('ID_NAMXEM').value);
//var gioxemdl = parseInt(document.getElementById('ID_GIOXEM').value);


var phutdl;

//AL

var namxem, gioxem;
var thangxem;
var ngayxem;
var nhuan, nhuanxem;
var thu, thuxem;
//CAN CHI

var cannamxem, chinamxem, canthangxem, chithangxem, canngayxem, chingayxem, cangioxem, chigioxem;
var thangxemtk; //CAN CHI

var canthangxemtk, chithangxemtk;
var canthai;
var chithai;

var acan = new Array();

var achi = new Array();

function toggle() {
    var ele = document.getElementById("toggleText");
    var text = document.getElementById("displayText");
    if (ele.style.display == "block") {
        ele.style.display = "none";
        text.innerHTML = "Nhập thêm sao";
    } else {
        ele.style.display = "block";
        text.innerHTML = "Không nhập thêm sao";
    }
}

function openTCP() {
    var ele = document.getElementById("toggleTCP");
    var text = document.getElementById("displayTCP");
    if (ele.style.display == "block") {
        ele.style.display = "none";
        text.innerHTML = "Nhập thêm sao";
    } else {
        ele.style.display = "block";
        text.innerHTML = "Không nhập thêm sao";
    }

}

function openTCP1() {
    var ele = document.getElementById("toggleTCP1");
    var text = document.getElementById("displayTCP1");
    if (ele.style.display == "block") {
        ele.style.display = "none";
        text.innerHTML = "Nhập thêm sao";
    } else {
        ele.style.display = "block";
        text.innerHTML = "Không nhập thêm sao";
    }

}

function openTCP2() {
    var ele = document.getElementById("toggleTCP2");
    var text = document.getElementById("displayTCP2");
    if (ele.style.display == "block") {
        ele.style.display = "none";
        text.innerHTML = "Nhập thêm sao";
    } else {
        ele.style.display = "block";
        text.innerHTML = "Không nhập thêm sao";
    }
}

function openTCP3() {
    var ele = document.getElementById("SuuMui");
    var text = document.getElementById("displayTCP2");
    if (ele.style.display == "block") {
        ele.style.display = "none";
        text.innerHTML = "Nhập thêm sao";
    } else {
        ele.style.display = "block";
        text.innerHTML = "Không nhập thêm sao";
    }
}

function openTCP4() {
    var ele = document.getElementById("MaoDau");
    var text = document.getElementById("displayTCP2");
    if (ele.style.display == "block") {
        ele.style.display = "none";
        text.innerHTML = "Nhập thêm sao";
    } else {
        ele.style.display = "block";
        text.innerHTML = "Không nhập thêm sao";
    }
}

function openTCP5() {
    var ele = document.getElementById("ThinTuat");
    var text = document.getElementById("displayTCP2");
    if (ele.style.display == "block") {
        ele.style.display = "none";
        text.innerHTML = "Nhập thêm sao";
    } else {
        ele.style.display = "block";
        text.innerHTML = "Không nhập thêm sao";
    }
}

function openTCP6() {
    var ele = document.getElementById("TiHoi");
    var text = document.getElementById("displayTCP2");
    if (ele.style.display == "block") {
        ele.style.display = "none";
        text.innerHTML = "Nhập thêm sao";
    } else {
        ele.style.display = "block";
        text.innerHTML = "Không nhập thêm sao";
    }
}

function openTCP7() {
    var ele = document.getElementById("DanThan");
    var ele1 = document.getElementById("TiHoi");
    var text = document.getElementById("displayTCP2");
    if (ele.style.display == "block") {
        ele.style.display = "none";
        text.innerHTML = "Nhập thêm sao";

    } else {
        ele.style.display = "block";
        text.innerHTML = "Không nhập thêm sao";

        ele1.style.display = "none";
    }
}

function openTCP8() {
    var ele = document.getElementById("PhiHoa");
    var text = document.getElementById("displayTCP2");
    if (ele.style.display == "block") {
        ele.style.display = "none";
        text.innerHTML = "Nhập thêm sao";

    } else {
        ele.style.display = "block";
        text.innerHTML = "Không nhập thêm sao";

    }
}

function resize() {
    if (trinhan == 1)
        bacot();
    if (trinhan == 3)
        haicot(size, 0, 0);

}

document.addEventListener("DOMContentLoaded", init, false);

function init() {
    var canvas = document.getElementById("canvasImg");
    canvas.addEventListener("mousedown", getPosition, false);
}

function getPosition(event) {
    var xy = new Array();
    var x = new Number();
    var y = new Number();
    var canvas = document.getElementById("canvasImg");

    if (event.x != undefined && event.y != undefined) {
        x = event.x;
        y = event.y + 900;
    } else // Firefox method to get the position
    {
        x = event.clientX + document.body.scrollLeft +
            document.documentElement.scrollLeft;
        y = event.clientY + document.body.scrollTop +
            document.documentElement.scrollTop;
    }

    x -= canvas.offsetLeft;
    y -= canvas.offsetTop;
    xy[0] = x;
    xy[1] = y; //alert(xy);
    return (xy);
}

function ShowHideObject(obj) {
    document.getElementById('idLich_1').style.display = 'none';
    document.getElementById('idLich_0').style.display = 'none';
    document.getElementById('idLich_' + obj).style.display = 'block';
    setup();
}

/* Convert a lunar date to the corresponding solar date */

function ngaygioxem() {
    var dd = new Date();

    var m_in = dd.getMonth() + 1;
    var y_in = dd.getFullYear();
    var d_in = dd.getDate();
    var h_in = Math.floor(dd.getHours() * 0.5);
    var z_in = (-1) * Math.floor((dd.getTimezoneOffset()) / 60); /// c?n ch򠽠gi? T񮯍


    var amlich = convertSolar2Lunar(d_in, m_in, y_in, 7.0);
    var ngay = parseInt(amlich[0]);
    var thang = parseInt(amlich[1]);
    var namAm = parseInt(amlich[2]);
    var nhuan = parseInt(amlich[3]);
    alert("Hôm nay là ngày " + d_in + " tháng " + m_in + " năm " + y_in + " Dương Lịch, tức là ngày " + ngay + " tháng " + thang + " năm " + namAm + " Âm Lịch, tại múi giờ số " + z_in);
    return false;
}

function zoomin() {
    size = size * 0.9576032806;
    bacot();
}

function zoomout() {
    size = size * 1.044273782;
    bacot();
}

function zoominlv() {
    size = size * 0.9576032806;
    lieuvo(size, 0, 0);
}

function zoomoutlv() {
    size = size * 1.044273782;
    lieuvo(size, 0, 0);
}

function zoominhaicot() {
    size = size * 0.9576032806;
    haicot(size, 0, 0);
}

function zoomouthaicot() {
    size = size * 1.044273782;
    haicot(size, 0, 0);
}

function color() {
    context.fillStyle = 'black';
}