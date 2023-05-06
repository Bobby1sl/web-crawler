# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FulibaPipeline:
    def process_item(self, item, spider):
        d = dict(item)
        with open('fuliba.csv', mode='a', encoding='utf-8') as f:
            f.write(d['title'] + ',' + d['put_time'] + ',' + d['reads'] + ',' + d['stars'])
            f.write('\n')
        return item
