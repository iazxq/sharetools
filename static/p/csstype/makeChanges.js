/*******************************************************/
/* JavaScript by Tristan Emerson                       */
/* For csstypeset.com                                  */
/* Dec. 31, 2007 (instead of drinking)                 */
/*******************************************************/

/*Onload!*/
function load(){
  initCSS();
  checkVersion();
}

function checkVersion(){
  var browser = BrowserDetect.browser;
  var version = BrowserDetect.version;
  
  switch(browser){
    case "Explorer":
      if(version < 7) noSupport("Internet Explorer " + version);
      break;
    case "Safari":
      if(version < 500) noSupport("Safari build " + version); 
  }
}

function delSelects(){
  var sel = document.getElementById('fontSel');
  sel.parentElement.removeChild(sel);
  sel = document.getElementById('measure');
  sel.parentElement.removeChild(sel);
  sel = document.getElementById('color');
  sel.parentElement.removeChild(sel);
}

/*Sets the font family*/
function setFontFamily(fontFamily){
  document.getElementById('textInput').style.fontFamily = fontFamily;
  document.getElementById('textInputViewer').style.fontFamily = fontFamily;
  setCSS();
}

/*Sets the font size*/
function setFontSize(){
  var selectTag = document.getElementById('measure');
  
  var fontSize = document.getElementById('fontSize').value;
  var units = selectTag[selectTag.selectedIndex].value;
  document.getElementById('textInput').style.fontSize = fontSize + units;
  document.getElementById('textInputViewer').style.fontSize = fontSize + units;
  setCSS();
}

/*Toggles Bold*/
function bold(){
  var input = document.getElementById('textInput');
  var styleView = document.getElementById('textInputViewer');
  var bold = document.getElementById('bold');
  if(bold.src.match('bold.gif')){
    bold.src = './static/p/csstype/bold_a.gif';
    input.style.fontWeight += 'bold';
    styleView.style.fontWeight += 'bold';
  }else{
    bold.src = './static/p/csstype/bold.gif';
    input.style.fontWeight = input.style.fontWeight.replace('bold','');
    styleView.style.fontWeight = input.style.fontWeight;
  }
  setCSS();
}

/*Toggles Italic*/
function italic(){
  var input = document.getElementById('textInput');
  var styleView = document.getElementById('textInputViewer');
  var italic = document.getElementById('italic');
  if(italic.src.match('italic.gif')){
    italic.src = './static/p/csstype/italic_a.gif';
    input.style.fontStyle += 'italic';
    styleView.style.fontStyle += 'italic';
  }else{
    italic.src = './static/p/csstype/italic.gif';
    input.style.fontStyle = input.style.fontStyle.replace('italic','');
    styleView.style.fontStyle = styleView.style.fontStyle.replace('italic','');
  }
  setCSS();
}

/*Toggles Underline*/
function uline(){
  var input = document.getElementById('textInput');
  var styleView = document.getElementById('textInputViewer');
  var uline = document.getElementById('uline');
  if(uline.src.match('uline.gif')){
    uline.src = './static/p/csstype/uline_a.gif';
    input.style.textDecoration = 'underline';
    styleView.style.textDecoration = 'underline';
    document.getElementById('sthrough').src = './static/p/csstype/sthrough.gif';
  }else{
    uline.src = './static/p/csstype/uline.gif';
    input.style.textDecoration = '';
    styleView.style.textDecoration = '';
  }
  setCSS();
}

/*Toggles Line-Through*/
function sthrough(){
  var input = document.getElementById('textInput');
  var styleView = document.getElementById('textInputViewer');
  var sthrough = document.getElementById('sthrough');
  if(sthrough.src.match('sthrough.gif')){
    sthrough.src = './static/p/csstype/sthrough_a.gif';
    input.style.textDecoration = 'line-through';
    styleView.style.textDecoration = 'line-through';
    document.getElementById('uline').src = './static/p/csstype/uline.gif';
  }else{
    sthrough.src = './static/p/csstype/sthrough.gif';
    input.style.textDecoration = '';
    styleView.style.textDecoration = '';
  }
  setCSS();
}

/*Toggles all caps*/
function allcaps(){
  var input = document.getElementById('textInput');
  var styleView = document.getElementById('textInputViewer');
  var allcaps = document.getElementById('allcaps');
  if(allcaps.src.match('allcaps.gif')){
    allcaps.src = './static/p/csstype/allcaps_a.gif';
    input.style.textTransform = 'uppercase';
    input.style.fontVariant = '';
    styleView.style.textTransform = 'uppercase';
    styleView.style.fontVariant = '';
    document.getElementById('smallcaps').src = './static/p/csstype/smallcaps.gif';
  }else{
    allcaps.src = './static/p/csstype/allcaps.gif';
    input.style.textTransform = '';
    styleView.style.textTransform = '';
  }
  setCSS();
}

/*Toggles small caps*/
function smallcaps(){
  var input = document.getElementById('textInput');
  var styleView = document.getElementById('textInputViewer');
  var smallcaps = document.getElementById('smallcaps');
  if(smallcaps.src.match('allcaps.gif')){
    smallcaps.src = './static/p/csstype/smallcaps_a.gif';
    input.style.fontVariant = 'small-caps';
    input.style.textTransform = '';
    styleView.style.fontVariant = 'small-caps';
    styleView.style.textTransform = '';
    document.getElementById('allcaps').src = './static/p/csstype/allcaps.gif';
  }else{
    smallcaps.src = './static/p/csstype/smallcaps.gif';
    input.style.fontVariant = '';
    styleView.style.fontVariant = '';
  }
  setCSS();
}

/*Toggles Left align*/
function left(){
  var input = document.getElementById('textInput');
  var styleView = document.getElementById('textInputViewer');
  var left = document.getElementById('left');
  if(left.src.match('left.gif')){
    left.src = './static/p/csstype/left_a.gif';
    input.style.textAlign = 'left';
    styleView.style.textAlign = 'left';
    document.getElementById('right').src = './static/p/csstype/right.gif';
    document.getElementById('justify').src = './static/p/csstype/justify.gif';
    document.getElementById('center').src = './static/p/csstype/center.gif';
  }
  setCSS();
}

/*Toggles Center align*/
function center(){
  var input = document.getElementById('textInput');
  var styleView = document.getElementById('textInputViewer');
  var center = document.getElementById('center');
  if(center.src.match('center.gif')){
    center.src = './static/p/csstype/center_a.gif';
    input.style.textAlign = 'center';
    styleView.style.textAlign = 'center';
    document.getElementById('left').src = './static/p/csstype/left.gif';
    document.getElementById('right').src = './static/p/csstype/right.gif';
    document.getElementById('justify').src = './static/p/csstype/justify.gif';
  }
  setCSS();
}

/*Toggles Right align*/
function right(){
  var input = document.getElementById('textInput');
  var styleView = document.getElementById('textInputViewer');
  var right = document.getElementById('right');
  if(right.src.match('right.gif')){
    right.src = './static/p/csstype/right_a.gif';
    input.style.textAlign = 'right';
    styleView.style.textAlign = 'right';
    document.getElementById('left').src = './static/p/csstype/left.gif';
    document.getElementById('justify').src = './static/p/csstype/justify.gif';
    document.getElementById('center').src = './static/p/csstype/center.gif';
  }
  setCSS();
}

/*Toggles Justify align*/
function justify(){
  var input = document.getElementById('textInput');
  var styleView = document.getElementById('textInputViewer');
  var justify = document.getElementById('justify');
  if(justify.src.match('justify.gif')){
    justify.src = './static/p/csstype/justify_a.gif';
    input.style.textAlign = 'justify';
    styleView.style.textAlign = 'justify';
    document.getElementById('left').src = './static/p/csstype/left.gif';
    document.getElementById('right').src = './static/p/csstype/right.gif';
    document.getElementById('center').src = './static/p/csstype/center.gif';
  }
  setCSS();
}

/*Changes the Line Spacing*/
function changeLineSpacing(){
  var spacing = document.getElementById('lineSpacingValue').value;
  var styleView = document.getElementById('textInputViewer');
  var input = document.getElementById('textInput');
  input.style.lineHeight = spacing;
  styleView.style.lineHeight = spacing;
  setCSS();
}

/*Changes the Letter Spacing*/
function changeLetterSpacing(){
  var spacing = document.getElementById('letterSpacingValue').value;
  var styleView = document.getElementById('textInputViewer');
  var input = document.getElementById('textInput');
  input.style.letterSpacing = spacing + "pt";
  styleView.style.letterSpacing = spacing + "pt";
  setCSS();
}

/*Changes the Word Spacing*/
function changeWordSpacing(){
  var spacing = document.getElementById('wordSpacingValue').value;
  var styleView = document.getElementById('textInputViewer');
  var input = document.getElementById('textInput');
  input.style.wordSpacing = spacing + "pt";
  styleView.style.wordSpacing = spacing + "pt";
  setCSS();
}

function setColorInput(){
  var inp = document.getElementById('ColorChooser');
  var selectTag = document.getElementById('color');
  var selection = selectTag[selectTag.selectedIndex].value;
          
  if(selection == "color"){
    inp.value = RGB2Color(document.getElementById("textInput").style.color);
  }else{
    inp.value = RGB2Color(document.getElementById("textInput").style.backgroundColor);
  }
}

/*Set the CSS code in the output field*/
function setCSS(){
  var instyle = document.getElementById('textInput').style;
  var text = "";
  if(instyle.fontFamily) text += "font-family: " + instyle.fontFamily + ";\n";
  if(instyle.color && RGB2Color(instyle.color) != '#000000') text += "color: " + RGB2Color(instyle.color) + ";\n";
  if(instyle.backgroundColor && RGB2Color(instyle.backgroundColor) != '#FFFFFF') text += "background-color: " + RGB2Color(instyle.backgroundColor) + ";\n";
  if(instyle.fontSize) text += "font-size: " + instyle.fontSize + ";\n";
  if(instyle.fontWeight) text += "font-weight: " + instyle.fontWeight + ";\n";
  if(instyle.fontStyle) text += "font-style: " + instyle.fontStyle + ";\n";
  if(instyle.textDecoration) text += "text-decoration: " + instyle.textDecoration + ";\n";
  if(instyle.textTransform) text += "text-transform: " + instyle.textTransform + ";\n";
  if(instyle.fontVariant) text += "font-variant: " + instyle.fontVariant + ";\n";
  if(instyle.textAlign && instyle.textAlign != "left") text += "text-align: " + instyle.textAlign + ";\n";
  if(instyle.letterSpacing && instyle.letterSpacing != "1pt") text += "letter-spacing: " + instyle.letterSpacing + ";\n";
  if(instyle.wordSpacing && instyle.wordSpacing != "1pt") text += "word-spacing: " + instyle.wordSpacing + ";\n";
  if(instyle.lineHeight && instyle.lineHeight != 1) text += "line-height: " + instyle.lineHeight + ";\n";
  
  document.getElementById('cssOutput').value = text;
}

/*Initializes the CSS in the output to the default values*/
function initCSS(){
  var instyle = document.getElementById('textInput').style;
  var styleView = document.getElementById('textInputViewer').style;
  instyle.fontFamily = "verdana, sans-serif";
  styleView.fontFamily = "verdana, sans-serif";
  instyle.fontSize = "12px";
  styleView.fontSize = "12px";
}

/*Called when the input textarea loses focus.  Shows the <div> element
and sets the new text*/
function loseFocus(){
  var instyle = document.getElementById('textInput');
  var styleView = document.getElementById('textInputViewer');
  matchDivLoc();
  //styleView.style.visibility = "visible";
  styleView.style.display = "block";
}

/*Called when the input area gains focus.  Hides the <div> element*/
function gainFocus(){
  var instyle = document.getElementById('textInput');
  var styleView = document.getElementById('textInputViewer');
  
  //if it's the first time the user clicks, select the text
  if(instyle.value == "Paste the text you want to modify here."){
    //instyle.select();
  }
  
  matchTALoc();
//  styleView.style.visibility = "hidden";
  styleView.style.display = "none";
  
  instyle.focus();
}

/*Copies the text from the input textarea to the div above it*/
function copyTextToDiv(){
  var instyle = document.getElementById('textInput');
  var styleView = document.getElementById('textInputViewer');
  
  var fixedText = instyle.value.replace(/\n/g,'<br/>');
  
  var multiSpaces = fixedText.match(/\s{2,}/g);
  var spaceCodes = new Array();
  for(var i=0; multiSpaces && i<multiSpaces.length; i++){
    spaceCodes[i] = multiSpaces[i].replace(/\s/g,'&nbsp;');
    fixedText = fixedText.replace(multiSpaces[i],spaceCodes[i]);
  }
  
  styleView.innerHTML = fixedText;
}

//-----------------------------------------------------------------------------
//These two functions are used to match the scrollbars on the input textarea
//and the div above it.
function matchDivLoc(){
  var ta = document.getElementById('textInput');
  var div = document.getElementById('textInputViewer');
  
  div.scrollTop = ta.scrollTop;
}

function matchTALoc(){
  var ta = document.getElementById('textInput');
  var div = document.getElementById('textInputViewer');
  
  ta.scrollTop = div.scrollTop;
}

//-----------------------------------------------------------------------------
//taken from http://www.krazydad.com/makecolors.php
//Modified lots and tons
function byte2Hex(n){
  var nybHexString = "0123456789ABCDEF";
  return String(nybHexString.substr((n >> 4) & 0x0F,1)) + nybHexString.substr(n & 0x0F,1);
}

function RGB2Color(colors){
  if(!colors) return '000000';
  if(!colors.match('rgb')) return colors;
  var rgb = colors.match(/\d+/g);
  return "#" + byte2Hex(rgb[0]) + byte2Hex(rgb[1]) + byte2Hex(rgb[2]);
}
//-----------------------------------------------------------------------------

function noSupport(version){
  var content = document.getElementById('content');
  content.parentElement.removeChild(content);
  document.getElementById('browserNoSupport').style.visibility = 'visible';
  
  var sm = document.getElementById('noSupportMsg');
  sm.innerHTML = 'CSSTypeSET does not support ' + version + ' at this time, but we plan to add support soon.<br />'
    + 'For now check out one of these supported browsers! <br />'
    + '<a href="http://www.apple.com/safari/">Safari</a><br />'
    + '<a href="http://www.getfirefox.com">Firefox</a><br />'
    + '<a href="http://www.opera.com/download/">Opera</a><br />'
    + '<a href="http://www.microsoft.com/windows/products/winfamily/ie/default.mspx">Internet Explorer 7</a>';
  sm.style.visibility = 'visible';
}