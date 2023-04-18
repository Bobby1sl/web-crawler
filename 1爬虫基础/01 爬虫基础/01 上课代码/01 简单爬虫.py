import requests  # 数据请求模块  第三方模块  作用:模拟请求


# requests.get  表示构建一个请求  -> 请求体对象
# response --> 响应, <Response [200]> -> 响应体对象
response = requests.get('https://www.baidu.com/')
print(response)

# 对象, 具有对象的属性和方法
# .text  获取 Response 对象的文本内容
print(response.text)  # 字符串, 图片, 视频, 音频  二进制


"""
爬虫项目的实现步骤

1. 找数据所在的链接地址  <分析网页性质: 静态网页/动态网页>
2. 代码模拟请求地址数据
3. 数据提取, 提取需要的数据, 剔除不需要的数据
4. 数据保存(本地, 数据库)

"""