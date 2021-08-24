from pyautogui import click
from LoginFaceBook import*


# chosephoto = broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[3]/div[1]/div/div/div')
# chosephoto.click()
# title = broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[4]/div/div/label/div/div[1]/input')
# title.click()
# title.send_keys('Bán Người yêu')
# sleep(1)

# value = broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[5]/div/div/label/div/div/input')
# value.click()
# value.send_keys('58000000')
# sleep(1)

# #HangMuc = broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[6]/div/div/div/label/div/div[1]/div/div')
# HangMuc =  broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[6]/div/div/div/label/div/div[1]/div/div')
# HangMuc.click()
# # HangMucCon = broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/span/div/div['+'19'+']/div/div[1]/div/div')
# # HangMucCon.click()
# sleep(1)
# LuaChon = broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[8]/div/div/div/label/div/div[1]/div/div')
# LuaChon.click()
# for i in range(1,3):
#     df.press('down')
# sleep(1)
# df.press('enter')
# df.press('tab')
# conten = broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[9]/div/div/label/div/div/textarea')
# #conten = broser.find_element_by_id('jsc_c_v')
# conten.click()
# conten.send_keys('Bán Người yêu vì \"het tien\"')
# sleep(1)

# TinhTrang = broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[10]/span/div/div/div/div/label/div/div[1]/div/div')
# TinhTrang.click()
# TinhTrang1 = broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]')
# TinhTrang1.click()
# sleep(1)

# ThuongHieu = broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[11]/div/div/label/div/div/input')
# ThuongHieu.click()
# ThuongHieu.send_keys('Móng Cái City')
# sleep(1)

# TinhChat =  broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[12]/div/div/div/label/div/div[1]/div/div')
# TinhChat.click()
# for i in range(1,6):
#     df.press('down')
# df.press('enter')
# sleep(1)

# DacDiem = broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[13]/div/div/label/div/div/input')
# DacDiem.click()
# DacDiem.send_keys('Xinh Nhất Làng')
# sleep(1)

# TheSanPham = broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[14]/div/div/div/label/div/div/div')
# TheSanPham.click()
# TheSanPham.send_keys('HangHiemThay')
# TheSanPham.send_keys(Keys.RETURN)
# sleep(1)

# SKU = broser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[15]/div/div/label/div/div/input')
# SKU.click()
# SKU.send_keys('SKU Là gì ???')



def choseclick(link,NumberOrClick):
    autoclick = broser.find_element_by_xpath(link)
    autoclick.click()
    sleep(1)
    if (type(NumberOrClick)==str and DataText!="none"):
        autoclick.send_keys(NumberOrClick)
        sleep(1)
    elif (type(NumberOrClick)==str and DataText!="none"):
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

fb.login()
sleep(1)
broser.get("https://www.facebook.com/marketplace/create/item")
sleep(3)

for i in range(0,12):
    choseclick(XpathText[i],DataText[i])