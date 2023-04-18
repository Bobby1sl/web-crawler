import csv  # 内置

list_dict = [{'first_name': 'Baked', 'last_name': 'Beans'},
             {'first_name': 'Lovely'},
             {'first_name': 'Wonderful', 'last_name': 'Spam'}]

with open('data.csv', mode='a', encoding='utf-8', newline='') as f:
    # 创建一个字典数据写入对象, 第一个参数是文件对象, 第二个参数是字典中的键
    # fieldnames 指定字典的键, 不能多不能少不能错
    csv_write = csv.DictWriter(f, fieldnames=['first_name', 'last_name'])
    # 字典数据会有专门写表头的方法
    csv_write.writeheader()

    for i in list_dict:
        csv_write.writerow(i)

