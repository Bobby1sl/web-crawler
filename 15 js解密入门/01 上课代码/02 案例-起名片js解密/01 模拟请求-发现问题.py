import requests

url = 'https://vipapi.qimingpian.cn/DataList/productListVip'
headers = {
    'Host': 'vipapi.qimingpian.cn',
    'Origin': 'https://www.qimingpian.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}
data = {
    'time_interval': '',
    'tag': '',
    'tag_type': '',
    'province': '',
    'lunci': '',
    'page': '1',
    'num': '20',
    'unionid': ''
}
response = requests.post(url=url, data=data, headers=headers)
print(response.json())
