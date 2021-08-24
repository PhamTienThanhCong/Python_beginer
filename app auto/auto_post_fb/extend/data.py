username = "tk"
password = "mk"
# username = "congphamtienthanh@gmail.com"
# password = "phamcong22022002"
conten_post = "Đây Là bot nâng cấp của bé công"
mapfile = 'C:\\Users\\congp\\Desktop\\facebook\\image'
namephoto = '\"photo.jpg\"\"votaoday.jpg\"'

#xử lý dữ liệu từ mảng vào
xpath = open('extend\\DataXpath.txt','r')
Data = open('extend\\DataText.txt','r')

XpathText = xpath.readlines()
DataText = Data.readlines()

for i in range(0,12):
    DataText[i] = DataText[i].replace('\n', ' ').replace('\r', '')
    XpathText[i] = XpathText[i].replace('\n', ' ').replace('\r', '')
    if (i== 3 or i==4 or i==6 or i==8):
        DataText[i]=int(DataText[i])

