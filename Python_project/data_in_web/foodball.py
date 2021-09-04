#Source: https://bit.ly/3cepXbI
from collections import namedtuple
import requests
from lxml import html

url = "https://www.24h.com.vn/bong-da/lich-thi-dau-cua-tuyen-viet-nam-o-vong-loai-thu-3-world-cup-2022-c48a1266672.html"
# url = "https://ncov.moh.gov.vn/"
# html_text = html.fromstring(requests.get(url).content)

html_conten = requests.get(url)

doc =  html.fromstring(html_conten.content)

matday = doc.xpath("//section[@class='cate-24h-foot-box-sche-table-ring cid40yjcbx2sq6oq736iqqqczwt1 rid2h83rz86nym6ac50nkadrq6i2']/article/header/span/text()")

day_run=[]

for i in matday:
    x=i[18:]+'-'+i[15:17]+'-'+i[12:14]
    day_run.append(x)

for x in day_run:
    class_run = "\"//article[@class=\'cate-24h-foot-box-sche-table margin-bottom-15 d\'"+x+"]\""

    ketqua = doc.xpath("//article[@class='cate-24h-foot-box-sche-table margin-bottom-15 d"+x+"']")

    day = ketqua[0].xpath("header[@class='cate-24h-foot-box-sche-table__title text-center']/span/text()")

    ketqua = ketqua[0].xpath("nav/ul/li/div[@class='d-flex align-items-center justify-content-between box-1']")

    print(day[0].upper())

    for i in range(0,len(ketqua)):
        time = ketqua[i].xpath("time/strong/text()")
        home = ketqua[i].xpath("div[@class='cate-24h-foot-home-sche-content__match d-flex align-items-center justify-content-center']/div[@class='cate-24h-foot-home-sche-content__match--left d-flex align-items-center justify-content-end']/figcaption/span/text()") 
        ways = ketqua[i].xpath("div[@class='cate-24h-foot-home-sche-content__match d-flex align-items-center justify-content-center']/div[@class='cate-24h-foot-home-sche-content__match--right d-flex align-items-center']/figcaption/span/text()")

        print(time[0][:5]+' '+home[0]+' vs '+ways[0])
    print()