<<<<<<< HEAD
from default import*
import random

class point():
    x=0
    y=0
    point=30


class HeadSnake(point):
    def uprage(Key):
        if (Key=="UP"):
            HeadSnake.y-=25
        elif (Key=="DOWN"):
            HeadSnake.y+=25
        elif (Key=="LEFT"):
            HeadSnake.x-=25
        elif (Key=="RIGHT"):
            HeadSnake.x+=25
        elif Key=="SPACE":
            pass
        HeadSnake.x,HeadSnake.y=limit(HeadSnake.x,HeadSnake.y)
    def check():
        if (fruit.x==HeadSnake.x and fruit.y==HeadSnake.y):
            fruit.change()
            BodySnake.size+=1
            HeadSnake.point+=10
    def die():
        for i in BodySnake.body:
            if i==(HeadSnake.x,HeadSnake.y):
                return False
        BodySnake.uprage()

class BodySnake():
    body=[(-25,-25),(-25,-25),(-25,-25)]
    size=3
    def uprage():
        BodySnake.body.insert(0,(HeadSnake.x,HeadSnake.y))
        if (len(BodySnake.body)>BodySnake.size):
            BodySnake.body.pop(BodySnake.size)

class fruit(point):
    x=125
    y=175
    def change():
        fruit.x=random.randrange(25, 700, 25)
        fruit.y=random.randrange(25, 450, 25)

def run(Key):
    HeadSnake.check()
    check=HeadSnake.die()
    HeadSnake.uprage(Key)
    return check
=======
import pygame
import time 
import random

from pygame.constants import KSCAN_Y, K_LEFT, K_SPACE

pygame.init()

screen=pygame.display.set_mode((725,500))

GREY=(130,120,200)
WHITE=(255,255,252)
pink=(250,200,250)
RED=(250,0,0)
GRAY=(128,128,128)
x=50
y=25
b1=[0,-0,-25]
b2=[25,25,25]
n=3
a=random.randrange(25, 700, 25)
b=random.randrange(25, 450, 25)
runing=True
Key="RIGHT"

class HeadSnake():
    def __init__(self,Huong,Vtx,Vty,Fx,Fy):
        self.Direction=Huong
        self.x=Vtx
        self.y=Vty
        self.fx=Fx
        self.fy=Fy
    def Change(self):
        if (self.Direction=="UP"):
            self.y-=25
        if (self.Direction=="DOWN"):
            self.y+=25
        if (self.Direction=="LEFT"):
            self.x-=25
        if (self.Direction=="RIGHT"):
            self.x+=25
        time.sleep(0.1)
        pygame.draw.rect(screen,WHITE,(self.x,self.y,25,25))
        return self.x,self.y
    def eat(self):
        if (self.x == self.fx and self.y == self.fy):
            return True
    def die(self):
        if (x<25 or x>700 or y<25 or y>450):
            return False   
        else:
            return True     

def Fruit(x,y,a,b):
    while (x==a and y==b):
        a=random.randrange(25, 700, 25)
        b=random.randrange(25, 475, 25)
    return a,b

def body(b1,b2,x,y,n):
    for i in range(0,n):
        if (b1[i]==x and b2[i]==y):
            return False
    b1.insert(0,x)
    b2.insert(0,y)
    for i in range (1,n):
        pygame.draw.rect(screen,pink,(b1[i],b2[i],25,25))
    return True
    
while runing:
    screen.fill(GREY)
    pygame.draw.rect(screen,RED,(a,b,25,25))
    Head=HeadSnake(Key,x,y,a,b)
    x,y=Head.Change()
    runing=Head.die()
    if Head.eat():
        a,b=Fruit(x,y,a,b)
        n+=1 
    runin=body(b1,b2,x,y,n)
    if runin==False:
        runing=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing=False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP and Key != "DOWN":
                Key="UP"
            if event.key==pygame.K_DOWN and Key != "UP" :
                Key="DOWN"
            if event.key==pygame.K_RIGHT and Key != "LEFT":
                Key="RIGHT"
            if event.key==pygame.K_LEFT and Key != "RIGHT":
                Key="LEFT"
    pygame.draw.rect(screen,GRAY,(10,10,710,485),25)
    pygame.display.flip()
pygame.quit()
print ("GAME OVER!")
>>>>>>> 5b25370d93c5ac8da625b9d9672e452934014730
