
"""
官网地址: https://www.pcbaby.com.cn/
登录网页地址: https://my.pcbaby.com.cn/login.jsp?return=https%3A//www.pcbaby.com.cn/

账号: mb51222353
密码: 123456..

个人中心地址:
    https://my.pcbaby.com.cn/user/adminIndex.jsp
"""
import requests

my_home_url = 'https://my.pcbaby.com.cn/user/adminIndex.jsp'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

response = requests.get(url=my_home_url, headers=headers, allow_redirects=False)
print(response.text)
print(response.status_code)

with open('my.html', mode='w', encoding='gb2312') as f:
    f.write(response.text)