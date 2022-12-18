import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver # импорт модуля webdriver для работы с браузерами
from selenium.webdriver.common.by import By # импорт класса By для обозначения локаторов поиска
from selenium.webdriver.common.keys import Keys
import datetime


headers={'accept': '*/*',
         'user-agent': 'add_the_info'}
url='https://www.gismeteo.ru/catalog/russia/'
res=requests.get(url, headers=headers)
page=res.text
#сохранение кода главной страницы
with open(r'D:\1\pycharm project\parser_gismeteo vol.2\cities_list\page_gismeteo.html', 'w', encoding='utf-8') as p:
    p.write(page)

with open(r'D:\1\pycharm project\parser_gismeteo vol.2\cities_list\page_gismeteo.html', 'r', encoding='utf-8') as r:
    lead_page=r.read()

#поиск всех классов с городами
soup=BeautifulSoup(lead_page, 'lxml')
data=soup.find(class_='popular-cities').find(class_='catalog-list').find_all(class_='catalog-item')
cities_dict={}

#проход по каждому классу с информацией о городе
for i in data:
    group=i.find_all(class_='catalog-item-link')
    for j in group:
        url=j.find(class_='link-item link-popular').get('href')
        name=j.find('a').text
        cities_dict[name]=url

city_weather={}
count=0

#проход по ссылке для каждого города
for city in cities_dict.values():
    count+=1
    url=requests.get('https://www.gismeteo.ru'+city, headers=headers)
    page=url.text
    soup=BeautifulSoup(page, 'lxml')
    name=soup.find(class_='page-title').text
    temp=soup.find(class_='unit unit_temperature_c').text
    city_weather[name]= temp
    if count==15:
        break

for k, v in city_weather.items():
    print(k, v)


































