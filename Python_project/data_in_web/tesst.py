#Source: https://bit.ly/2KHn1ZW

import requests
from lxml import html
from collections import namedtuple

# Bước 1 kiểm tra xem nó cho phép không?

url = 'https://xoso.com.vn/xsmb-01-01-2020.html'

htlm_web = requests.get(url)

doc =  html.fromstring(htlm_web.content)

# print(htlm_web)

# xpath_name = "//*[@id='table-body-scroll']"
data = doc.xpath('//div[@id="kqngay_01012020_kq"]/table/tbody/tr[2]/td/span/text()')
print('giải đặc biệt:',data[0])
for i in range(3,10):
   data = doc.xpath('//div[@id="kqngay_01012020_kq"]/table/tbody/tr['+str(i)+']/td/span/text()')
   print('giải ' ,i-2 , ':',data[0:])

