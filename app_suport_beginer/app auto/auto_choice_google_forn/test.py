from selenium import webdriver
from time import sleep
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import pyautogui as df
import random


def click(key):
    if key == -5:
        key = random.randint(2,key*-1)
    elif key < -1 and key > -5:
        key = random.randint(1,key*-1)
    if key==1:
        df.press('down')
        df.press('up')
    elif key == 0:
        df.press('enter')
        sleep(2)
    elif key == -1:
        df.press('tab')
    elif key > 1:
        for i in range(1,key):
            df.press('down')

a = [-1,-1,-2,-1,-2,-1,-3,-1,3,-1,-1,2,-1,0,-1,-3,-1,-1,-4,-1,-1,-3,-1,-3,-1,-1,-1,0,-1,-5,-1,-5,-1,-5,-1,-5,-1,1,-1,3,-1,-1,0]

for time in range(20,100):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    broser = webdriver.Chrome(chrome_options=chrome_options ,executable_path="chromedriver.exe")
    broser.get('https://docs.google.com/forms/d/1G2XlqW8pxGaJZSgxvtDlloL_jCfd0tMT4VVLCAmwgJ8/viewform?ts=60bf9201&fbclid=IwAR3VVW8JS_jVnRHpx4Iv7eRvduzGK0qTbzcang_UeVRjvBzFxE8GpDQi41M&edit_requested=true')
    sleep(3)
    for i in a:
        click(i)  
        sleep(0.5)     
    broser.close() 
    print(time)
    sleep(2)           
    