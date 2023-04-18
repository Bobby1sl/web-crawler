"""
    - 课上肯德基案例, 将 北京,上海,广州 三个城市的门店信息获取下来
	- 获取下来的信息用print函数打印即可
	
请在下方实现代码:
"""
import requests


url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

def get_page(city_name):
    data = {
        'cname': '',
        'pid': '',
        'keyword': city_name,
        'pageIndex': '1',
        'pageSize': '10',
    }
    json_data = requests.post(url=url, data=data).json()
    count = json_data['Table'][0]['rowcount']
    # print(count)

    if count % 10 > 0:
        page_num = count // 10 + 1
    else:
        page_num = count // 10

    return page_num

def send_request(city):
    page_num = get_page(city)

    count = 1
    print(f'======================正在获取{city}地区的数据=====================')
    for page in range(1, page_num + 1):
        url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
        params = {'op': 'keyword'}
        data = {
            'cname': '',
            'pid': '',
            'keyword': city,
            'pageIndex': str(page),
            'pageSize': '10'
        }  # 构建请求参数

        # data 关键字构建请求参数的关键字
        response = requests.post(url=url, params=params, data=data)
        json_data = response.json()
        # print(json_data)

        res_data = json_data['Table1']

        for res in res_data:
            storeName = res['storeName']
            addressDetail = res['addressDetail']
            cityName = res['cityName']
            pro = res['pro']
            print(count, storeName, addressDetail, cityName, pro, sep=' | ')
            count += 1



# print(get_page('北京'))
if __name__ == '__main__':

    city_list = ['北京','上海','广州']
    for i in city_list:
        send_request(i)

