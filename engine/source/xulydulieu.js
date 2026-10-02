
//==========================================Nam sinh===============
function getdata() {
    list = document.getElementById('ID_CANNAMTHEM');
    for (var i = 0; i < list.options.length; ++i) {
        if (list.options[i].selected)
            cannamthem = parseInt(list.options[i].value);
    }
    list = document.getElementById('ID_CANNAMTHEM1');
    for (var i = 0; i < list.options.length; ++i) {
        if (list.options[i].selected)
            cannamthem1 = parseInt(list.options[i].value);
    }

    tennguoi = document.getElementById('ID_TEN').value;
    list = document.getElementById('ID_PHUTDL');
    for (var i = 0; i < list.options.length; ++i) {
        if (list.options[i].selected)
            phutdl = parseInt(list.options[i].value);
    }

    list = document.getElementById('ID_GIOITINH');
    for (var i = 0; i < list.options.length; ++i) {
        if (list.options[i].selected)
            gioitinh = parseInt(list.options[i].value);
    }

    //DL
    ngaydl = parseInt(document.getElementById('ID_NGAYDL').value);
    thangdl = parseInt(document.getElementById('ID_THANGDL').value);
    namdl = parseInt(document.getElementById('ID_NAMDL').value);
    giodl = parseInt(document.getElementById('ID_GIODL').value);

    //AL

    nam = parseInt(document.getElementById('ID_NAM').value);
    ngay = parseInt(document.getElementById('ID_NGAY').value);
    thang = parseInt(document.getElementById('ID_THANG').value);
    if (!document.getElementById('ID_NHUAN').checked)
        nhuan = 0;
    else
        nhuan = 1;
    gio = check(parseInt(document.getElementById('ID_GIO').value));

    //CAN CHI


    //==========================năm xem===============================


    //DL
    // var ngayxemdl = parseInt(document.getElementById('ID_LUUNHATDL').value);
    //  var thangxemdl = parseInt(document.getElementById('ID_THANGXEMDL').value);
    //var namxemdl = parseInt(document.getElementById('ID_NAMXEM').value);
    //var gioxemdl = parseInt(document.getElementById('ID_GIOXEM').value);

    namxem = parseInt(document.getElementById('ID_NAMXEM').value);
    thangxem = parseInt(document.getElementById('ID_THANGXEM').value);
    ngayxem = parseInt(document.getElementById('ID_NGAYXEM').value);
    gioxem = parseInt(document.getElementById('ID_GIOXEM').value);
    gioxemdl = gioxem
    if (!document.getElementById('ID_THANGXEMNHUAN').checked)
        nhuanxem = 0;
    else
        nhuanxem = 1;

    //CAN CHI


}

function convertfromDL(ngaydl, thangdl, namdl, giodl) {
    // return new Array(lunarDay, lunarMonth, lunarYear, lunarLeap);
    var lunar = convertSolar2Lunar(ngaydl, thangdl, namdl, 7);
    ngay = lunar[0];
    thang = lunar[1];
    nam = lunar[2];
    nhuan = lunar[3];
}

function convertfromAL(ngay, thang, nam, nhuan, timeZone) {
    // function convertLunar2Solar(lunarDay, lunarMonth, lunarYear, lunarLeap, timeZone)

    var solar = convertLunar2Solar(ngay, thang, nam, nhuan, timeZone);
    ngaydl = solar[0];
    thangdl = solar[1];
    namdl = solar[2];
}

function sync() {
    if (document.getElementById("ID_LICH").value == 1) {

        document.getElementById('ID_NGAY').selectedIndex = 0;
        document.getElementById('ID_NGAY').value = ngay;
        document.getElementById('ID_THANG').value = thang;
        document.getElementById("ID_NAM").selectedIndex = 0;
        document.getElementById("ID_NAM").value = nam;
        document.getElementById("ID_GIO").selectedIndex = 0;

        document.getElementById('ID_GIO').value = gio;
    }

    if (document.getElementById("ID_LICH").value == 0) {

        document.getElementById('ID_NGAYDL').selectedIndex = 0;
        document.getElementById('ID_NGAYDL').value = ngaydl;
        document.getElementById('ID_THANGDL').value = thangdl;
        document.getElementById("ID_NAMDL").selectedIndex = 0;
        document.getElementById("ID_NAMDL").value = namdl;
        document.getElementById("ID_GIODL").selectedIndex = 0;

        document.getElementById('ID_GIODL').value = giodl;
    }
}

// nếu nhập là DL.
function setup() {
    getdata();
    if (document.getElementById("ID_LICH").value == 0) {

        var solar = convertLunar2Solar(ngay, thang, nam, nhuan, 7);
        ngaydl = solar[0];
        thangdl = solar[1];
        namdl = solar[2];
        giodl = 2 * gio - 2;

    }

    // if(document.getElementById("ID_LICH").value==1)
    {
        convertfromDL(ngaydl, thangdl, namdl, giodl);
        var jd = jdFromDate(ngaydl, thangdl, namdl);
        canngay = checkcan(jd);
        chingay = check(jd + 2);
        gio = check(INT((giodl + 1) / 2 + 1));

        chigio = check(1 + INT((giodl + 1) / 2));
        cangio = checkcan(2 * canngay + chigio - 2);
        thu = jd % 7; thu++;
        cannam = checkcan(nam - 1983 + 360);
        chinam = check(nam - 1983 + 360);
        chithang = check(thang + 2);
        canthang = checkcan(cannam * 2 + thang);

        var jd1 = jdAtVST(ngaydl, thangdl, namdl, giodl, 7);
        var sl = solarLongitude(jd1);
        sl = sl - 315;
        if (sl < 30)
            sl = sl + 360;
        thangtk = check(INT(sl / 30) + 1);
        canthangtk = checkcan(2 * cannam + thangtk);
        chithangtk = check(thangtk + 2);

        function tinhthangtk(jdtemp) {
            var sl = solarLongitude(jdtemp - 0.5 + (giodl - 7) / 24.0 + phutdl / 1440.0) - 315;
            if (sl < 30)
                sl = sl + 360;
            return check(INT(sl / 30) + 1);
        }
        //alert(jd);

        var jdsau = jd;
        var jdtruoc = jd;
        while (tinhthangtk(jdsau) == tinhthangtk(jd))
            jdsau++;
        while (tinhthangtk(jdtruoc) == tinhthangtk(jd))
            jdtruoc--;
        jdtruoc++;
        //alert(jdsau-jd+" "+(jd-jdtruoc)+" ");
        //alert (jd+" "+tinhthangtk(jd)+" "+jdsau+" "+tinhthangtk(jdsau)+" "+jdtruoc+" "+tinhthangtk(jdtruoc)+" ");
        dvtutrunam = jdsau - jd;
        dvtutrunu = jd - jdtruoc;

        //  alert("Dương Lịch "+namdl+" "+thangdl+" "+ngaydl+" "+giodl+" "+"Âm Lịch "+nam+" "+thang+" "+ngay+" "+giodl+" nhuận "+nhuan+ " Can Chi năm"+cannam+" "+chinam+" can chi tháng "+canthang+" "+chithang+" can chi ngày "+ canngay+" " +chingay+" can chi giờ "+cangio+" "+chigio+" tiết khí tháng "+ thangtk+ " "+canthangtk+" " +chithangtk+ " thứ"+ jd%7+" giới tính "+gioitinh);
        var solarxem = convertLunar2Solar(ngayxem, thangxem, namxem, nhuanxem, 7);
        ngayxemdl = solarxem[0];
        thangxemdl = solarxem[1];
        namxemdl = solarxem[2];
        chigioxem = check(INT((gioxem + 1) / 2)+1);		

        var jdxem = jdFromDate(ngayxemdl, thangxemdl, namxemdl);
        canngayxem = checkcan(jdxem );
        chingayxem = check(jdxem + 2);
	

        cangioxem = checkcan(2 * canngayxem + chigioxem - 2);
        thuxem = (jdxem+1) % 7;
		thuxem++;
        cannamxem = checkcan(namxem - 183 );
        chinamxem = check(namxem - 183 );
        chithangxem = check(thangxem + 2);
        canthangxem = checkcan(cannamxem * 2 + thangxem);

        var jd1xem = jdAtVST(ngayxemdl, thangxemdl, namxemdl, gioxem, 7);
        var slxem = solarLongitude(jd1xem);
        slxem = slxem - 315;
        if (slxem < 30)
            slxem = slxem + 360;
        thangxemtk = check(INT(sl / 30) + 1);
        canthangxemtk = checkcan(2 * cannamxem + thangxemtk);
        chithangxemtk = check(thangxemtk + 2);

    }

    var cannamtk = cannam;
    var chinamtk = chinam;
    if (chithangtk == 12)
        if (chithang == 1) {
            cannamtk = checkcan(cannam - 1);
            chinamtk = check(chinam - 1);
        }

    canthai = checkcan(canthangtk + 1);
    chithai = check(chithangtk + 3);
    achi[1] = chinamtk;
    achi[2] = chithangtk;
    achi[3] = chingay;
    achi[4] = chigio;
    achi[5] = chithai;
	achi[6]=check(16-achi[2]+1-achi[4]);

    acan[1] = cannamtk;
    acan[2] = canthangtk;
    acan[3] = canngay;
    acan[4] = cangio;
    acan[5] = canthai;

    sync();
    id_diaban = 0;
	if (namxem>nam-1)
	{
    document.getElementById('canvasImg').src = bacot();

    id_diaban = 1;
    document.getElementById('canvasImg2').src = bacot();
    id_diaban = 2; //nhân bàn
    document.getElementById('canvasImg3').src = bacot();
    document.getElementById('canvasImg4').src = tutru();
	}
}