"""
=========================
File Name:名言名句.py
Author:Bobby
Date:2023/4/6 15:05
==========================
"""
import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all('div', {'class': 'quote'})

for quote in quotes:
    text = quote.find('span', {'class': 'text'}).text  # 名言
    author = quote.find('small', {'class': 'author'}).text  # 作者
    print(f'{text} ——{author}')


# url = 'http://quotes.toscrape.com/'
#
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
#
# quotes = soup.find_all('div', {'class': 'quote'})
#
# with open('quotes.txt', mode='w', encoding='utf-8') as f:
#     for quote in quotes:
#         text = quote.find('span', {'class': 'text'}).text
#         author = quote.find('small', {'class': 'author'}).text
#         f.write(f'{text} ——{author}\n')
