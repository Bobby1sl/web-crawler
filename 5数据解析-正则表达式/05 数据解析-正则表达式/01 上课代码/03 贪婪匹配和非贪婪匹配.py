text = """_
回复(2)4楼2018-07-04 11:48

    哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com
Super劫Zed: 999999999@qq.com
Super劫Zed: 666666666@qq.com
2018-8-8 16:00回复
我也说一句

Super劫Zed: 540775360@qq.com
Super劫Zed: 999999999@qq.com
Super劫Zed: 666666666@qq.com

RAVV2017
物联硕士4
"""

import re

"""
贪婪匹配: 默认模式, 在满足正则表达式规则的前提下, 会尽可能多匹配数据

.*?   代表非贪婪模式
?   匹配一次或者0次
"""

result = re.findall('Super劫Zed: .*@qq.com', text, re.S)
print(result)

result = re.findall('Super劫Zed: .*?@qq.com', text, re.S)
print(result)