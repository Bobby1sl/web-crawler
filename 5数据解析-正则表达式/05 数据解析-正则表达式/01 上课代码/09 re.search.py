import re

string = '00PythonahsdgjasghPythonasdjajsk'

# re.search  可以在字符串中的任意位置查找指定的字符串, 找到了就返回, 有且仅返回一次数据
result = re.search('Python', string)
print(result)
print(result.group())  # group() 将对象里面的数据取出
