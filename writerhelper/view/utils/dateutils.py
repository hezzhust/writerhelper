# -*- coding: utf-8 -*-
import datetime
import time

DEFUALT_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"

# 把datetime转成字符串
def datetime_toString(dt):
    return dt.strftime(DEFUALT_FORMAT)


# 把字符串转成datetime
def string_toDatetime(st):
    return datetime.datetime.strptime(st, DEFUALT_FORMAT)


# 把字符串转成时间戳形式
def string_toTimestamp(st):
    return time.mktime(time.strptime(st, DEFUALT_FORMAT))


# 把时间戳转成字符串形式
def timestamp_toString(sp):
    return time.strftime(DEFUALT_FORMAT, time.localtime(sp))


# 把datetime类型转外时间戳形式
def datetime_toTimestamp(dt):
    return time.mktime(dt.timetuple())


# 格式化成2017-08-18
def fmt_date(c_time):
    return fmt_d(c_time, DATE_FORMAT)


# 格式化成22:18:45
def fmt_time(c_time):
    return fmt_d(c_time, TIME_FORMAT)


# 格式化成2017-08-18 22:18:45
def fmt_datetime(c_time):
    return fmt_d(c_time, DEFUALT_FORMAT)


# 格式化成“fmt_str”指定格式
def fmt_d(c_time, fmt_str=None):
    if c_time is None:
        c_time = time.time()
    if fmt_str is None:
        fmt_str = DEFUALT_FORMAT
    return time.strftime(fmt_str, time.localtime(c_time))


# 将字符串格式的时间转换成时间戳（单位毫秒）
def stamp_time(time_str, fmt_str=None):
    if time_str is None or len(time_str) == 0:
        return None
    if fmt_str is None:
        fmt_str = DEFUALT_FORMAT
    try:
        timeArray = time.strptime(time_str, fmt_str)
        timeStamp = int(time.mktime(timeArray)) * 1000
        return timeStamp
    except Exception as e:
        print(e)
    return None