from selenium import webdriver
from time import sleep
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from extend.data import*
import pyautogui as df

def setup():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    broser = webdriver.Chrome(chrome_options=chrome_options, executable_path="extend\chromedriver.exe")
    return broser

broser = setup()

class facebook():
    def __init__(self,user,password,post,mapfile,namephoto):
        self.user = user
        self.password = password
        self.post = post
        self.mapfile = mapfile
        self.namephoto = namephoto
    def login(self):
        broser.get("https://www.facebook.com/")
        user = broser.find_element_by_id("email")
        passworld = broser.find_element_by_id("pass")
        user.send_keys(self.user)
        passworld.send_keys(self.password)
        passworld.send_keys(Keys.RETURN)
        sleep(5)

    def KeyChosePhoto(self):
        # change map file
        df.keyDown('alt')
        df.press('d')
        df.keyUp('alt')
        df.typewrite(self.mapfile)
        df.press('enter')
        # chose file
        df.keyDown('alt')
        df.press('n')
        df.keyUp('alt')
        df.typewrite(self.namephoto)
        df.press('enter')

    def postconten(self):
        clickpost = broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div')
        clickpost.click()
        sleep(2)
        writepost = broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div')
        writepost.send_keys(self.post)
        sleep(1)
        postimg = broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div[1]/div/span/div')
        postimg.click()
        sleep(1)
        facebook.KeyChosePhoto(self)
        sleep(3)
        puts = broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div')
        puts.click()

    def PostMarket():
        pass

    def closefacebook():
        broser.close()

def choseclick(link,NumberOrClick):
    autoclick = broser.find_element_by_xpath(link)
    autoclick.click()
    sleep(1)
    if (type(NumberOrClick)==str and DataText!="none"):
        autoclick.send_keys(NumberOrClick)
        sleep(1)
    elif (type(NumberOrClick)==str and DataText =="none"):
        sleep(1)
        fb.KeyChosePhoto()
        sleep(2)
    elif (type(NumberOrClick) == int and NumberOrClick > 0):
        for i in range(1,NumberOrClick):
            df.press('dowm')
        df.press('enter')
        sleep(1)
    elif (type(NumberOrClick) == int and NumberOrClick < 0):
        for i in range(1,NumberOrClick):
            df.press('tab')
        df.press('enter')
        sleep(1)


fb=facebook(username,password,conten_post,mapfile,namephoto) 
fb.login()
sleep(1)
broser.get("https://www.facebook.com/marketplace/create/item")
sleep(3)

for i in range(1,12):
    choseclick(XpathText[i],DataText[i])