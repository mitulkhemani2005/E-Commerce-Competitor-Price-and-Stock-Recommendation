from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime
import sqlite3

DATABASE = './data/sales.db'

text_pattern = re.compile(r'[a-zA-Z\s]+')
number_pattern = re.compile(r'[\d\.]+')

def scrap_data (product_url):
    response = requests.get(product_url)
    if response.status_code!=200:
        return ({'Message':'Link Not Valid'})
    
    soup = BeautifulSoup(response.content, 'html.parser')
    product_name = soup.find_all('span', class_='LMizgS')[0].text
    product_price = soup.find_all('div', class_='hZ3P6w bnqy13')[0].text
    product_price = float("".join(product_price[1:].split(',')))
    product_discount = soup.find_all('div',class_='HQe8jr rASMtN')[0].text
    product_discount = float(product_discount.split('%')[0])
    product_overall_rating = soup.find_all('div', class_ = 'MKiFS6')[0].text
    product_overall_rating = float(product_overall_rating)
    product_reviews_rating = soup.find_all('span', class_ = 'PvbNMB')[0].text
    product_review = int(product_reviews_rating.replace('Ratings','|').split('|')[0].strip().replace(',',''))
    product_rating = int(product_reviews_rating.replace('\xa0',' ').split('&')[1].strip().split(' ')[0].replace(',',''))
    try:
        product_stock = soup.find_all('div', class_='VkYRUs')[0].text
        product_stock
    except:
        product_stock = 'Available'
    seller_name_rating = soup.find_all('div', id='sellerName')[0].text
    seller_name = "".join(text_pattern.findall(seller_name_rating)).strip()
    seller_rating = "".join(number_pattern.findall(seller_name_rating))
    original_price = soup.find_all('div', class_='kRYCnD yHYOcc')[0].text
    original_price = float("".join(original_price[1:].split(',')))
    date = str(datetime.now().date())
    time = str(datetime.now().time())
    try:
        conn = sqlite3.connect(DATABASE, check_same_thread=False)
        curr = conn.cursor()
        curr.execute('''
            INSERT INTO sales (date, time, name, original_price, selling_price, discount, overall_rating, ratings, reviews, stock, seller_name, seller_rating, url)
            VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',(date, time, product_name, original_price, product_price, product_discount, product_overall_rating, product_rating, product_review, product_stock, seller_name, seller_rating, product_url

        ))
        conn.commit()
        conn.close()
        return ({"Message":"Data Scrapped and Saved in DataBase"})
    except Exception as ex:
        return ({"Message":f"Data Scrapped Error: {ex}"})

