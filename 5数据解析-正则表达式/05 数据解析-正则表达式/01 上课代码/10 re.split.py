import re

string = 'Pythonasdkjasd 464654 adhuiaghsdk 564654 akjsdhkashdkja'


"""
pattern     正则规则
string      需要分割的字符串
maxsplit    最大分割次数
flags       匹配模式
"""
result = re.split('\d+', string, maxsplit=1)
print(result)
