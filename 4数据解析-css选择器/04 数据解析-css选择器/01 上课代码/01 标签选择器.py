# 简化的html标签
html = """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>标签选择器</title>
</head>
<style>
	p{
		color: #f00;
		font-size: 16px;
	}
</style>
<body>
	<p>css标签选择器的介绍</p>
	<p>标签选择器、类选择器、ID选择器</p>
	<a href="https://www.baidu.com">百度一下</a>
	<span> 我是一个span标签</span>
</body>
</html>
"""

# 所有的html数据其类型是字符串类型  response.text
# 假设 html 是我请求过来的数据
# 只有 selector 对象可以调用数据解析方法

import parsel  # parsel 数据解析模块, 第三方模块 pip install parsel


# 1. 转化类型
selector = parsel.Selector(html)
print(selector)

# 2. 根据转化后的对象解析数据
result = selector.css('p')
print(result)
result = selector.css('p').getall()
print(result)

# p  代表标签选择器, 直接根据标签的名字定位标签数据
result = selector.css('p').get()
print(result)

result = selector.css('a').getall()
print(result)


# get() 从 Selector 对象中提取第一个数据, 直接返回字符串数据给我们
# getall() 从 Selector 对象中提取提取所有数据, 返回一个列表

# 在css语法中 空格代表取后代标签<子标签, 孙子标签, 重孙子标签 ....>
# 在css语法中 > 代表仅取子标签