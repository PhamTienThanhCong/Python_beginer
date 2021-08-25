def limit(x,y):
    if x>LENGTHBACKGROUD-25:
        x=0
    elif x<0:
        x=LENGTHBACKGROUD
    if y<0:
        y=WIDTHBACKGROUD
    elif y>WIDTHBACKGROUD-25:
        y=0
    return x,y

LENGTHBACKGROUD=700
WIDTHBACKGROUD=500
SPEED=0.1

GREY=(130,120,200)
WHITE=(255,255,252)
pink=(250,200,250)
RED=(250,0,0)
GRAY=(128,128,128)
black=(0,0,0,0.7)
runing=True
Key="RIGHT"
