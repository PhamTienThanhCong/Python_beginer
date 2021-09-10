import re
from tkinter.constants import FALSE
from pull_data_in_web import *
import time
from datetime import date   

data = [['87728'], ['88415'], ['19940 ', ' 44927'], ['26793 ', ' 17788 ', ' 33474 ', ' 52904 ', ' 88310 ', ' 77646'], ['1183 ', ' 9036 ', ' 7786 ', ' 1612'], ['8192 ', ' 9483 ', ' 3950 ', ' 4803 ', ' 7481 ', ' 1667'], ['792 ', ' 575 ', ' 369'], ['71 ', ' 02 ', ' 19 ', ' 65']]

data_train = [['87728'], ['88415'], ['19940 ', ' 44927'], ['26793 ', ' 17788 ', ' 33474 ', ' 52904 ', ' 88310 ', ' 77646'], ['1183 ', ' 9036 ', ' 7786 ', ' 1612'], ['8192 ', ' 9483 ', ' 3950 ', ' 4803 ', ' 7481 ', ' 1667'], ['792 ', ' 575 ', ' 369'], ['71 ', ' 02 ', ' 19 ', ' 65']]
name_data = ['Giải đặc biệt','Giải 1','Giải 2','Giải 3','Giải 4','Giải 5','Giải 6','Giải 7']

def get_url(day,month,year):
    url = 'https://xoso.com.vn/xsmb-'+day+'-'+month+'-'+year+'.html'
    day = day+month+year
    return get_data(url,day)

def print_data(a,b,c):
    data_train = get_url(a,b,c)
    for i in range(0,len(data_train)):
        for j in range(0,len(data_train[i])):
            data[i][j].set(data_train[i][j])

def clear():
    for i in range(0,len(data_train)):
        for j in range(0,len(data_train[i])):
            data[i][j].set("")


def data_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    return current_time

def check_today():
    current_time =data_time()
    if (current_time>"18:30"):
        return True
    else: 
        return False

def fix_data(a,b):
    if (len(a)==1):
        a='0'+a
    if (len(b)==1):
        b='0'+b
    return a,b

def check_data(a,b,c):
    for i in a:
        if ('0'<=i and i<='9')==False:
            return "Ngày Không hợp lệ"
    for i in b:
        if ('0'<=i and i<='9')==False:
            return "Tháng Không hợp lệ"
    for i in c:
        if ('0'<=i and i<='9')==False:
            return "Năm Không hợp lệ"
    a=int(a)
    b=int(b)
    c=int(c)

    today = date.today()
    x   = today.strftime("%d")
    y = today.strftime("%m")
    z  = today.strftime("%Y")

    if (a<1 or a>31):
        return "Lỗi 1<=Ngày<=31"
    if (b<1 or b>12):
        return "Lỗi 1<=Tháng<=12"
    if (c<2015):
        return "Lỗi năm <=2015"
    
    if c==int(z):
        if b==int(y):
            if a>int(x):
                return "Không vượt quá Ngày"
        if b>int(y):
            return "Không vượt quá tháng"
    if c > int(z):
        return "Không vượt quá năm"
