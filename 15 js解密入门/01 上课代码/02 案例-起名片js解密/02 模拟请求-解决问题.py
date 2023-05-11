import json

import execjs
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

with open('02 企名片js解密.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()

compile_obj = execjs.compile(js_code)
result = compile_obj.call('s', response.json()['encrypt_data'])
print(result)

print(json.loads(result))
