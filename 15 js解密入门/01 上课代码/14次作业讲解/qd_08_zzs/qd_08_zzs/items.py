# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Qd08ZzsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()  # 标题
    info = scrapy.Field()  # 简介
    time = scrapy.Field()  # 发布时间
    likes = scrapy.Field()  # 喜欢数
    stars = scrapy.Field()  # 点赞数
