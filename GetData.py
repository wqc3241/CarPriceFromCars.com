# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 23:11:45 2017

@author: ASUS
"""

from lxml import html
import requests
from carData import carData
from re import sub
from decimal import Decimal

'''
from bs4 import BeautifulSoup
'''

carType = []
carPrice = []

'get all information from all pages'
pageUrl = "https://www.cars.com/for-sale/searchresults.action/?mdId=20567&mkId=20081&page=1&perPage=100&rd=99999&searchSource=PAGINATION&sort=price-highest&stkTypId=28880&zc=48823"
urlCopy = pageUrl

initial = 0

'''
tree = html.fromstring(page.content)
webinfo = page.text
soup = BeautifulSoup(webinfo, "lxml")
'''
text_file = open("Output.txt", "w")
text_file.write(webinfo)
text_file.close()

'''
idk = soup.find_all("cui-page-list")
for ite in idk:
    print(ite)
'''

while True:
    newPage = '&page=%d' %(initial+1)
    urlCopy = pageUrl.replace('&page=1', newPage)
    page = requests.get(urlCopy)
    tree = html.fromstring(page.content)
    cars = tree.xpath('//*/div/div[2]/h2/a/text()')
    prices = tree.xpath('//*/div/div[2]/span[1]/text()')
    if len(cars) == 0:
        break;
    else:
        initial +=1
        carType.extend(cars)
        carPrice.extend(prices[:len(cars)])

'''
print ('Car:', carType)
print ('Prices:', carPrice)
'''

'Put all information into list'

data = []

for i in range(len(carType)):
    key = str(carType[i]).strip()
    if str(carPrice[i]) != "Not Priced":
        value = int(Decimal(sub(r'[^\d.]', '', carPrice[i])))
    else:
        value = str(carPrice[i])
    info = carData(key,value)
    data.append(info)
    'data.append(zip(key,value))'

'filter out car set not priced'
data_priced = [info for info in data if type(info.price) == int ]

average = {}
count = {}
for data in data_priced:
    if data.name not in average:
        average[data.name] = data.price
        count[data.name] = 1
    else:
        average[data.name] += data.price
        count[data.name] +=1

average = {k: int(average[k]/count[k]) for k in average.keys() & count}     

print(average)

'''
for i in data:
    print(i.name, ": ", i.price)
'''
'''
print(len(cars))
print(len(prices))
'''