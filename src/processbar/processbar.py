# -*- coding: utf-8 -*-

import math
import time

# 绘图设置
# ELAPSED_DAY_CHAR='H'                # 已流逝天数的绘图字符
# ELAPSED_DAY_CHAR="\u2591"                # 已流逝天数的绘图字符 ░
# ELAPSED_DAY_CHAR="\u2764"                # 已流逝天数的绘图字符 ❤
ELAPSED_DAY_CHAR="\u2665"                # 已流逝天数的绘图字符 ♥
# REMAIN_DAY_CHAR='\u002D'                 # 年度剩余天数的绘图字符 -
#REMAIN_DAY_CHAR='\u2500'                 # 年度剩余天数的绘图字符 ━
REMAIN_DAY_CHAR='\u2661'                 # 年度剩余天数的绘图字符 ━♡
# Bar的字符数
BAR_NUM = 20
BAR_NUM_FACTOR = round(100/BAR_NUM)

Leap_monthDays=[31,29,31,30,31,30,31,31,30,31,30,31]
Ping_monthDays=[31,28,31,30,31,30,31,31,30,31,30,31]

def isLeapYear(year):
    retVal=0
    if((0 == (year % 4)) and (0 != (year % 100))):
        retVal = 1
    elif(0 == (year % 400)):
        retVal = 1

    return retVal

def elapsedDaysInYear(year,mon,day):
    LeapYear = isLeapYear(year)

    if(1 == LeapYear):
        pMonthDaysArray = Leap_monthDays
    else:
        pMonthDaysArray = Ping_monthDays
    
    sum = 0
    i = 0
    while(i < (mon -1)):
        sum += pMonthDaysArray[i]
        i = i + 1

    sum += day - 1
    return sum

def get_date():
    loc_time = time.localtime(time.time())
    #print("now datetime:",loc_time.tm_year,"\\",loc_time.tm_mon,"\\,",loc_time.tm_mday, loc_time.tm_hour,":",loc_time.tm_min,":",loc_time.tm_sec,"\n")
    return loc_time.tm_year,loc_time.tm_mon,loc_time.tm_mday

def generateText():
    year,mon,day = get_date()
    # year,mon,day = 2020,12,31
    # year,mon,day = 2020,1,2
    a = elapsedDaysInYear(year,mon,day)
    if(1 == isLeapYear(year)):
        b = 366
    else:
        b = 365
    p = a*100/b
    print(a,b,p)
    #if(a < 5):
        # 向上取整
    #    p=math.ceil(a*100/b)
    #elif(a > 350):
        # 向下取整
    #    p=int(a*100/b)
    #else:
        # 四舍五入
    #    p=round(a*100/b)
    #print(str(year)+"已经过了"+str(a)+"天，还剩"+str(b-a)+"天\n")
    #print('%d年已经过%d天了，还剩%d天了。\n' % (year,a,b-a))
    text ='{0}年已经过{1}天，还剩{2}天，余额{3:.1f}%。\n'.format(year,a,b-a,100-p)
    #print(text)
    return text,p

def generateBar(text,percentage):
    # bar='{0}% ['.format(percentage)
    bar=''
    tmp = math.ceil(percentage/BAR_NUM_FACTOR)
    for i in range(int(100/BAR_NUM_FACTOR)):
        if(i<tmp):
            bar=bar+ELAPSED_DAY_CHAR
        else:
            bar=bar+REMAIN_DAY_CHAR

    bar=bar+' {0:.1f}%\n'.format(percentage)
    bar=text+bar
    return bar

def GetText():
    text,p = generateText()
    #print(text)
    bar = generateBar(text,p)
    return bar

if __name__ == '__main__':
    text,p = generateText()
    print(text)
    bar = generateBar(text,p)
    print(bar)
