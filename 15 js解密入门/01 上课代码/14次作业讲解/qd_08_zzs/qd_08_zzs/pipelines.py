# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CsvPipeline:
    def open_spider(self, spider):
        self.f = open('zzs.csv', mode='a', encoding='utf-8', newline='')
        self.csv_write = csv.DictWriter(self.f, fieldnames=['title', 'time', 'likes', 'stars', 'info'])
        self.csv_write.writeheader()

    def process_item(self, item, spider):
        self.csv_write.writerow(item)
        return item

    def close_spider(self, spider):
        self.f.close()
