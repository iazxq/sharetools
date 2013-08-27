var temp;
function S_Code(){
        var address = document.form1.url.value;
        var op_tool  = (document.form1.tool.checked== true)  ?"toolbar=1,":"";
        var op_loc = (document.form1.loc.checked == true)  ?"location=1,":"";
        var op_link  = (document.form1.link.checked == true)  ? "directories==1," :"";
        var op_stat  = (document.form1.stat.checked == true)  ?"status=1," :"";
        var op_menu  = (document.form1.menu.checked == true)  ? "menubar=1,":"";
        var op_scroll  = (document.form1.scroll.checked == true)  ?"scrollbars=1," :"";
        var op_resize  = (document.form1.resize.checked == true)  ?"resizable=1,":"";
        var op_selfopen = (document.form1.selfopen.checked==true)?"_self":"newwindow";
        var op_width  = (document.form1.width.value !="")?"width="+document.form1.width.value+",":"";
        var op_heigh = (document.form1.heigh.value!="")?"heigh="+document.form1.heigh.value+",":"";
        var op_L  = (document.form1.L.value)?"left="+document.form1.L.value+",":"";
        var op_T = (document.form1.T.value)?"top="+document.form1.T.value +",":"";
if (op_tool =="" && op_loc=="" && op_link =="" && op_stat=="" && op_menu =="" && op_scroll=="" &&op_resize=="" && op_width=="" && op_heigh=="" && op_L=="" && op_T==""){
tempopenstyle="";
}else{
tempopenstyle=",'" + op_width + op_heigh + op_L + op_T + op_tool  + op_loc + op_link + op_stat + op_menu + op_scroll + op_resize;
tempopenstyle=tempopenstyle.substring(0,tempopenstyle.length-1);
tempopenstyle=tempopenstyle+"'";
}
temp="window.open('" + address +"','" + op_selfopen + "'" + tempopenstyle + ")"
}