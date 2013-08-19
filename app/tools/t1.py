# -*- coding: utf-8 -*-
__author__ = 'Administrator'
from BeautifulSoup import BeautifulSoup as bs
root='<html><head></head><body></body><h1>hello<script type="text/javascript">document.wirte("helloworld");var i=10;</script></h1></html>'
soup=bs(root)                #make BeautifulSoup
prettyHTML=soup.prettify()   #prettify the html
print(prettyHTML)