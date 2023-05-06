# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Qd02FulibaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 标题
    put_time = scrapy.Field()  # 发布时间
    reads = scrapy.Field()  # 阅读数
    stars = scrapy.Field()  # 点赞数
