# -*- coding: utf-8 -*-

import smallseg
import gvar

def cut(value):
    seg = gvar.seg
    text = value.encode('utf8')
    result =  seg.cut(text)
    #result = map(lambda x:x.lower(),result)

    return result


if __name__=="__main__":
    print(cut(u'狼狗'))