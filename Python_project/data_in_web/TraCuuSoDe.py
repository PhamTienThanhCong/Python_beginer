#Source: https://bit.ly/2KHn1ZW

import requests
from lxml import html
from collections import namedtuple

# Bước 1 kiểm tra xem nó cho phép không?

url = 'https://xoso.com.vn/xsmb-06-09-2021.html'

htlm_web = requests.get(url)

doc =  html.fromstring(htlm_web.content)

# print(htlm_web)

# xpath_name = "//*[@id='table-body-scroll']"
data = doc.xpath('//*[@id="kqngay_06092021_kq"]/table/tbody/tr[2]/td/span/text()')
print("giải đặc biệt",data)
for i in range(3,10):
   data = doc.xpath('//*[@id="kqngay_06092021_kq"]/table/tbody/tr['+str(i)+']/td/span/text()')
   print('giải ' ,i-2 , ':',data[0:])

