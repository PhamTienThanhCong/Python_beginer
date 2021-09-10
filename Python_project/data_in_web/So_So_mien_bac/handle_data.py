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

data_train = get_url('09','09','2021')

def print_data(data_train):
    print(data_train)
    for i in range(0,len(data_train)):
        for j in range(0,len(data_train[i])):
            data[i][j].set(data_train[i][j])

def clear():
    for i in range(0,len(data_train)):
        for j in range(0,len(data_train[i])):
            data[i][j].set("")

def check_today():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    if (current_time>"18:30"):
        return True
    else: 
        return False



# def settoday():
#     today = date.today()
#     day   = today.strftime("%d")
#     month = today.strftime("%m")
#     year  = today.strftime("%Y")
#     if check_today==True:
#         # Label(main,text="Ngay chuan").grid(row=9,column=0)
#         print("done")


# day,month,year = settoday()
# day,month,year = settoday()



# url = 'https://xoso.com.vn/xsmb-09-09-2021.html'
# day = '09092021'

