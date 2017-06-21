#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

import calendar

ticks = time.time()
print "当前时间戳为：", ticks


localtime = time.localtime(time.time())
print "本地时间为：",localtime

locationtime = time.asctime(time.localtime(time.time()))
print "本地时间为：",locationtime

print time.strftime("%Y-%m-%d %H:%M:%S %Y",time.localtime())

a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

cal =calendar.month(2016,1)
print "以下输出2016年1月日历"

print cal;