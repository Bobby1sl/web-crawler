import requests

proxy_response = requests.get('http://127.0.0.1:5010/get')
# proxy = proxy_response.json()
print(proxy_response)

# requests.exceptions.ConnectionError  链接错误
# 原因:
    # 个人网络不好
    # 服务器问题