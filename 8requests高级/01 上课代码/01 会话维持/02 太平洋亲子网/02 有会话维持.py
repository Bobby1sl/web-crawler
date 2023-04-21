import requests


session = requests.Session()
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

"""模拟登陆获取用户权限"""
data = {
    'return': 'https://my.pcbaby.com.cn/user/adminIndex.jsp',
    'bindUrl': 'https://my.pcbaby.com.cn/passport/bindMobile.jsp?return=https://my.pcbaby.com.cn/user/adminIndex.jsp',
    'username': 'mb51222353',
    'password': '123456..',
    'auto_login': '30',
    'checkbox': 'on',
}

login_url = 'http://passport3.pcbaby.com.cn/passport3/passport/login_ajax_do_new.jsp?req_enc=UTF-8'

login_response = session.post(url=login_url, data=data, headers=headers)
# print(login_response.status_code)
print(login_response.json())

print('登录后的cookies: ', login_response.cookies.get_dict())

my_home_url = 'https://my.pcbaby.com.cn/user/adminIndex.jsp'

response = session.get(url=my_home_url)
# print(response.text)
# print(response.status_code)

with open('管理中心页面.html', mode='w', encoding='gb2312') as f:
    f.write(response.text)

"""
怎么抓取用户登录后的数据?

    1. 通过代码做模拟登陆
    2. 用session维持登录状态
    3. 用登录状态请求需要抓取的数据
"""

