import requests

response = requests.get('https://www.baidu.com/')
response.encoding = response.apparent_encoding  # 自动识别响应体编码
print(response.text)

# response  # 查看响应体体信息

"""获取数据的属性和方法"""
# print(response.text)  # 获取响应体字符串数据 --> str
# print(response.content)  # 获取响应体二进制数据
# print(response.json())  # 获取响应体 json 数据, 如果数据格式不是json数据格式, 那么报错

"""查看响应体其他内容"""
print(response.headers)  # 查看响应体的响应头信息
print(response.encoding)  # 指定响应体编码
print(response.apparent_encoding)  # 自动识别响应体编码

print(response.cookies)  # 获取响应体的 cookies 字段信息, 得到的是 RequestsCookieJar对象
print(response.cookies.get_dict())  # RequestsCookieJar对象转化成字典
print(response.url)  # 获取响应体的url地址
print(response.status_code)  # 获取响应体状态码

