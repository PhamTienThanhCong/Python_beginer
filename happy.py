import pygame as pg
import datetime
from famework import*
import os

def maintime():
    pg.init()
    screen = pg.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
    FontTime = pg.font.Font(None, 120)
    FontDay = pg.font.Font('freesansbold.ttf', 60)
    FontText= pg.font.Font(None, 60)
    gray = pg.Color('gray19')
    blue = pg.Color('dodgerblue')
    red  = (250,0,0)
    # The clock is used to limit the frame rate
    # and returns the time since last tick.
    clock = pg.time.Clock()

    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

         # Reset it to 10 or do something else.
        time = datetime.datetime.now()
        #print(time.strftime("%H:%M:%S"))
        time_down=time.strftime("%H:%M:%S")
        DayMonth =time.strftime("%d-%m-%Y")
        screen.fill(gray)
        hour1 = FontTime.render(time_down, True, blue)
        day   = FontDay.render(DayMonth,True, red)
        text  = FontText.render("The clock does not count down",True, red)
        text2  = FontText.render("waiting sleep in today",True, red)
        screen.blit(hour1, (450,DISPLAY_HEIGHT//2-90))
        screen.blit(day, (465,DISPLAY_HEIGHT//2+10))
        screen.blit(text,(320,DISPLAY_HEIGHT//2-200))
        screen.blit(text2,(380,DISPLAY_HEIGHT//2+150))
        if time_down=="23:35:00":
            os.system("shutdown /p")
        pg.display.flip()

maintime()