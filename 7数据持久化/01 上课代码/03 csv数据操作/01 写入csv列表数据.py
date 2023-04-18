"""
csv数据, 默认是一行是一条数据
    数据中每个字段与字段之间用逗号分隔
"""
import csv  # 内置

data = [[1, 2, 3, 4],
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [5, 6, 7, 8]]

with open('data.csv', mode='a', encoding='utf-8', newline='') as f:
    # newline=''  指定数据新行是一个空字符串, 不然会有数据空行
    # 实例化一个csv文件的对象, 括号内部传打开的文件对象
    # writerow(i)  给一个列表, 会把列表中的数据按照行的方式写入csv文件中
    csv_write = csv.writer(f)
    for i in data:
        csv_write.writerow(i)

# 是针对列表数据写入