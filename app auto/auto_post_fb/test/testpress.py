xpath = open('extend\\DataXpath.txt','r')
Data = open('extend\\DataText.txt','r')

XpathText = xpath.readlines()
DataText = Data.readlines()

for i in range(0,12):
    DataText[i] = DataText[i].replace('\n', ' ').replace('\r', '')
    XpathText[i] = XpathText[i].replace('\n', ' ').replace('\r', '')
    if (i==2 or i== 3 or i==4 or i==6 or i==8):
        DataText[i]=int(DataText[i])    