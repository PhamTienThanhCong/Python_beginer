#Source: https://bit.ly/2KHn1ZW

import requests
from lxml import html
from collections import namedtuple

url = 'https://xoso.com.vn/xsmb-06-09-2021.html'
day = '06092021'

def get_data(url,day):

   htlm_web = requests.get(url)

   doc =  html.fromstring(htlm_web.content)

   number_data=[]
   
   for i in range(2,10):
      data = doc.xpath('//*[@id="kqngay_'+day+'_kq"]/table/tbody/tr['+str(i)+']/td/span/text()')
      number_data.append(data)

   return number_data

print(get_data(url,0))