"""
=========================
File Name:斗鱼直播人气.py
Author:Bobby
Date:2023/4/6 15:02
==========================
"""
import requests
from bs4 import BeautifulSoup

url = 'https://www.douyu.com/g_LOL'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

rank_list = soup.find('div', {'class': 'rank-list'})  # 找到人气榜的div
items = rank_list.find_all('li')  # 找到所有的直播间

for item in items:
    title = item.find('h3', {'class': 'ellipsis'}).text  # 直播间标题
    nickname = item.find('span', {'class': 'dy-name ellipsis fl'}).text  # 直播间主播名
    viewer = item.find('span', {'class': 'dy-num fr'}).text  # 直播间观众人数
    print(f'{title}, {nickname}, {viewer}')

