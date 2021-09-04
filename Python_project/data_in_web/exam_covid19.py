#Source: https://bit.ly/3cepXbI
from collections import namedtuple
import requests
from lxml import html

fmt = """\nTổng Số Người Mắc COVID-19 : {} Người
\nTỏng Số Người Tử Vong Do COVID-19 : {} Người
\nTổng Số Người Đã Được Chữa Khỏi COVID-19 : {} Người"""

url_vn = "https://www.worldometers.info/coronavirus/country/viet-nam/"
url_world = "https://www.worldometers.info/coronavirus/"

def covid_stats(url):
    xpath_str = '//div[@class = "maincounter-number"]/span/text()'
    x = html.fromstring(requests.get(url).content).xpath(xpath_str)
    print(fmt.format(*x))

print("Ở VIỆT NAM: ")
covid_stats(url_vn)
print("\nTRÊN THẾ GIỚI")
covid_stats(url_world)