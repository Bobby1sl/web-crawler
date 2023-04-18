text = """_
回复(2)4楼2018-07-04 11:48

    哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 111111111@qq.com Super劫Zed: 222222222@qq.com
Super劫Zed: 999999999@qq.com Super劫Zed: 333333333@qq.com
Super劫Zed: 666666666@qq.com Super劫Zed: 777777777@qq.com
2018-8-8 16:00回复
我也说一句

RAVV2017
物联硕士4
"""

import re

"""
精确匹配: 先根据正则的语法匹配数据, 然后提取()内的数据
()        表示精确匹配, 匹配之后再提取括号内的

在正则语法中如果使用了多次精确匹配, 会返回一个列表嵌套元组的对象
"""


result = re.findall('Super劫Zed: (.*?)@qq.com', text, re.S)
print(result)

result = re.findall('Super劫Zed: (.*?)@qq.com Super劫Zed: (.*?)@qq.com', text, re.S)
print(result)
