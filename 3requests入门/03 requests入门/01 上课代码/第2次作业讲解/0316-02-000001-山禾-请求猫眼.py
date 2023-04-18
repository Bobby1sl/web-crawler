"""
	目标地址：https://m.maoyan.com/asgard/board/4
	
	要求：
		1、请求到目标网址数据，需要在请求到的数据中看到当前页面所有的电影名字、主演、上映时间、评分等信息
		2、请列举在请求不到数据时，需要添加几个常见请求头字段（课程讲过）
		
请在下方编写代码
"""
import requests


url = 'https://m.maoyan.com/asgard/board/4'
headers = {
    'Cookie': 'iuuid=9DED7A10B17C11ECB1EFC3BD08D8135DA8FA319C52714E4EBC6C74008CD8840E; ci=70%2C%E9%95%BF%E6%B2%99; ci=70%2C%E9%95%BF%E6%B2%99; ci=70%2C%E9%95%BF%E6%B2%99; _lxsdk_cuid=1803c6fc140c8-03e4923d825316-1734337f-1fa400-1803c6fc140c8; _lxsdk=9DED7A10B17C11ECB1EFC3BD08D8135DA8FA319C52714E4EBC6C74008CD8840E; _lxsdk_s=18760a390d9-6c5-b03-453%7C%7CNaN; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1680953545; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1680953545',
    'Host': 'm.maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
html_data = response.text
print(html_data)

"""
User-Agent: 浏览器的身份标识
Host: 指定想要访问服务器的域名
Referer: 防盗链
Origin: 申明资源的起始位置
cookies: 用户身份的标识, 能不加就不加
"""