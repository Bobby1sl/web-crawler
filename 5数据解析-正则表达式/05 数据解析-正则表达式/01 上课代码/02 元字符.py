text = """_
回复(2)4楼2018-07-04 11:48

    哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com
2018-8-8 16:00回复
我也说一句

RAVV2017
物联硕士4
"""

import re

# . 在默认的情况下, 匹配除了换行符以外的任意字符
# re.S  模式匹配, 能够让 . 匹配到换行符
# 除了数量词和多次匹配以外, 一个元字符只能匹配一个字符串
result = re.findall('Super劫Zed: .................', text, re.S)
print(result)

"""
\d   匹配一个数字字符
\D   匹配一个非数字字符
"""
result = re.findall('Super劫Zed: \d\d\d\d\d\d\d\d\d', text, re.S)
print(result)
result = re.findall('Super劫Zed: \d\d\d\d\d\d\d\d\d\D\D\D\D\D\D\D\D', text)
print(result)

"""
\s    匹配空白字符(换行<\n> 制表符, tab \r\n)
\S    匹配非空白字符
"""
result = re.findall('\s', text)
print(result)
result = re.findall('\S', text)
print(result)

# """
# \w    匹配单词字符a-z A-Z _  还包括各个国家地区的语言文字
# \W    匹配非单词字符
# """
# result = re.findall('\w', text)
# print(result)
# result = re.findall('\W', text)
# print(result)
#
# """
# *   匹配前一个字符的零次或者多次(最少可以是零次)
# +   匹配前一个字符的一次或者多次(最少要只有一次)
#
# .*  匹配除了换行符以外的任意字符串零次或者多次
# .+  匹配除了换行符以外的任意字符串一次或者多次
# """
# result = re.findall('Super劫Zed: \d*', text)
# print(result)
# result = re.findall('Super劫Zed: \s*', text)
# print(result)
# result = re.findall('Super劫Zed: \s+', text)
# print(result)