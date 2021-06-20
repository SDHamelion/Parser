import requests
from bs4 import BeautifulSoup
import csv
CSV = 'mebel.csv' #Файл экселя
url = "https://planetadsp.ru/catalog/mebel/stoly-i-stulya/stulya-derevyannye/" #Ссылка для парсинга
base_url = "https://planetadsp.ru/catalog" #Коренная ссылка,но иногда может не пригодиться
response = requests.get(url) # берем html
html = response.text #переводим в текст
soup = BeautifulSoup(html, "html.parser")
products = soup.find_all("div",class_='wrapper') #ищем все значения
urls = [] #создаем лист куда будем закидывать ссылки
for product in products: # перебираем карточки и ищем ссылки
    product = product.select_one('div a')['href']
    urls.append(product) #записываем их
 #лист для значений
with open('mebel.csv','a',encoding='UTF-8',newline = '') as file:
    writer = csv.writer(file,delimiter = ';',)
    writer.writerow(['Название;' 'Цена;' 'Изображение;' 'Описание;' 'Характеристики;'])
for url in urls:
    args = []
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    # 'name': soup.select_one("h1").text
    # 'price': soup.select_one("span",{'class':'woocommerce-Price-amount amount'}).find_next('bdi').text[:6]
    # 'img': soup.select_one('figure',class_='woocommerce-product-gallery__wrapper').find('img').get('src')
    # 'description': soup.find("div", {"class":"product-info product-description"}).find_next("p").text
    # 'info':soup.select_one("table.woocommerce-product-attributes.shop_attributes").text
    name1 = str(soup.select_one("h1").text) + ';'
    price1 = str(soup.select_one("span",{'class':'woocommerce-Price-amount amount'}).find_next('bdi').text[:6]) + ';'
    img1 = str(soup.select_one('figure',class_='woocommerce-product-gallery__wrapper').find('img').get('src')) + ';'
    description1 = str(soup.select_one("div", {"class":"product-info product-description"}).find('div').get('p'))+ ';'
    info1 = str(soup.select_one("table.woocommerce-product-attributes.shop_attributes").text) + ';'
    args.append([name1,price1 ,img1,description1,info1 ])
    with open('mebel.csv','a',encoding='UTF-8',newline = '') as file:
        writer = csv.writer(file,delimiter = ';',)
        writer.writerow(args)

