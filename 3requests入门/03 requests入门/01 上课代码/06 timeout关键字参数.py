import requests

url = 'https://github.com/'
# timeout=1  设置请求时间,单位秒, 超过时间就会报错, 可以通过异常捕获取处理
response = requests.post(url=url, timeout=0.1)
print(response.text)

"""
报错可以异常重试
"""