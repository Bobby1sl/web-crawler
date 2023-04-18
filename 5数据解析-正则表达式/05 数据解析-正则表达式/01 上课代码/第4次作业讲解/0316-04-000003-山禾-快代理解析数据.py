"""
    使用 css 选择器将快代理中我需要的信息提取出来。
    目标网址：https://www.kuaidaili.com/free/
    
    需要解析以下数据:
        ip、
        port、
        类型
	
	提取出来print（）打印即可
"""
import parsel
import requests

# 1. 找数据地址
url = 'https://www.kuaidaili.com/free/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

# 2. 发送数据请求
response = requests.get(url, headers=headers)
html_data = response.text
# print(html_data)  # 在解析数据之前一定要打印数据查看有没有获取到

# 3.数据解析
# 3.1 转数据类型
selector = parsel.Selector(html_data)

# 3.2 数据提取
"""一次提取"""
trs = selector.css('tbody>tr')
# print(trs)
# print(len(trs))

"""二次提取"""
for tr in trs:
    ip = tr.css('td:nth-child(1)::text').get()
    port = tr.css('td:nth-child(2)::text').get()
    type_ = tr.css('td:nth-child(4)::text').get()
    print(ip, port, type_)

print('-----------------------------------------\n')

