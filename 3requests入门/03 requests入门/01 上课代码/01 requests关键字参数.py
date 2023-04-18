import requests


url = 'https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76'
response = requests.get(url=url)
print(response.url)

"""
method: 请求方法  get  post
url: 请求的链接地址

headers: (可选的) 构建请求头字段的关键字参数, 构建字典
cookies: (可选的) 通过这个关键字传递cookies字段信息, 构建字典
proxies: (可选的) ip代理的关键字参数, 构建字典

params: (可选的) 构建查询参数的关键字
data: (可选的) 构建请求参数的关键字
json: (可选的) 以 json 数据提交的请求参数关键字, 构建字典

timeout: (可选的) 设置响应时间, 单位/秒, 如果超过这个时间程序会报错
allow_redirects: (可选的) 是否允许重定向, 默认如果发生了重定向, 会自动重定向, 设置布尔值
verify: (可选的) 是否验证网站证书  ca证书  ssl证书, 默认为Ture, 默认会校验证书

files: (可选的) 文件操作
stream: (可选的) 数据流数据, 是都是数据流数据, 实时更新的数据
"""
