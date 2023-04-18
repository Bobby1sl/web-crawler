import requests


# def get_proxy():
#     url = 'http://demo.spiderpy.cn/get/'
#     response = requests.get(url=url).json()
#     ip_proxy = response['proxy']
#     # print(ip_proxy)
#
#     # 代理形式
#     """
#     proxies = {
#       "http": "http://10.10.1.10:3128",
#       "https": "http://10.10.1.10:1080",
#     }
#     """
#
#     proxies = {
#         "http": "http://" + ip_proxy,
#         "https": "http://" + ip_proxy,
#     }
#     return proxies


def get_proxy():
    url = 'http://zltiqu.pyhttp.taolop.com/getip?count=1&neek=13873&type=2&yys=0&port=2&sb=&mr=2&sep=0&ts=1'
    response = requests.get(url=url)
    json_data = response.json()
    # print(json_data)

    ip_port = json_data['data'][0]['ip'] + ":" + str(json_data['data'][0]['port'])
    # print(ip_port)

    proxies = {
        "http": "http://" + ip_port,
        "https": "http://"  + ip_port,
    }
    return proxies

proxies = get_proxy()
print(proxies)
url = 'https://www.ku6.com/index'
# proxies关键是使用代理请求的关键字, 代理质量不好的话就会报错(requests.exceptions.ProxyError)
response = requests.post(url=url, proxies=proxies)
print(response.status_code)
print(response.text)

"""
报错可以异常重试
"""