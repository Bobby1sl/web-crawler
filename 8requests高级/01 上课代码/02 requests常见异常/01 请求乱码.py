import requests

url = 'https://m.maoyan.com/asgard/board/4'

# 2. 发送数据请求
response = requests.get(url)
# response.encoding = response.apparent_encoding  # 自动识别响应体编码
response.encoding = 'utf-8'  # 手动指定编码
html_data = response.text
print(html_data)

# gbk  gb2312  gb18030  utf-8  utf-8-sig  🐎 😰
