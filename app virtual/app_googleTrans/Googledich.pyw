from tkinter import*
from tkinter.font import BOLD
from googletrans import Translator
import pyttsx3

root=Tk()
root.title('Trợ lý ảo')
root.geometry("400x500")
root.iconbitmap('logo.ico')

l = Label(root, text = "Trợ Lý Ảo Của Bạn",fg="#a52a2a",pady=10) 
l.config(font =("Courier", 20)) 
l.pack()

box1=Text(root,width=50,height=4,font=("ROBOTO",10))
box1.pack(pady=20)
box_frame=Frame(root).pack(side=BOTTOM)

def reset():
    box1.delete(1.0,END)
    box2.delete(1.0,END)

def trans():
    box2.delete(1.0,END)
    new=box1.get(1.0,END)
    print(new)
    t=Translator()
    a=t.translate(new,src='auto',dest='en')
    new2=a.text
    box2.insert(END,new2)
    
def speak_text():
    noi=box2.get(1.0,END)
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.say(noi)
    engine.runAndWait()

clear_box=Button(box_frame,text="reset",font=("Arian",10,'bold'),fg='#000099',command=reset)
clear_box.place(x=50,y=175)
clear_box=Button(box_frame,text="Trans",font=("Arian",10,'bold'),fg='#000099',command=trans)
clear_box.place(x=300,y=175)
speak_box=Button(box_frame,text="Speak",font=("Arian",10,'bold'),fg='#000099',command=speak_text)
speak_box.place(x=50,y=300)

box2=Text(root,width=50,height=4,font=("ROBOTO",10))
box2.pack(pady=60)

l2 = Label(root, text = "Dịch Cả Thế Giới Với Translate",fg="#a52a2a",pady=10) 
l2.config(font =("Courier", 15)) 
l2.pack()

root.mainloop()