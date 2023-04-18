"""
=========================
File Name:top250.py
Author:Bobby
Date:2023/4/13 15:33
==========================
"""
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

for i in range(10):
    url = f'https://movie.douban.com/top250?start={i * 25}'
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    movies = soup.select('.item')
    for movie in movies:
        title = movie.select('.title')[0].text
        rating = movie.select('.rating_num')[0].text
        print(title + ' ' + rating)
