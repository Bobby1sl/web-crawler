"""
表情包爬取
将此页面下表情包图片全部获取下来：https://www.biaoqingbao.net/gaoxiao/
"""
import re

"""请下下方开始编写代码"""
import requests


url = 'https://www.biaoqingbao.net/gaoxiao/'
response = requests.get(url)
html_data = response.text
# print(html_data)

# <img class="waitpic" src=".*?" data-original="(.*?)" alt=".*?" >
result = re.findall('<img class="waitpic" src=".*?" data-original="(.*?)" alt=".*?" >', html_data, re.S)
# print(result)

for img_url in result:
    img_data = requests.get(img_url).content
    # 文件名
    file_name = img_url.split('/')[-1]

    with open('img\\' + file_name, mode='wb') as f:
        f.write(img_data)
        print('保存完成:', file_name)