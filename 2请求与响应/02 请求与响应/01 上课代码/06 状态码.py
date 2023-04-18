import requests

response = requests.get('https://pvp.qq.com/web201605/js/herolist.json')
print(response.status_code)

"""
100 - 200   请求服务器已经接收到了
200 - 299   表示请求成功 200  206  207
300 - 399   重定向<你需要请求的资源已经移动到了另一个位置>
400 - 499   服务器无法找到资源位置, 地址错误  404  403
500 - 599   服务器内部出错, 是服务器问题 500

仅供参考
"""
