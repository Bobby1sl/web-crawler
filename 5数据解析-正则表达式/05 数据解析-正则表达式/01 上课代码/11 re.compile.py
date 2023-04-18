import re

str1 = "540775360@qq.com"
str2 = "python = 9999， c = 7890， c++ = 12345"
str3 = "python = 997"


# re.compile()   将正则表达式编译成一个对象
# 已经编译好的对象可以重复多次使用
# 在python解释器底层, 首先会对正则表达式语法进行编译
# 已经编译好的正则对象, 在python解释器底层就不会编译了
pattern = re.compile('\d+')
print(pattern)

result1 = re.findall(pattern, str1)
print(result1)
result2 = re.findall(pattern, str2)
print(result2)
result3 = re.findall(pattern, str3)
print(result3)

