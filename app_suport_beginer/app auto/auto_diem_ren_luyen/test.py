from selenium import webdriver
from time import sleep
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as df
import random

account  = "20010920"
password = "0333288883"

click_edit = '//*[@id="root"]/div/main/div[1]/div/div[2]/div/div[2]/div/div[1]/div[1]/button'
click_done = '/html/body/div[3]/div[3]/div/div[2]/button'

def login():
    df.write(account)
    df.press('tab')
    df.write(password)
    df.press('enter')
    sleep(2) 
    broser.get('https://ctsv.phenikaa-uni.edu.vn/diem-ren-luyen/ca-nhan')

def edit_click(xpath):
    sleep(2)   
    clickBtn = broser.find_element(By.XPATH, xpath)
    clickBtn.click()

a = [7,0,-65,-65]

def send_key(keys):
    sleep(0.2) 
    for i in keys:
        sleep(0.2) 
        if (i > 0):
            for j in range(0 , i):
                df.press('tab')
        if (i == 0):
            df.press('up')
        if (i < 0):
            for j in range(0 , abs(i)):
                df.press('tab')
                df.press('up')


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")
broser = webdriver.Chrome(chrome_options=chrome_options ,executable_path="./chromedriver.exe")
broser.get('https://ctsv.phenikaa-uni.edu.vn/diem-ren-luyen/ca-nhan')
sleep(1)   
login()
edit_click(click_edit)
send_key(a)
edit_click(click_edit)
edit_click(click_done)
sleep(2)           
broser.close() 
