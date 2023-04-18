import requests
requests.packages.urllib3.disable_warnings()  # 忽略关闭证书以后引发的警告

url = 'https://data.stats.gov.cn/'
# verify=False 发送请求的时候不校验证书
response = requests.post(url=url, verify=False)
print(response.text)

"""
requests.exceptions.SSLError:  网站没有证书引发的报错, 因为requests模块会默认校验证书
"""