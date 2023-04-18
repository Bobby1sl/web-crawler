# coding=utf-8
# 指定当前py文件编码
import requests
import parsel

# 找数据地址
url = 'https://www.bqg78.com/book/1031/'

# 发送请求
response = requests.get(url)
# print(response.text)


with open('a1.html', mode='w', encoding='utf-8') as f:
    f.write(response.text)
# 3. 解析数据
selector = parsel.Selector(response.text)


"""第一次提取: 首先提取所有需要的标签"""
dds = selector.css('.listmain>dl dd:nth-child(1)')
print(dds)
print(len(dds))


# # 只有 selector 对象可以调用数据解析方法
# """二次提取: 针对每一个需要的标签进行提取"""
# for dd in dds:  # 遍历每一个 selector 标签对象
#     title = dd.css('a::text').get()
#     href = dd.css('a::attr(href)').get()
#     print(title, href)

# 当提取不到数据的时候， 可以从一下几个方面考虑
# 1. 数据有没有获取到， 打印查看
# 2. 可能是解析语法问题


