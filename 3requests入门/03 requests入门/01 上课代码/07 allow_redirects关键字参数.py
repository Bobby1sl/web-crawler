import requests

url = 'http://github.com/'
# allow_redirects=False 阻止重定向
response = requests.post(url=url, allow_redirects=False)
print(response.status_code)
print(response.url)

"""
报错可以异常重试
"""