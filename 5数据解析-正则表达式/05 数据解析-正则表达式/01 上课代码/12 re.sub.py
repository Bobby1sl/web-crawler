import re


string = 'Pythonasdkjasd Java adhuiaghsdk Java akjsdhkashdkja'

result = re.sub('Java', 'python', string, count=1)
print(result)


def func(x):
    # 可以在函数内部写替换逻辑
    return 'python'


result = re.sub('Java', func, string)
print(result)


"""
pattern 匹配规则
repl    匹配的数据替换成什么字符, 可以自定义函数规则
string  在哪个字符串匹配
count   替换的次数
flags   匹配模式
"""

