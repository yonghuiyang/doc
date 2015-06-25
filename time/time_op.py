#-*-coding:utf-8-*-
#/usr/bin/env python

import time
import datetime
from datetime import date
from datetime import timedelta

def TimeOp():
    #cat /etc/sysconfig/clock 查看系统时区
    #timestamp to struct_time
    print "gmtime:", time.gmtime() #返回0时区的struct_time
    print "localtime():", time.localtime() #返回当前系统设置时区的struct_time

    #struct_time to timestamp
    print time.mktime(time.localtime())
    #struct_time 格式化
    print time.strftime("%Y-%m-%d")
    print time.time() #timestamp
    print time.ctime(time.time()) #secs to 24-character string
    print time.asctime(time.gmtime()) #struct_time to 24-character string
                                      #default time.localtime()
    print time.strftime("%Y-%m-%d", time.strptime("20150610", "%Y%m%d"))

    #struct_time tm_yday：一年中的第几天
    st = time.localtime()
    print st.tm_year, st.tm_mon, st.tm_mday, st.tm_hour, st.tm_min
    print st.tm_wday, st.tm_yday, st.tm_isdst

def DateTimeDateOP():
    now = date.today()
    print now.year
    print now.month
    print now.day
    print now.weekday()
    print now.strftime("%Y/%m/%d")
    print date.fromtimestamp(time.time())

    print date.today().timetuple()

def DateTimeDateTimeOP():
    now = datetime.datetime.today()
    print now
    print datetime.datetime.fromtimestamp(time.time())

def TimeDeltaOP():
    now = date.today() #2015-06-25
    td = timedelta(days=1)
    tomorrow = now - td 
    print tomorrow  #2015-06-25

if __name__=='__main__':
    TimeDeltaOP()
