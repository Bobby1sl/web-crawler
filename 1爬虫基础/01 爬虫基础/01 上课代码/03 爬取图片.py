# coding=utf-8
# 指定当前py文件编码
import requests
import re  # 正则表达式匹配模块

url = 'https://www.hexuexiao.cn/a/124525.html'
response = requests.get(url)
print(response.text)

# 解析小说数据
"""
<a class="btn btn-default btn-xs" href="https://i.hexuexiao.cn/up/da/75/47/f59543039ce27d69ef5d25b5a04775da.jpg.source.jpg" role="button" target="_blank">


<a class="btn .*?" href="(.*?)" role="button" targe.*?


"""
result = re.findall('<a class="btn .*?" href="(.*?)" role="button" targe.*?',
           response.text,
           re.S)

print(result)


# 图片地址得到了, 需要继续请求图片数据
# 图片, 视频 , 音频 是属于二进制数数据
img_response = requests.get(result[0])
img_data = img_response.content  # .content  提取对象里面的二进制内容
# print(img_data)

file_name = result[0].split('/')[-1]
print(file_name)

# contend = result[0].replace('\u3000\u3000', '').replace('<br /><br />', '\n')
# # print(contend)

# 保存数据
with open(file_name, mode='wb') as f:
    f.write(img_data)