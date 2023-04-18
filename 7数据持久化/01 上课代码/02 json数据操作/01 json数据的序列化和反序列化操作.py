# 列表和字典数据可以直接转json格式

# {}  []
import json  # 内置模块


data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
"""
json序列化操作: 把对象转化成json字符串
"""
json_str = json.dumps(data)
print(json_str)
print(type(json_str))


"""
json反序列化操作: 把json字符串转化成python对象
"""
str1 = '["1", "2"]'
json_obj = json.loads(str1)
print(json_obj)
print(type(json_obj))