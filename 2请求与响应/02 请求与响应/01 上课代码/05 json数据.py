

"""json数据"""

# json数据是目前前后端主流的数据交换格式
# json数据本质上类型是字符串

"""
形式: 
    外层: {}  []
    内层: 嵌套的数据--> eg:{字段1: 值1, 字段2: [{嵌套字段1: 嵌套字段值1}, {}, {}, {}]}
    
在json数据中, 值必须是以下数据类型

字符串
数字
对象(json对象)<嵌套形式>
数组
布尔值
null

所有的json数据字段都是要用双引号表示
"""

import requests

# response = requests.get('https://news.163.com/special/cm_yaowen20200213/?callback=data_callback')
response = requests.get('https://pvp.qq.com/web201605/js/herolist.json')
print(response.text)  # 获取json字符串数据
print(response.json())  # 只要数据是规范的json数据, 用json()可以提取响应体的json数据
print(type(response.json()))  # 只要数据是规范的json数据, 用json()会在底层做数据类型转化



