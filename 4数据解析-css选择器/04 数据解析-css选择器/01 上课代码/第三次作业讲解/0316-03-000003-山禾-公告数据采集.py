"""
    目标网址: http://www.zfcg.sh.gov.cn
    作业要求:
            1. 点击页面导航栏中 "采购公告" 栏目
            2. 采集下面公告信息数据, 需要采集以下数据:
                title  公告标题
                url    公告详情页地址
                districtName 公告区域
            3. 采集完后打印输出即可
请在下方完成代码:
"""

import requests

url = 'http://www.zfcg.sh.gov.cn/front/search/category'
json_data = {
    "utm": "sites_group_front.2ef5001f.0.0.07ec2550d86011edb93db70f086e4f9a",
    "categoryCode": "ZcyAnnouncement3012",
    "pageSize": '15',
    "pageNo": '1'
}

# json 主要是以json字符串提交的请求参数
response = requests.post(url=url, json=json_data)
print(response.json())

for res in response.json()['hits']['hits']:
    title = res['_source']['title']
    detail_url = res['_source']['url']
    districtName = res['_source']['districtName']
    print(title, detail_url,districtName)
