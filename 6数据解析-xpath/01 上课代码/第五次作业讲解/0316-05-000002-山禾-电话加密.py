
"""
    根据下方出现的电话号码进行加密
    
    需求:
        最终效果: 181****5458

    使用正则表达式完成
"""
import re

def func(x):
    print(x)
    print(x.group())
    str_ = x.group()
    return str_[:3] + '****' + str_[-4:]

tel = "18123115458"


# func 函数传入的是一个函数名, 会被sub默认调用
result = re.sub('\d{11}', func, tel)
print(result)

# \\1 取第一个分组  \\2 第二个分组 ....
result = re.sub('(\d{3})(\d{4})(\d{4})', '\\1****\\3', tel)
print(result)