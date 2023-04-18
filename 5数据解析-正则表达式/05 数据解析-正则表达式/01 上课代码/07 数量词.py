text = """
回复(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com
Super劫Zed: 1117753456460@qq.com
Super劫Zed: 2224568775360@qq.com
2018-8-8 16:00回复
我也说一句

RAVV2017
物联硕士4
以上的邮箱，已发，还需要的请回复邮箱。两套物联网学习资料。

回复(4)7楼2018-07-04 16:06

儒雅的刘飞3
初识物联1
397872410@qq.com，谢谢楼主

收起回复8楼2018-07-04 16:20

RAVV2017: 已发送，麻烦请查收，谢谢
2018-7-4 16:23回复
我也说一句

该来的总会来
物联博士5
1459543548@qq.com
谢谢谢谢

回复9楼2018-07-04 17:18来自Android客户端
BLACKPINK_罗捷
深入物联2
1228074244@qq.com
"""

import re


# []  表示字符集,一个[]只能匹配一个字符串, 字符集里面罗列的内容才可以匹配
result = re.findall('[0-9]*@qq.com', text)
print(result)


# {start,stop}  表示数量词, 限制前一个字符的匹配数量, 闭区间
result = re.findall('[0-9]{5,11}@qq.com', text)
print(result)

