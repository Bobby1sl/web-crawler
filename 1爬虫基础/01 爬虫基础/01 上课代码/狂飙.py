"""
=========================
File Name:狂飙.py
Author:Bobby
Date:2023/4/6 14:46
==========================
"""
import requests

url = 'https://www.zjhsgl.com/vodplay/66643-1-1.html'  # 将url替换为要获取的资源链接
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    with open('狂飙.mp4', 'wb') as f:
        f.write(response.content)
