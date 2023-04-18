import re


email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]

for email in email_list:
    result = re.match('^\w*@\w*\.com$', email)
    if result:
        print(f' {email} 是规范的邮箱地址, 地址是 {result.group()}')
    else:
        print(f' {email} 不是规范的邮箱地址')

# 约束字符(.*?)
