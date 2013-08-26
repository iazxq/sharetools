//ASCII 转换 Unicode
function AsciiToUnicode() {

    if (document.getElementById('content').value == '') { 
	alert('文本框中没有代码！'); 
	return; 
	}
    document.getElementById('result').value = '';
	for (var i = 0; i < document.getElementById('content').value.length; i++)
	    result.value += '&#' + document.getElementById('content').value.charCodeAt(i) + ';';
	document.getElementById('content').focus();
}

//Unicode 转换 ASCII
function UnicodeToAscii() {
    var code = document.getElementById('content').value.match(/&#(\d+);/g);
	if (code == null) { 
	alert('文本框中没有合法的Unicode代码！'); document.getElementById('content').focus();
	return; 
	}
document.getElementById('result').value = '';
	for (var i=0; i<code.length; i++)
	    document.getElementById('result').value += String.fromCharCode(code[i].replace(/[&#;]/g, ''));
	document.getElementById('content').focus();
}
function preview() {
	var win = window.open();
	win.document.open('text/html', 'replace');
	win.document.writeln(document.getElementById('result').value);
	win.document.close();
}
