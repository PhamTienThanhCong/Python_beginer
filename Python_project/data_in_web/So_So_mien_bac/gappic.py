from tkinter import *
from typing import Sized
from handle_data import *

main = Tk()

main.title("xổ số miền bắc")
main.resizable(height=True,width=True)
main.minsize(height=300,width=500)

kq=StringVar()
Ngay  = StringVar()
Thang = StringVar()
Nam   = StringVar()

def data_1():
    ngay =  str(Ngay.get())
    thang = str(Thang.get())
    nam = str(Nam.get())
    ngay,thang = fix_data(ngay,thang)
    return ngay,thang,nam

def data_2():
    today = date.today()
    day   = today.strftime("%d")
    month = today.strftime("%m")
    year  = today.strftime("%Y")
    return day,month,year

def data_check():
    a,b,c=data_1()
    x,y,z=data_2()
    if (a==x and b==y and c==z):
        if (check_today==True):
            text_print = "Ngày hôm nay"
        else:
            text_print = "Error: Có sau 18:30 "
        Label(main,text=text_print).grid(row=9,column=0)
    else:
        print_data(a,b,c)    

def getdata():
    ngay,thang,nam=data_1()
    a,b,c = data_2()
    kt = check_data(ngay,thang,nam);
    if kt!=None:
        text_print = kt
    else:
        if (a==ngay and b==thang and c==nam):
            text_print = "Ngày hôm nay"
        else:
            text_print = "Ngày: "+str(ngay)+"-"+str(thang)+"-"+str(nam)
    Label(main,text=text_print).grid(row=9,column=0)
    current_time = "Time: "+data_time()
    Label(main,text=current_time).grid(row=10,column=0)
    
def settoday():
    day,month,year = data_2()
    Ngay.set(day)
    Thang.set(month)
    Nam.set(year)
    
def search_data():
    clear()
    data_check()
    
Label(main,text="KẾT QUẢ SỔ SỐ MIỀN BẮC",justify=CENTER).grid(row=0,columnspan=3)

for i in range(0,len(name_data)):
    Label(main,text=name_data[i]).grid(row=i+1,column=0)
    colum=2
    for j in range(0,len(data[i])):
        data[i][j]=StringVar()
        Entry(main,width=10,textvariable=data[i][j]).grid(row=i+1,column=colum)
        colum+=1

Label(main,text="Ngày: ").grid(row=9,column=0)

B = Button(text="tra cứu",command=search_data)
B.grid(row=11,column=6)

B = Button(text=" to day ",command=settoday)
B.grid(row=11,column=4)

B = Button(text="set day",command=getdata)
B.grid(row=11,column=5)

Label(main,text="Nhập ngày tháng năm:  ").grid(row=11,column=0)

Label(main,text="Ngày").grid(row=10,column=1)
Entry(main,width=5,font=("Tahoma",12),textvariable=Ngay).grid(row=11,column=1)

Label(main,text="Tháng").grid(row=10,column=2)
Entry(main,width=5,font=("Tahoma",12),textvariable=Thang).grid(row=11,column=2)

Label(main,text="Năm").grid(row=10,column=3)
Entry(main,width=5,font=("Tahoma",12),textvariable=Nam).grid(row=11,column=3)

main.mainloop()