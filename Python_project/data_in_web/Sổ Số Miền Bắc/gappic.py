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

def profit_calculator():
    ngay =  int(Ngay.get())
    thang = int(Thang.get())
    nam = int(Nam.get())
    return ngay,thang,nam

Label(main,text="KẾT QUẢ SỔ SỐ MIỀN BẮC",justify=CENTER).grid(row=0,columnspan=3)

for i in range(0,len(name_data)):
    Label(main,text=name_data[i]).grid(row=i+1,column=0)
    colum=2
    for j in range(0,len(data[i])):
        data[i][j]=StringVar()
        Entry(main,width=10,textvariable=data[i][j]).grid(row=i+1,column=colum)
        colum+=1

Label(main,text="").grid(row=9,column=0)

B = Button(text="tra cứu",command=chane)
B.grid(row=11,column=6)

B = Button(text=" to day ",command=profit_calculator)
B.grid(row=11,column=4)

B = Button(text="set day",command=clear)
B.grid(row=11,column=5)

Label(main,text="Nhập ngày tháng năm:  ").grid(row=11,column=0)
Entry(main,width=5,font=("Tahoma",12),textvariable=Ngay).grid(row=11,column=1)
Entry(main,width=5,font=("Tahoma",12),textvariable=Thang).grid(row=11,column=2)
Entry(main,width=5,font=("Tahoma",12),textvariable=Nam).grid(row=11,column=3)

print(profit_calculator())

main.mainloop()