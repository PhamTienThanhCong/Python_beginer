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