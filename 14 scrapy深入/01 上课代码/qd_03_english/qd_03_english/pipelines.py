# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class Qd03EnglishPipeline:
#     # process_item 主要写入数据的方法, item 可以获取到流经管道的数据
#     def process_item(self, item, spider):
#         with open('data.csv', mode='a', encoding='utf-8') as f:
#             f.write(item['title'] + ',' + item['info'] + ',' + item['img_url'])
#             f.write('\n')
#         return item

"""创建一次"""
# 1. 创建工作簿对象
# 2. 创建表

"""操作多次"""
# 3. 表写入数据

"""操作一次"""
# 4. 保存工作簿


class CsvPipeline:
    def __init__(self):
        """初始化方法, 一般打开文件, 数据库对象"""
        self.f = open('english.csv', mode='a', encoding='utf-8', newline='')
        self.csv_write = csv.DictWriter(self.f, fieldnames=['title', 'info', 'img_url'])
        self.csv_write.writeheader()  # 写表头, 只需要写入一次

    # def open_spider(self, spider):
    #     ## spider (Spider 对象) – 被开启的spider
    #     ## 可选实现，当spider被开启时，这个方法被调用。
    #     pass

    def process_item(self, item, spider):
        """
        :param item: 爬虫文件返回的一条一条数据
        :param spider: 区分爬虫对象的参数
        :return: 返回一条一条数据, 必须原路返回, 可以便于下一个管道类使用
        """
        # d = dict(item)
        self.csv_write.writerow(item)  # 把item数据一条一条写入
        return item  # 原路返回

    def close_spider(self, spider):
        """整个项目停止前会调用的方法, 一般用于关闭文件, 关闭数据连接"""
        self.f.close()


# json数据结构---> [{}, {}, {}, .......]
class JsonPipeline:
    def open_spider(self, spider):
        self.f = open('english.json', mode='w', encoding='utf-8')
        self.d_list = []  # 用于收集每一条数据, 构建json结构

    def process_item(self, item, spider):
        d = dict(item)  # 针对json数据需要把item强制转化转化成原生的字典对象
        self.d_list.append(d)
        return item

    def close_spider(self, spider):
        print('数据:', self.d_list)
        # 执行json数据序列化操作
        json_str = json.dumps(self.d_list, ensure_ascii=False)
        self.f.write(json_str)
        self.f.close()

# 13个管道类
# 数据库