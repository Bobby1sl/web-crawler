# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

"""
数据管道:
    在整个项目中提取出来的所有数据都会流经数据管道
    数据保存, 数据去重
"""
class Qd01QuotesPipeline:
    def process_item(self, item, spider):
        print('管道文件打印数据: ', item)

        d = dict(item)
        with open('quotes.csv', mode='a', encoding='utf-8') as f:
            f.write(d['text'] + ',' + d['author'] + ',' +  '-'.join(d['tags']))
            f.write('\n')

        return item
