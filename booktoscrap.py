import requests
from bs4 import BeautifulSoup
import csv


csv_file=open("books.csv",'w',newline='',encoding='utf-8')
csv_writer=csv.writer(csv_file, quoting=csv.QUOTE_ALL)
csv_writer.writerow(["name","price","availability"])

for page in range(1,51):
    url=f'https://books.toscrape.com/catalogue/page-{page}.html'
    rsp=requests.get(url).text
    soup=BeautifulSoup(rsp, 'html.parser')

    for article in soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"):
        name=article.h3.a['title']
        prod=article.find('div',class_="product_price")
        price=prod.p.text
        availability=prod.find("p",class_='instock availability').text.strip()
        print(name)
        print(price)
        print(availability)
        csv_writer.writerow([f'"{name}"' , f'"{price}"' , f'"{availability}"'])

csv_file.close()