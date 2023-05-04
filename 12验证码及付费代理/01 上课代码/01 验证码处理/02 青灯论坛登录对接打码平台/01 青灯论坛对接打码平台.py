import time

import requests


def get_time():
    now_time = str(int(time.time() * 1000))
    print('当前时间戳:', now_time)
    return now_time


# 创建一个会话维持对象
session = requests.Session()  # 具有所有requests请求方法

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
cookies = {'hello': '681976911'}

"""保存验证码"""
now_time = get_time()  # 获取时间戳
img_url = 'http://118.126.88.143:5000/login/captcha?image_code=' + now_time
print(img_url)

img_response = session.get(url=img_url, headers=headers, cookies=cookies)
with open('yzm.png', mode='wb') as f:
    f.write(img_response.content)

# # 手动输入验证码
# code = input('请输入验证码:')
# print('您输入的验证码为: ', code)

# 对接打码平台自动识别验证码
from img_api import base64_api  # 导入识别函数

result = base64_api('yzm.png', 1001)
print('验证码识别结果为:', result)

"""发送模拟登录请求"""
json_data = {
    "captcha_code": result,  # 验证码
    "image_code": now_time,  # 时间戳
    "password": "123456",  # 密码
    "username": "admin"  # 用户名
}

login_url = 'http://118.126.88.143:5000/api/private/v1/login'

sms_response = session.post(url=login_url, json=json_data)
print(sms_response.json())

# 打印查看登录后的cookie
print(sms_response.cookies.get_dict())

