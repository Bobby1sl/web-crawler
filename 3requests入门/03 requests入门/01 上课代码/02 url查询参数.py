import requests

"""
? 左边是请求地址, 右边是请求的查询参数
&   分隔每一个查询参数
所有的查询参数都是二值型的数 
"""

# url = 'https://pic.sogou.com/pics?query=%E9%A3%8E%E6%99%AF&mood=7&dm=0&mode=1'
url = 'https://pic.sogou.com/pics'  # ? 可加可不加

params = {
    'query': '风景',
    'mood': '7',
    'dm': '0',
    'mode': '1'

}

response = requests.get(url=url, params=params)
print(response.request.url)


"""
url编码: 默认在http协议中不支持中文字符, 会自动的经过url编码
# 组成部分: % 字母 数字
https://pic.sogou.com/pics?query=%E9%A3%8E%E6%99%AF&mood=7&dm=0&mode=1
"""
# requests.utils.quote('风景')  对指定的中文进行url编码
print(requests.utils.quote('风景'))
# requests.utils.unquote('%E9%A3%8E%E6%99%AF')  对指定的中文进行url解码
print(requests.utils.unquote('%E9%A3%8E%E6%99%AF'))