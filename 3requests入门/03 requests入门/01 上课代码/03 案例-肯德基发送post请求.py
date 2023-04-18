import requests


url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
params = {'op': 'keyword'}
data = {
    'cname': '',
    'pid': '',
    'keyword': '北京',
    'pageIndex': '1',
    'pageSize': '10'
}  # 构建请求参数

# data 关键字构建请求参数的关键字
response = requests.post(url=url, params=params, data=data)
json_data = response.json()
print(json_data)

res_data = json_data['Table1']

for res in res_data:
    storeName = res['storeName']
    addressDetail = res['addressDetail']
    cityName = res['cityName']
    pro = res['pro']
    print(storeName, addressDetail, cityName, pro, sep=' | ')

# 浏览器的地址导航栏只能发送get请求
#