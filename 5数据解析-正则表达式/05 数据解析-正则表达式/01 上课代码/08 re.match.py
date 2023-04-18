import re

string = 'PythonahsdgjasghPythonasdjajsk'

# re.match  匹配字符串中头部内容, 如果字符串的最前面没有你要查找的内容就会报错, 只会找头部
result = re.match('Python', string)
print(result)
print(result.group())  # group() 将对象里面的数据取出
print(result.span())  # group() 将对象里面的数据取出
