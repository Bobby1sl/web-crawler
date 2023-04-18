# coding=utf-8
# 指定当前py文件编码
import requests
import parsel

# 找数据地址
url = 'https://www.bqg78.com/book/1031/1.html'

# 发送请求
response = requests.get(url)
print(response.text)

# 3. 解析数据
# 3.1 转化对象
selector = parsel.Selector(response.text)
print(selector)
# 3.2 提取数据
name_ = selector.css('div.content>h1::text').getall()
print(name_)

contend = selector.css('#chaptercontent::text').getall()
print(contend)


