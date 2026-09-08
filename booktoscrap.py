import requests
from bs4 import BeautifulSoup
import csv
import logging

logging.basicConfig(
    filename="scrapper.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)
successful_books = 0
failed_pages = 0

csv_file=open("books.csv",'w',newline='',encoding='utf-8')
csv_writer=csv.writer(csv_file, quoting=csv.QUOTE_ALL)
csv_writer.writerow(["name","price","availability"])
errors=[]

for page in range(1,51):
    try:
        url=f'https://books.toscrape.com/catalogue/page-{page}.html'
        rsp=requests.get(url,timeout=5).text
        soup=BeautifulSoup(rsp, 'html.parser')

        for article in soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"):
            try:
                name=article.h3.a['title']
            except AttributeError:
                name="NAME NOT FOUND"
                logging.warning(f"Page{page}:could not find book name")
            try:
                prod=article.find('div',class_="product_price")
                price=prod.p.text
            except AttributeError:
                price="PRICE NOT FOUND"
                logging.warning(f"Page {page}: Could not find price for {name}")
            try:
                availability=prod.find("p",class_='instock availability').text.strip()
            except AttributeError:
                availability="AVAILABILITY NOT FOUND"
                logging.warning(f"Page {page}: Could not find availability for {name}")
            print(name)
            print(price)
            print(availability)
            csv_writer.writerow([f'"{name}"' , f'"{price}"' , f'"{availability}"'])
            successful_books += 1
            logging.info(f"Page {page}: Scraped {name}")
    except requests.exceptions.Timeout:
        failed_pages += 1
        error_msg = f"Page {page}: Connection timeout (took too long)"
        logging.error(error_msg)
        print(f"ERROR: {error_msg}")
    except requests.exceptions.ConnectionError:
        failed_pages += 1
        error_msg = f"Page {page}: Connection failed (can't reach website)"
        logging.error(error_msg)
        print(f"ERROR: {error_msg}")
    except Exception as e:
        failed_pages += 1
        error_msg = f"Page {page}: Unknown error - {str(e)}"
        logging.error(error_msg)
        print(f"ERROR: {error_msg}")
csv_file.close()


with open("errors.txt", "w") as error_file:
    for error in errors:
        error_file.write(error + "\n")

print("\n" + "="*50)
print("SCRAPING COMPLETE!")
print("="*50)
print(f"Successfully scraped: {successful_books} books")
print(f"Failed pages: {failed_books}")
print(f"Check 'books.csv' for data")
print(f"Check 'scraper.log' for details")
print("="*50)

logging.info(f"Scraping finished: {successful_books} books scraped, {failed_books} pages failed")