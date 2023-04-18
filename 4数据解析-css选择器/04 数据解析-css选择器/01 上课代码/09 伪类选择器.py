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
	<p class="top" id="contend">css标签选择器的介绍</p>
	<p class="top" id="contend">标签选择器、类选择器、ID选择器</p>
	<a href="https://www.baidu.com">百度一下</a>
	<span> 我是一个span标签</span>
</body>
</html>
"""

import parsel  # parsel 数据解析模块, 第三方模块 pip install parsel


selector = parsel.Selector(html)

# : 表示伪类选择器
# nth-child 满足标签的第几个元素
# (2) 选择满足标签的第二个元素, 类似索引, 从1开始取
result = selector.css('p:nth-child(2)::text').getall()
print(result)

