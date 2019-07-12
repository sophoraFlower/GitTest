# coding:utf8

import time

"""
print(time.time())  # 1558923723.4145875
print(time.ctime())  # Mon May 27 10:22:03 2019
print(time.gmtime())  # time.struct_time(tm_year=2019, tm_mon=5, tm_mday=27, tm_hour=2, tm_min=22, tm_sec=57, tm_wday=0, tm_yday=147, tm_isdst=0)

t1 = time.gmtime()
t2 = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", t1))   # 2019-05-27 02:26:10
print(time.strftime("%Y-%m-%d %H:%M:%S", t2))   # 2019-05-27 10:34:49

timeStr = "2018-01-26 12:55:20"
print(time.strptime(timeStr, "%Y-%m-%d %H:%M:%S"))

start = time.perf_counter()
print(start)
end = time.perf_counter()
print(end)
print(end-start)
"""

time_1 = time.time()
print(time_1)
time_2 = time.ctime()
print(time_2)
time_3 = time.gmtime()
print(time.gmtime())

# 时间格式化
time_format_1 = time.strftime("%Y-%m-%d", time_3)
time_format_2 = time.strftime("%m-%B-%b  %A-%a")
time_format_3 = time.strftime("%p: %H:%M:%S")
print(time_format_1)
print(time_format_2)
print(time_format_3)

time_format_4 = "2019-06-02 15:33:33"
print(time.strptime(time_format_4, "%Y-%m-%d %H:%M:%S"))  # 得到与time.gmtime()一样的时间格式

# 测量时间：perf_count()
time_per = time.perf_counter()
time.sleep(2)
time_per_2 = time.perf_counter()
print("{}  {}".format(time_per, time_per_2))





