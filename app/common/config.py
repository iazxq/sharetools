# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import pymongo
from sharetools import settings

SmsState = {'unread':u'未读',
            'readed':u'已读'}


Tools = {
    'jsdecoder':{'name':u'JavaScript代码格式化整理工具','content':u'JsDecoder工具可以将凌乱的JavaScript整理的整整齐齐，并且可以高亮显示。'},
    'periodic-table':{'name':u'在线元素周期表','content':u'本工具是一个可以在线使用的元素周期表，包含了所有元素及其相关数据'},
    'simple2traditional':{'name':u'在线繁简体转换工具','content':u'本工具可以把简体字转换成繁体，可以把繁体字转换成简体'},
    'regex-test':{'name':u'正则表达式在线测试工具','content':u'测试JavaScript正则表达式的工具，只要输入正则的内容就可以输出匹配结果等等。如果正则表达式不改变，可以观察到记录的lastIndex等等属性、并且能观察到属性的改变过程。'},
    'beautify-javascript':{'name':u'格式化JavaScript代码工具','content':u'可以把你写的凌乱的JavaScript整理的更漂亮一些'},
    'javascript-encrypt':{'name':u'JavaScript代码加密在线工具','content':u'可以对您辛苦编写的JavaScript代码进行加密，加密后是一对乱字符，放在网页里可以照样执行'},
    'web-color':{'name':u'在线网页配色工具','content':u'提供各种常用颜色供选择，均给出了该颜色的学名'},
    'calendar':{'name':u'在线万年历','content':u'阳历中红色/绿色表示节假日，农历中绿色表示为24节气日，红色表示为传统节日，蓝色则表示为公众节假日万年历，每月的节日提示，24节气，世界各国时间表等等，功能强大'},
    'safe-day':{'name':u'女性安全期测试','content':u'可以自己设定上次月经时间，最长周期，最短周期，帮你计算出你的安全期'},
    'calculator':{'name':u'在线科学计算器','content':u'类似于Windows里的科学计算器，不过功能好像更强大哟'},
    'pinyin':{'name':u'在线汉字转换成拼音工具','content':u'在线将汉字翻译为汉语拼音，可选择翻译中汉字和拼音一一对照'},
    'health':{'name':u'个人健康指数在线查询','content':u'输入您的体重和身高，得出您的健康值与电脑评价，电脑会提示您是否偏胖'},
    'jinzhi':{'name':u'在线进制转换工具','content':u'可以实现各类进制间的相互转换，二进制、十进制、八进制、十六进制以及各种自定义的进制之间的转换'},
    'unit':{'name':u'常用单位在线换算器','content':u'此工具提供了常用的计量单位换算的功能，包括长度单位、温度单位、功率、速度、重量、面积、体积、容积等单位的转换'},
    'css-format':{'name':u'CSS代码格在线式化工具','content':u'可以将格式不规整的CSS代码格式化成比较规范的格式，同时本工具可以压缩CSS的代码，减小CSS文件大小，同时起到一定程序的代码保护作用'},
    'html2js':{'name':u'HTML代码转换成JS代码','content':u'可以把HTML代码转换成JavaScript格式，形式如：document.write(...)，同时可以把转换后的JavaScript代码还原'},
    'md5':{'name':u'MD5在线加密工具','content':u'可以把用户输入的字符串生成32位的MD5编码'},
    'base64':{'name':u'Base64在线编码解码工具','content':u'对给定的文字进行标准的Base64加密和解密操作。'},
    'htpasswd':{'name':u'在线生成htpasswd工具','content':u'如果我们不使用apache服务器，例如使用nginx等，可能手头没有这个命令行工具，就无法生成密码文件，有了在线版的可以方便服务器管理员使用。'},
    'csstype':{'name':u'在线生成字体CSS样式工具','content':u'这是一个非常适合对CSS不熟悉的朋友的在线工具，使用这个工具可以轻松地写出具备字体、文本颜色大小位置、字符间距、单词间距等属性的CSS样式。'},
    'strongpasswordgenerator':{'name':u'高强度密码生成器','content':u'这是一个帮助你生成高强度密码的工具，你可以选择密码长度，是否包含标点符号，系统会自动为你生成一个难以破解的密码。'},
    'lottery':{'name':u'在线抽奖','content':u'一个简单的在线抽奖系统, 可用于公司年会抽奖, 电视台抽奖等，可以自己设定抽奖名单、抽奖人数、每次出奖人数，有防止重复得奖的功能。'},
    'unique':{'name':u'在线去重工具','content':u'这个工具可以用于去除列表中的重复项，将列表内容放入文本框内，每行一条，点击去重按钮，可以得到无重复数据的列表。'},
    'ifconfig':{'name':u'获取本机公网ip地址工具','content':u'这个工具获取本机上网的公网ip地址及用户浏览器相关信息，如：user-agent，HTTP_ACCEPT，cookie等信息'},



    }