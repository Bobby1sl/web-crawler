"""
	目标网址：https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76
	
	要求：
		1、请求上述网址的数据
		2、把获取到的数据保存到json文件中
            文件命名: data.json
            需要在文件中看到json字符串
			
请在下方编写代码
"""
import json
import requests


url = 'https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76'

response = requests.get(url=url)
json_data = response.json()
# json_data = response.text  # 用text提取json数据会有编码问题, 使用的是unicode--> \u515
print(json_data)

# 序列化
json_str = json.dumps(json_data, ensure_ascii=False)
print(json_str)

with open('data.json', mode='w', encoding='utf-8') as f:
    f.write(json_str)

