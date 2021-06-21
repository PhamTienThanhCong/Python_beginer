import pygame
import time 
from default import*
from snake import*

pygame.init()
screen=pygame.display.set_mode((LENGTHBACKGROUD,WIDTHBACKGROUD))

#hello man
while runing:
    screen.fill(GREY)
    ru=run(Key)
    pygame.display.set_caption("snake new game")
    pygame.draw.rect(screen,RED,(fruit.x,fruit.y,25,25))
    pygame.draw.rect(screen,pink,(HeadSnake.x,HeadSnake.y,25,25))
    text='point: '+str(HeadSnake.point)
    FontText=pygame.font.Font(None, 20)
    text3  = FontText.render(text,True, black)
    screen.blit(text3,(10,10))
    for x,y in BodySnake.body:
        pygame.draw.rect(screen,WHITE,(x,y,25,25))
    time.sleep(SPEED)
    if ru==False:
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
            if event.key==pygame.K_SPACE:
                Key="SPACE"
    pygame.display.flip()
pygame.quit()