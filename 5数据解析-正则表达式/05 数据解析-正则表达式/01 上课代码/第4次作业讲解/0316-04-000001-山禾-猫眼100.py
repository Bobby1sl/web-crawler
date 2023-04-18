"""
    使用 css 选择器将猫眼 100 全部电影信息全部提取出来。
    目标网址：https://m.maoyan.com/asgard/board/4

    name（电影名）
    star（主演）
    releasetime（上映时间）
    score（评分）
	
	提取出来print（）打印即可
"""
import requests
import parsel


# 1. 找数据地址
url = 'https://m.maoyan.com/asgard/board/4'
headers = {
    'Cookie': 'iuuid=9DED7A10B17C11ECB1EFC3BD08D8135DA8FA319C52714E4EBC6C74008CD8840E; ci=70%2C%E9%95%BF%E6%B2%99; ci=70%2C%E9%95%BF%E6%B2%99; ci=70%2C%E9%95%BF%E6%B2%99; _lxsdk_cuid=1803c6fc140c8-03e4923d825316-1734337f-1fa400-1803c6fc140c8; _lxsdk=9DED7A10B17C11ECB1EFC3BD08D8135DA8FA319C52714E4EBC6C74008CD8840E; _lxsdk_s=18760a390d9-6c5-b03-453%7C%7CNaN; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1680953545; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1680953545',
    'Host': 'm.maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

# 2. 发送数据请求
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
html_data = response.text
# print(html_data)

# 3.数据解析
# 3.1 转数据类型
selector = parsel.Selector(html_data)

# 3.2 数据提取
"""一次提取"""
divs = selector.css('.clearfix')
# print(divs)
# print(len(divs))

for div in divs:
    title = div.css('.title::text').get()
    actors = div.css('.actors::text').get()
    date = div.css('.date::text').get()
    number = div.css('.number::text').get()
    print(number)

