import requests

try:
    proxy_response = requests.get('http://127.0.0.1:5010/get', timeout=0.1)
    print(proxy_response)

except:
    print('开始异常重试')
    proxy_response = requests.get('http://127.0.0.1:5010/get', timeout=0.1)
    print(proxy_response)

