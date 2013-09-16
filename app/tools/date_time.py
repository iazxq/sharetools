# -*- coding: utf-8 -*-
#!/usr/bin/env python
import datetime
#datetime一般的时间计算
d1 = datetime.datetime(2013, 8, 05,15,50)
d2 = datetime.datetime(2013, 8, 4,21,9,0,0)
d3 = datetime.timedelta(microseconds=5000)
print u'相差：%s微秒'%(d1-d2).microseconds
print u'相差：%s秒'%(d1-d2).seconds
print u'相差：%s天'%(d1-d2).days
print u'时间间隔：%s微秒'%d3
#时区转换，当前系统所在时区+1
d = datetime.datetime.now()
d = d + datetime.timedelta(seconds=3600)
print d
print d.ctime()