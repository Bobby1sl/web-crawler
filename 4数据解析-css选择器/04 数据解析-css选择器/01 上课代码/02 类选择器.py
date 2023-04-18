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
	<p class="top">css标签选择器的介绍</p>
	<p class="top">标签选择器、类选择器、ID选择器</p>
	<a href="https://www.baidu.com">百度一下</a>
	<span> 我是一个span标签</span>
</body>
</html>
"""

import parsel  # parsel 数据解析模块, 第三方模块 pip install parsel


selector = parsel.Selector(html)

# . 代表提取标签的类型
# 具有相同类属性的标签都会被提取
# 类选择器可以通过标签的类属性(class属性)精确定位到你想要的标签
# 只有标签具有 class 属性才可以用类选择器提取对应得标签
# 如果类属性中有空格, 需要将空格替换成 .   因为空格在css语法中有特殊含义
result = selector.css('.top').getall()
print(result)


