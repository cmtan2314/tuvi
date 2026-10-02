function tinhdiem(acan, achi) {//nhập tứ trụ, tính ra ngũ hành.
//Các bước chính



//1- Check xem các địa chi có hóa hợp hay không

		// 1.1 Phải có thiên can dẫn xuất. Nếu là bán tam hợp, hai chi phải liền nhau.


		// 1.2  in ra các can đã tàng. sau khi khử bì. 

//2-Check xem các can có chỗ dựa hay không

//Check xem các thiên can có hóa hợp hay không

//check xem 


	return [20, 60, 15, 55, 4];
}














// 4- Các function check để tính
{
	//4.1- Check tam hội Chi return ra can hóa hợp
	function checktamhoi(x, y, z) {
		var points = [check(x + 1), check(y + 1), check(z + 1)];
		points.sort(function (a, b) {
			return a - b
		});
		for (var i = 0; i < 3; i++)
			points[i] = points[i] - i;
		if (points[0] != points[1])
			return new Array(0, 0, 0, 0);
		else if (points[1] != points[2])
			return new Array(0, 0, 0, 0);
		else
			return points;
	}

	// 4.2 Check Tam Hợp Chi return ra can hóa hợp
	function checktamhop(x, y, z) {
		var points = [check(x), check(y), check(z)];
		points.sort(function (a, b) {
			return a - b
		});

		for (var i = 0; i < 3; i++)
			points[i] = check(points[i] - i * 4);
		if (points[0] != points[1])
			return new Array(0, 0, 0, 0);
		else if (points[1] != points[2])
			return new Array(0, 0, 0, 0);
		else {
			var temp = points[1];
			if (temp == 2)
				temp = 10;
			if (temp == 3)
				temp = 7;

			return new Array(temp, temp, temp, temp);
		};
	}
	// 4.3 Check Nhị Hợp Chi, return ra can hóa hợp
	function checknhihop(x, y) {
		var points = [check(x), check(y)];
		points.sort(function (a, b) {
			return a - b
		});

		if ((check(x + y) != 3) || (x == y))
			return 0;
		else
			if ((x == 2) || (y == 2))
				return 5;
			else
				if ((x == 3) || (y == 3))
					return 7;
				else
					if ((x == 4) || (y == 4))
						return 9;
					else
						if ((x == 5) || (y == 5))
							return 1;
						else
							if ((x == 6) || (y == 6))
								return 3;
							else
								if ((x == 7) || (y == 7))
									return 5;
	}
	//4.4 Check Xung Chi, return ra 1 chi.
	function checkxung(x, y) {
		if (check(x - y + 12) == 6)
			return x;
		else
			return 0;
	}
	function checknhihopcan(x, y) { // 4.5Check Nhị hợp can
		if (checkcan(x - y) == 5)
			return (checkcan(2 * y + 3));
		else
			return 0;
	}
}

//5-Các hàm chức năng

function roundRect(ctx, x, y, width, height, radius, fill, stroke) {
  if (typeof stroke == "undefined" ) {
    stroke = true;
  }
  if (typeof radius === "undefined") {
    radius = 5;
  }
  ctx.beginPath();
  ctx.moveTo(x + radius, y);
  ctx.lineTo(x + width - radius, y);
  ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
  ctx.lineTo(x + width, y + height - radius);
  ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
  ctx.lineTo(x + radius, y + height);
  ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
  ctx.lineTo(x, y + radius);
  ctx.quadraticCurveTo(x, y, x + radius, y);
  ctx.closePath();
  if (stroke) {
    ctx.stroke();
  }
  if (fill) {
    ctx.fill();
  }        
}
function curverec(a,b,c,d,r)
{
	var canvas = document.getElementById('myCanvas');
	var context = canvas.getContext('2d');
	context.closePath();context.beginPath();
	context.moveTo(a+r,b);
	context.globalAlpha = 1;

	context.arc(a+r,b+r,r,1*Math.PI,1.5*Math.PI);
	context.moveTo(a+r,b);
	context.lineTo(a+c-r,b);
	context.arc(a+c-r,b+r,r,1.5*Math.PI,2*Math.PI);
	context.moveTo(a+c,b+r);
	context.lineTo(a+c,b+d-r);
	context.arc(a+c-r,b+d-r,r,0*Math.PI,0.5*Math.PI);
	context.moveTo(a+c-r,b+d);
	
	context.lineTo(a+r,b+d);
	context.arc(a+r,b+d-r,r,0.5*Math.PI,1*Math.PI);
	context.moveTo(a,b+d-r);
	
	context.lineTo(a,b+r);	context.closePath();
	context.stroke();
	

}


function vekhung()
{
		var canvas = document.getElementById('myCanvas');
		var context = canvas.getContext('2d');
	var imageObj = new Image();	canvas.width = 1160;
	canvas.height = 1600;
	//	context.clearRect(0, 0, canvas.width, canvas.height);
	
		context.save();
		context.scale(800 * 0.001, 800 * 0.001);
		context.fillStyle = '#FFFFFA';
		//context.fillRect(5, 3, 1200, 1600);
		context.globalAlpha = 1;
	
		context.fillStyle = '#FFFFFA';
	context.fill();		
	context.closePath();
//	curverec(100, 300, 1190, 1600,80);
	roundRect(context,1,1,1180,1600,30,0,1) ;
		context.lineWidth = 1;
		context.strokeStyle = 'black';
		context.shadowColor = '#999';
		context.shadowBlur = 10;
		context.shadowOffsetX = 5;
		context.shadowOffsetY = 5;
		context.stroke();
		context.closePath();
	roundRect(context,1,1,1180,1600,30,0,1) ;
		context.fillStyle = '#FFFFFA';
		context.fill();
		context.lineWidth = 1;
		context.strokeStyle = 'black';
		context.shadowColor = '#999';
		context.shadowBlur = 0;
		context.shadowOffsetX = 0;
		context.shadowOffsetY = 0;
		context.stroke();
		context.closePath();
	//curverec(15,51,790,400,30);
	
		context.beginPath();
		context.rect(40, 40, 240, 160);
		context.fillStyle = '#FFFFFA';
		context.fill();
		context.lineWidth = 1;
		context.strokeStyle = 'black';
		context.shadowColor = '#999';
		context.shadowBlur = 10;
		context.shadowOffsetX = 5;
		context.shadowOffsetY = 5;
		context.stroke();
		context.closePath();
		context.rect(30, 540, w * 5, 130 + hh * 9);
		context.fillStyle = '#FFFFFA';
		context.fill();
		context.lineWidth = 1;
		context.strokeStyle = 'black';
		context.stroke();
		context.closePath();
		context.beginPath();
		context.moveTo(40, 70);
		context.lineTo(280, 70);
		context.shadowColor = '0';
		context.shadowBlur = 0;
		context.shadowOffsetX = 0;
		context.shadowOffsetY = 0;
		context.rect(30, 540, w * 5, 130 + hh * 9);
		context.fillStyle = '#FFFFFA';
		context.fill();

		context.lineWidth = 1;
		context.strokeStyle = 'black';
		context.stroke();
		context.closePath();
		context.beginPath();
		context.rect(40, 40, 240, 160);
		context.fillStyle = '#FFFFFA';
		context.fill();
		context.lineWidth = 1;
		context.strokeStyle = 'black';
		context.closePath();
		context.rect(30, 540, w * 5, 30);
		context.fillStyle = '#7D542A';
		context.fill();
		context.stroke();
		context.rect(30, 970, w * 4, 30);
		context.fillStyle = '#7D542A';
		context.fill();
		context.stroke();
		context.rect(30, 970 + 2 * hh, w * 4, 30);
		context.fillStyle = '#7D542A';
		context.fill();
		context.stroke();
		context.rect(30, 1170 + 2 * hh, w * 4, 30);
		context.fillStyle = '#7D542A';
		context.fill();
		context.stroke();
		context.strokeStyle = 'black';
		context.shadowColor = '#999';
		context.shadowBlur = 10;
		context.shadowOffsetX = 5;
		context.shadowOffsetY = 5;
		context.stroke();
		context.closePath();
		context.rect(30 + w * 5, 540, 30, hh * 10 + 30);
		context.fillStyle = '#7D542A';
		context.fill();
		context.stroke();
		context.fillStyle = '#FFFFFA';
		context.strokeStyle = 'black';
		context.shadowColor = '#999';
		context.shadowBlur = 0;
		context.shadowOffsetX = 0;
		context.shadowOffsetY = 0;
		context.stroke();
		context.closePath();
		context.rect(30 + w * 5, 540, 30, hh * 10 + 30);
		context.fillStyle = '#7D542A';
		context.fill();
		context.stroke();
		context.fillStyle = '#FFFFFA';
		context.globalAlpha = 0.5;
		context.beginPath();
		context.moveTo(30, 570);
		context.lineTo(30 + 5 * w + 30, 570);
		context.stroke();
		context.closePath();
		context.beginPath();
		context.moveTo(30, 570 + hh);
		context.lineTo(30 + 5 * w + 30, 570 + hh);
		context.stroke();
		context.closePath();
		context.beginPath();
		context.moveTo(30, 570 + 3 * hh);
		context.lineTo(30 + 5 * w + 30, 570 + 3 * hh);
		context.stroke();
		context.closePath();
		context.beginPath();
		context.moveTo(30, 680 + 8 * hh);
		context.lineTo(30 + 5 * w, 680 + 8 * hh);
		context.stroke();
		context.closePath();
		context.beginPath();
		context.moveTo(30, 680 + hh);
		context.lineTo(30 + 5 * w, 680 + hh);
		context.stroke();
		context.closePath();
		context.beginPath();
		context.moveTo(30, 680 + 8 * hh);
		context.lineTo(30 + 5 * w, 680 + 8 * hh);
		context.stroke();
		context.closePath();
		context.beginPath();
		context.moveTo(30, 680 + 4 * hh);
		context.lineTo(30 + 5 * w, 680 + 4 * hh);
		context.stroke();
		context.closePath();
		context.beginPath();
		context.moveTo(30, 770 + 5 * hh);
		context.lineTo(30 + 5 * w + 30, 770 + 5 * hh);
		context.stroke();
		context.closePath();
		context.beginPath();
		context.moveTo(30, 770 + 2 * hh);
		context.lineTo(30 + 5 * w + 30, 770 + 2 * hh);
		context.stroke();
		context.closePath();
		context.beginPath();
		context.moveTo(30 + w, 540);
		context.lineTo(30 + w, 570 + 10 * hh);
		context.stroke();
		context.closePath();
		context.beginPath();
		context.moveTo(30 + w * 2, 540);
		context.lineTo(30 + w * 2, 570 + 10 * hh);
		context.stroke();
		context.closePath();
		context.beginPath();
		context.moveTo(30 + w * 3, 540);
		context.lineTo(30 + w * 3, 570 + 10 * hh);
		context.stroke();
		context.closePath();
		context.beginPath();
		context.moveTo(30 + w * 4, 540);
		context.lineTo(30 + w * 4, 570 + 10 * hh);
		context.stroke();
		context.closePath();
	}
function arraysAreIdentical(arr1, arr2) {
	if (arr1.length !== arr2.length)
		return false;
	for (var i = 0, len = arr1.length; i < len; i++) {
		if (arr1[i] !== arr2[i]) {
			return false;
		}
	}
	return true;
}

function vongtruongsinhtutru(cantinh, chi) {
	if (cantinh == 1)
		p = 12;
	if (cantinh == 2)
		p = 7;
	if (cantinh == 3)
		p = 3;
	if (cantinh == 4)
		p = 10;
	if (cantinh == 5)
		p = 3;
	if (cantinh == 6)
		p = 10;
	if (cantinh == 7)
		p = 6;
	if (cantinh == 8)
		p = 1;
	if (cantinh == 9)
		p = 9;
	if (cantinh == 10)
		p = 4;
	var tstutru;
	if (cantinh % 2 == 1) {
		tstutru = check(chi - p + 13)
	} else {
		tstutru = check(-achi[2] + p + 13);
	}
	return tstutru;
}

function thapthan(can1, can2) {
	var temp = 2 * (INT((can2 - 1) * 0.5) - INT((can1 - 1) * 0.5));
	if (temp < 0)
		temp = temp + 10;
	if ((can2 - can1 + 10) % 2 != 0)
		temp = temp + 1;
	return temp;
}
function incantang(n, x, y, ccan1, than1, ccan2, than2, ccan3, than3) {
	var canvas = document.getElementById('myCanvas');
	var context = canvas.getContext('2d');
	if (n == 1) {
		g(ccan1);
		context.font = 'bold 12pt Arial';
		context.fillText(can[ccan1], x, y);
		context.font = '11pt Arial';
		context.fillText(than1, x, y + lineskip);
		context.fillText(ts[vongtruongsinhtutru(ccan1, achi[2])], x, y + 2 * lineskip);
	}
	if (n == 2) {
		g(ccan1);
		context.font = 'bold 12pt Arial';
		context.fillText(can[ccan1], x - 40, y);
		context.font = '11pt Arial';
		context.fillText(than1, x - 40, y + lineskip);
		context.fillText(ts[vongtruongsinhtutru(ccan1, achi[2])], x - 40, y + 2 * lineskip);
		g(ccan2);
		context.font = 'bold 12pt Arial';
		context.fillText(can[ccan2], x + 40, y);
		context.font = '11pt Arial';
		context.fillText(than2, x + 40, y + lineskip);
		context.fillText(ts[vongtruongsinhtutru(ccan2, achi[2])], x + 40, y + 2 * lineskip);
	}
	if (n == 3) {
		g(ccan1);
		context.font = 'bold 12pt Arial';
		context.fillText(can[ccan1], x - 70, y);
		context.font = '11pt Arial';
		context.fillText(than1, x - 70, y + lineskip);
		g(ccan2);
		context.fillText(ts[vongtruongsinhtutru(ccan1, achi[2])], x - 70, y + 2 * lineskip);
		g(ccan2);
		context.font = 'bold 12pt Arial';
		context.fillText(can[ccan2], x, y);
		context.font = '11pt Arial';
		context.fillText(than2, x, y + lineskip);
		context.fillText(ts[vongtruongsinhtutru(ccan2, achi[2])], x, y + 2 * lineskip);
		g(ccan3);
		context.font = 'bold 12pt Arial';
		context.fillText(can[ccan3], x + 70, y);
		context.font = '11pt Arial';
		context.fillText(than3, x + 70, y + lineskip);
		context.fillText(ts[vongtruongsinhtutru(ccan3, achi[2])], x + 70, y + 2 * lineskip);
	}
}

function nguhanhcan(x, y) {
	x = checkcan(x);
	y = checkcan(y);
	if (INT((x - 1) / 2) == INT((y - 1) / 2))
		return true;
	else
		return false; ;
}

function convertcan2nguhanh(x) {
	x = check(x);
	return INT((x + 1) / 2);
}






// 3- Các function An Thần Sát

function anthansat(sao, chi) {
	var canvas = document.getElementById('myCanvas');
	var context = canvas.getContext('2d');
	for (var i = 1; i <= 4; i++) {
		if (achi[i] == chi) {
			if (thansat[i] <4) 
				context.fillText(sao, (2 * i - 2) * 220 / 2 + 40, thansat[i] * lineskip + 800);
			else
			context.fillText(sao, (2 * i - 1) * 220 / 2 + 40, (thansat[i] -4)* lineskip + 800);
						thansat[i]++;
		}
	}
}
function ansaott(sao, i) {
	var canvas = document.getElementById('myCanvas');
	var context = canvas.getContext('2d');

			if (thansat[i] <4) 
				context.fillText(sao, (2 * i - 2) * 220 / 2 + 40, thansat[i] * lineskip + 800);
			else
			{	context.fillText(sao, (2 * i - 1) * 220 / 2 + 40, (thansat[i] -4)* lineskip + 800);}
						thansat[i]++;
		
	
}

function anthansatcan(sao, can) {
	var canvas = document.getElementById('myCanvas');
	var context = canvas.getContext('2d');
	for (var i = 1; i <= 4; i++) {
		if (acan[i] == can) {	if (thansat[i] <4) 
			context.fillText(sao, (2 * i - 2) * 220 / 2 + 40, thansat[i] * lineskip + 800);
			else
			context.fillText(sao, (2 * i - 1) * 220 / 2 + 40, (thansat[i] -4)* lineskip + 800);
			thansat[i]++;
		}
	}
}


function thienduc(x) {
	var day;
	switch (x) {
	case 1:
		anthansatcan("Thiên Đức", 4);
		break;
	case 2:
		anthansat("Thiên Đức", 9);
		break;
	case 3:
		anthansatcan("Thiên Đức", 9);
		break;
	case 4:
		anthansatcan("Thiên Đức", 8);
		break;
	case 6:
		anthansatcan("Thiên Đức", 1);
		break;
	case 12:
		anthansatcan("Thiên Đức", 7);
		break;
	case 7:
		anthansatcan("Thiên Đức", 10);
		break;
	case 5:
		anthansat("Thiên Đức", 12);
		break;
	case 9:
		anthansatcan("Thiên Đức", 3);
		break;
	case 10:
		anthansatcan("Thiên Đức", 2);
		break;
	case 8:
		anthansat("Thiên Đức", 3);
		break;
	case 11:
		anthansat("Thiên Đức", 6);
		break;

	}
}

function phuctinh(can) {
	var t = 0;
	switch (can) {
	case 1:
		t = 3;
		break;
	case 3:
		t = 1;
		break;
	case 2:
		t = 4;
		break;
	case 10:
		t = 2;
		break;
	case 5:
		t = 9;
		break;
	case 6:
		t = 8;
		break;
	case 4:
		t = 12;
		break;
	case 7:
		t = 7;
		break;
	case 8:
		t = 6;
		break;
	case 9:
		t = 5;
		break;
		return t;
	}

}
function kinhduong(can) {
	var t = 0;
	switch (can) {
	case 1:
		t = 4;
		break;
	case 2:
		t = 3;
		break;
	case 3:
		t = 7;
		break;
	case 4:
		t = 6;
		break;
	case 5:
		t = 7;
		break;
	case 6:
		t = 6;
		break;
	case 7:
		t = 10;
		break;
	case 8:
		t = 9;
		break;
	case 9:
		t = 1;
		break;
	case 10:
		t = 12;
		break;

	}
	return t;
}

function nguyetduc(chi) {
	var day;
	switch (chi) {
	case 1:
		anthansatcan("Nguyệt Đức", 9);
		break;
	case 5:
		anthansatcan("Nguyệt Đức", 9);
		break;
	case 9:
		anthansatcan("Nguyệt Đức", 9);
		break;
	case 3:
		anthansatcan("Nguyệt Đức", 3);
		break;
	case 7:
		anthansatcan("Nguyệt Đức", 3);
		break;
	case 10:
		anthansatcan("Nguyệt Đức", 3);
		break;

	case 12:
		anthansatcan("Nguyệt Đức", 1);
		break;
	case 4:
		anthansatcan("Nguyệt Đức", 1);
		break;
	case 8:
		anthansatcan("Nguyệt Đức", 1);
		break;
	}
}

function quocanquynhan(can) {
	var t = 0;
	switch (can) {
	case 1:
		t = 11;
		break;
	case 2:
		t = 12;
		break;
	case 3:
		t = 2;
		break;
	case 4:
		t = 3;
		break;
	case 5:
		t = 2;
		break;
	case 6:
		t = 3;
		break;
	case 7:
		t = 5;
		break;
	case 8:
		t = 6;
		break;
	case 9:
		t = 8;
		break;
	case 10:
		t = 9;
		break;

	}
	return t;
}

function thieny(thang) {
	var t = 0;
	switch (check(thang)) {
	case 1:
		t = 2;
		break;
	case 2:
		t = 3;
		break;
	case 3:
		t = 4;
		break;
	case 4:
		t = 5;
		break;
	case 5:
		t = 6;
		break;
	case 6:
		t = 7;
		break;
	case 7:
		t = 8;
		break;
	case 8:
		t = 9;
		break;
	case 9:
		t = 10;
		break;
	case 10:
		t = 11;
		break;
	case 11:
		t = 12;
		break;
	case 12:
		t = 1;
		break;

	}
	return t;
}
function kimdu(can) {
	var t = 0;
	switch (can) {
	case 1:
		t = 5;
		break;
	case 2:
		t = 6;
		break;
	case 3:
		t = 8;
		break;
	case 4:
		t = 9;
		break;
	case 5:
		t = 8;
		break;
	case 6:
		t = 9;
		break;
	case 7:
		t = 11;
		break;
	case 8:
		t = 12;
		break;
	case 9:
		t = 2;
		break;
	case 10:
		t = 3;
		break;

	}
	return t;
}
function ductu(chi) {
	var t = 0;
	var u = 0;
	switch (chi % 4) {

	case 3:
		anthansatcan("Đức Quý Nhân", 3);
		anthansatcan("Đức Quý Nhân", 4);
		anthansatcan("Tú Quý Nhân", 5);
		anthansatcan("Tú Quý Nhân", 10);
		break;
	case 1:
		anthansatcan("Đức Quý Nhân", 9);
		anthansatcan("Đức Quý Nhân", 10);
		anthansatcan("Đức Quý Nhân", 5);
		anthansatcan("Đức Quý Nhân", 6);
		anthansatcan("Tú Quý Nhân", 3);
		anthansatcan("Tú Quý Nhân", 8);
		anthansatcan("Tú Quý Nhân", 1);
		anthansatcan("Tú Quý Nhân", 6);
		break;
	case 2:
		anthansatcan("Đức Quý Nhân", 7);
		anthansatcan("Đức Quý Nhân", 8);
		anthansatcan("Tú Quý Nhân", 2);
		anthansatcan("Tú Quý Nhân", 7);
		break;
	case 0:
		anthansatcan("Đức Quý Nhân", 1);
		anthansatcan("Đức Quý Nhân", 2);
		anthansatcan("Tú Quý Nhân", 4);
		anthansatcan("Tú Quý Nhân", 9);
		break;

	}
	return t;
}
function anloc(i) {
	var l;
	if (i == 1)
		l = 3;
	if (i == 2)
		l = 4;
	if (i == 3)
		l = 6;
	if (i == 4)
		l = 7
			if (i == 5)
				l = 6;
			if (i == 6)
				l = 7;
			if (i == 7)
				l = 9;
			if (i == 8)
				l = 10;
			if (i == 9)
				l = 12;
			if (i == 10)
				l = 1;
			return l;
}

function coloan(a, b) {
	var coloan = new Array(2, 4, 8, 5, 5, 5, 9, 3);
	var coloanchi = new Array(6, 6, 12, 9, 3, 7, 1, 7)
		for (var i = 0; i < 4; i++)
			if (a == coloan[i])
				if (b == coloanchi[i]) {
					return 1;
				} else
					return 0;
}
function thienxa(a, b, j) {
	var thienxa = new Array(5, 1, 5, 1);
	var thienxachi = new Array(3, 7, 9, 1);
	for (var i = 0; i < 4; i++)
		if (a == thienxa[i])
			if (b == thienxachi[i])
				if (i == INT((j - 3) / 3)) {
					return 1;
				} else
					return 0;
}

function tuphe(a, b, j) {
	var tuphe = new Array(7, 8, 9, 10, 1, 2, 3, 4);
	var tuphechi = new Array(9, 10, 1, 12, 3, 4, 6, 7);
	for (var i = 0; i < 4; i++)
		if (a == tuphe[i])
			if (b == tuphechi[i])
				if (INT(i / 2) == INT((j - 3) / 3)) {
					return 1;
				} else
					return 0;
}

function ankhoiviet(tcannam, ch) {
	var tk;
	var tv;
	if (tcannam == 1) {
		tk = 6;
		tv = 12;
	} else
		if (tcannam == 5) {
			tk = 12;
			tv = 6;
		} else
			if (tcannam == 7) {
				tk = 12;
				tv = 6;
			} else
				if (tcannam == 2) {
					tk = 7;
					tv = 11;
				} else
					if (tcannam == 6) {
						tk = 11;
						tv = 7;
					} else
						if (tcannam == 3) {
							tk = 8;
							tv = 10;
						} else
							if (tcannam == 4) {
								tk = 10;
								tv = 8;
							} else
								if (tcannam == 8) {
									tk = 1;
									tv = 5;
								} else
									if (tcannam == 9) {
										tk = 2;
										tv = 4;
									} else
										if (tcannam == 10) {
											tk = 4;
											tv = 2;
										};
	anthansat(ch + " D. Quý nhân", tk);
	anthansat(ch + " A. Quý nhân", tv);
}
function khoicanh(x, y) {
	var a = new Array(x, y);
	var nt = new Array(9, 5);
	var ct = new Array(7, 11);
	var cth = new Array(7, 5);
	var mt = new Array(5, 11);
	if (arraysAreIdentical(a, nt) == true) {
		context.fillText("Khôi Canh QN", (2 * 3 - 2) * w / 2 + 40, thansat[3] * lineskip + 800);
		thansat[3]++;
	}
	if (arraysAreIdentical(a, ct) == true) {
		context.fillText("Khôi Canh QN", (2 * 3 - 2) * w / 2 + 40, thansat[3] * lineskip + 800);
		thansat[3]++;
	}
	if (arraysAreIdentical(a, cth) == true) {
		context.fillText("Khôi Canh QN", (2 * 3 - 2) * w / 2 + 40, thansat[3] * lineskip + 800);
		thansat[3]++;
	}
	if (arraysAreIdentical(a, mt) == true) {
		context.fillText("Khôi Canh QN", (2 * 3 - 2) * w / 2 + 40, thansat[3] * lineskip + 800);
		thansat[3]++;
	}
}

function kimthan(x, y, n) {
	var a = new Array(x, y);
	var nt = new Array(2, 2);
	var ct = new Array(6, 6);
	var cth = new Array(10, 10);

	if (arraysAreIdentical(a, nt) == true) {
		context.fillText("Kim Thần", (2 * n - 2) * w / 2 + 40, thansat[3] * lineskip + 800);
		thansat[3]++;
	}
	if (arraysAreIdentical(a, ct) == true) {
		context.fillText("Kim Thần", (2 * n - 2) * w / 2 + 40, thansat[3] * lineskip + 800);
		thansat[3]++;
	}
	if (arraysAreIdentical(a, cth) == true) {
		context.fillText("Kim Thần", (2 * n - 2) * w / 2 + 40, thansat[3] * lineskip + 800);
		thansat[3]++;
	}
}
function locton(can) {
	var t = 0;
	switch (can) {
	case 1:
		t = 3;
		break;
	case 2:
		t = 4;
		break;
	case 3:
		t = 6;
		break;
	case 4:
		t = 7;
		break;
	case 5:
		t = 6;
		break;
	case 6:
		t = 7;
		break;
	case 7:
		t = 9;
		break;
	case 8:
		t = 10;
		break;
	case 9:
		t = 12;
		break;
	case 10:
		t = 1;
		break;

	}
	return t;
}
function tuquanhocduong() {}
function tamky(a, b, c) {
	var tk = "0";
	if (a == 1)
		if (b == 5)
			if (c == 7)
				tk = "Thiên Tam Kỳ";
	if (a == 2)
		if (b == 3)
			if (c == 4)
				tk = "Địa Tam Kỳ";
	if (a == 9)
		if (b == 10)
			if (c == 8)
				tk = "Nhân Tam Kỳ";
	return tk;
}
function vanxuongquynhan(can) {
	var t = 0;
	switch (can) {
	case 1:
		t = 6;
		break;
	case 2:
		t = 7;
		break;
	case 3:
		t = 6;
		break;
	case 4:
		t = 7;
		break;
	case 5:
		t = 9;
		break;
	case 6:
		t = 10;
		break;
	case 7:
		t = 12;
		break;
	case 8:
		t = 1;
		break;
	case 9:
		t = 3;
		break;
	case 10:
		t = 4;
		break;

	}
	return t;
}
function thaicuc(x) {
	var day;
	switch (x) {
	case 1:
		day = 1;
		break;
	case 2:
		day = 7;
		break;
	case 3:
		day = 10;
		break;
	case 4:
		day = 4;
		break;
	case 5:
		day = "tuquy";
		break;
	case 6:
		day = "tuquy";
		break;
	case 7:
		day = 3;
		break;
	case 8:
		day = 12;
		break;
	case 9:
		day = 6;
		break;
	case 10:
		day = 9;
		break;
	}
	return day;
}
