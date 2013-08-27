ie = (document.all)? true:false 
if (ie){ 
function ctlent(eventobject){if(event.ctrlKey && window.event.keyCode==13){convert();}} 
} 
var tblChars = [['┏','┓','┗','┛','┯','┷','┃','│', '━'],
				['╔','╗','╚','╝','╤','╧','║','│', '═'],
				['╔','╗','╚','╝','╤','╧','║','┆', '═'],
				['╔','╗','╚','╝','╤','╧','║','↓', '═'],
				['╔','╗','╚','╝','╤','╧','║','↑', '═'],
				['╃','╄','╁','╆ ','┬','┴','║','│', '─'],
				['╔','╗','╚','╝','╤','╧','║','', '═'],
				['╔','╗','╚','╝','╤','╧','║','★', '═'],
				['╔','╗','╚','╝','●','●','║','┆', '○'],
				['┏','┓','┗','┛','▽','△','┃','┆', '━'],
				['╔','╗','╚','╝','⊕','◎','║','┆', '○'],
				['┏','┓','┗','┛','≈','≈','┃','┆', '≈'],
				['卐','卐','卐','卐','卐','卐','卐','┆', '卐'],
				['　','　','　','　','　','　','　','　', '　']];

var tblTemplet = 1;
var blankChar = '　';
var width=20;
var height=8;
function convert(){
	var s =document.getElementById("wz").value.toString();
	if(s.length == 0){
		document.getElementById("s").focus();
		alert("请首先输入要转换格式的文字。");
		return;
	}

	var ary = [];
	var i,j, index;
	var t = "";
	index = 0;
	width = document.getElementById("x").value * 1;
	height = document.getElementById("y").value * 1;
	tblTemplet = document.getElementById("tbl").value * 1;
	
	for(i=width*16; i>=0; i--){
		ary[i] = new Array();
	}
	while(index < s.length){
		for(i=width*2; i>=0; i--){
			for(j=0; j<=(height+1); j++){
				if( i == (width * 2)){
					if(j==0){
						ary[i][j] = tblChars[tblTemplet][1];
					}else if(j == (height + 1)){
						ary[i][j] = tblChars[tblTemplet][3];
					}else{
						ary[i][j] = tblChars[tblTemplet][6];
					}
				}else if( i== 0){
					if(j==0){
						ary[i][j] = tblChars[tblTemplet][0];
					}else if(j == (height + 1)){
						ary[i][j] = tblChars[tblTemplet][2];
					}else{
						ary[i][j] = tblChars[tblTemplet][6];
					}
				}else if( i % 2 == 0){
					if(j==0){
						ary[i][j] = tblChars[tblTemplet][4];
					}else if(j == (height + 1)){
						ary[i][j] = tblChars[tblTemplet][5];
					}else{
						ary[i][j] = tblChars[tblTemplet][7];
					}
				}else if(j == 0 || j == (height + 1)){
					ary[i][j] = tblChars[tblTemplet][8];
				}else{
					var c = getChar(s, index++);
					if (c == '\n' || c == '\r'){
						if(j == 1){
							j = 0;
							continue;
						}else{
							while(j<(height+1)){
								ary[i][j] = blankChar;
								j++;
							}
							j = height;
						}
					}else{
						ary[i][j] = c;
					}
				}
			}
		}
		for(j=0; j<=(height + 1); j++){
			for(i=0; i<=width*2; i++){
				t += ary[i][j];
			}
			t += "\r\n";
		}
	}

	t += "\r\n古文竖排格式由 脚本分享网在线小工具 " + document.location.href + " 生成！";
	document.getElementById("t").value = t;
}

var half = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','(',')','[',']','{','}','<','>','*','&','^','%','$','#','@','!','~','`','+','-','=','_','|','\\','\'','"',';',':','.',',','?','/',' ','（','）','【','】','《','》',"“","”"];
var full = ['０','１','２','３','４','５','６','７','８','９','ａ','ｂ','ｃ','ｄ','ｅ','ｆ','ｇ','ｈ','ｉ','ｊ','ｋ','ｌ','ｍ','ｎ','ｏ','ｐ','ｑ','ｒ','ｓ','ｔ','ｕ','ｖ','ｗ','ｘ','ｙ','ｚ','Ａ','Ｂ','Ｃ','Ｄ','Ｅ','Ｆ','Ｇ','Ｈ','Ｉ','Ｊ','Ｋ','Ｌ','Ｍ','Ｎ','Ｏ','Ｐ','Ｑ','Ｒ','Ｓ','Ｔ','Ｕ','Ｖ','Ｗ','Ｘ','Ｙ','Ｚ','︵','︶','︻','︼','︷','︸','︽','︾','＊','＆','︿','％','＄','＃','＠','！','～','｀','＋','－','＝','＿','｜','＼','＇','＂','；','：','。','，','？','／', blankChar,'︵','︶','︻','︼','︽','︾',"『","』"];


function getChar(s, index){
	if(index >= s.length){
		return blankChar;
	}
	var c = s.charAt(index);
	for(var i=0; i<half.length; i++){
		if(c == half[i]){
			c = full[i];
		}
	}
	return c;
}