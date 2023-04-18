text = """

\
/
:
*
?
"
<
>
|
"""

import re


# []  表示字符集,一个[]只能匹配一个字符串, 字符集里面罗列的内容才可以匹配
result = re.findall(r'[\\/\:\*\?\"\<\>\|]', text)
print(result)

# 对于连续的字符或者数字的规则可以用一下写法
result = re.findall(r'[a-zA-Z0-9]', text)
print(result)

