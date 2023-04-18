import requests
import parsel

# 1. 找数据地址
url = f'https://movie.douban.com/top250?start=0&filter='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

# 2. 发送数据请求
response = requests.get(url, headers=headers)
html_data = response.text
# print(html_data)  # 在解析数据之前一定要打印数据查看有没有获取到

# 3.数据解析
# 3.1 转数据类型
selector = parsel.Selector(html_data)

# 3.2 数据提取
"""一次提取"""
lis = selector.xpath('//*[@class="grid_view"]/li')
print(lis)
print(len(lis))

"""二次提取"""
for li in lis:
    title = li.xpath('.//*[@class="title"]/text()').get()
    info = li.xpath('.//*[@class="bd"]/p[1]/text()').getall()
    info = ' | '.join([i.strip() for i in info])
    score = li.xpath('.//*[@class="rating_num"]/text()').get()
    follow = li.xpath('.//*[@class="inq"]/text()').get()
    commom = li.xpath('.//*[@class="star"]/span[4]/text()').get()
    print(title, info, score, follow, commom)

# css 和 xpath 是很像的
