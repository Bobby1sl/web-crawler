import requests

proxy_response = requests.get('http://127.0.0.1:5010/get', timeout=0.1)
# proxy = proxy_response.json()
print(proxy_response)

"""
ConnectTimeout: 连接超时
timeout: 指定需要在多久返回数据, 单位是秒
一旦你请求的时间超过你设置的时间, 整个程序会报错
"""