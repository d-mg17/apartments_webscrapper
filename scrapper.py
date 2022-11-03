from bs4 import BeautifulSoup as BS
import requests
import csv
import re
from sys import argv

area = argv[1]
filename = argv[2]

if "," in area:
    area.replace(",", "&RentalsPueblos=")

url = f'https://www.clasificadosonline.com/UDRentalsListingAdv.asp?RentalsPueblos={area}&%FCez&Category=Apartamento%2FWalkUp&Bedrooms=%25&LowPrice=0&HighPrice=9999999999999999&Area=&IncPrecio=1&redirecturl=%2FUDRentalsListingAdvMap.asp&BtnSearchListing=Listado'

'''
url = f'https://www.clasificadosonline.com/UDRentalsListingAdv.asp?RentalsPueblos={area}&%FCez&Category=Apartamento%2FWalkUp&Bedrooms=%25&LowPrice=0&HighPrice=9999999999999999&IncPrecio=1&Area=&redirecturl=%2FUDRentalsListingAdvMap%2Easp&BtnSearchListing=Listado&offset=30'
'''
page = requests.get(url)
html = BS(page.content, 'html.parser')
lists = html.find_all('div', class_= 'dv-classified-row dv-classified-row-v2')

with open(filename, 'w', encoding='utf8', newline='') as f:
    mywriter = csv.writer(f)
    header = ['Title', 'Location', 'Price/Month']
    mywriter.writerow(header)
    
    for list in lists:
        
        title = list.find('span', class_="link-blue-color").text.replace('\n','').strip()
        
        location_list = list.find_all('span', style="color: blue !important;")
        location = location_list[0].text.replace('\n','').strip() +' , '+  location_list[1].text.replace('\n','').strip()
        
        price = list.find('span', class_="Tahoma16BrownNound").find('font').text.replace('\n','').strip()
        if price[0] == ',': 
            price = price.replace(',','$',1)
        
        apartment= [title,location,price]
        mywriter.writerow(apartment)