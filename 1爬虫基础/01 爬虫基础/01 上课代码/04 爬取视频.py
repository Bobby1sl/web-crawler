# coding=utf-8
# 指定当前py文件编码
import requests
import re  # 正则表达式匹配模块

url = 'https://video-qn.ibaotu.com/19/83/83/49Z888piC4I8.mp4'
response = requests.get(url)
print(response.content)


# 保存数据
with open('my.mp4', mode='wb') as f:
    f.write(response.content)