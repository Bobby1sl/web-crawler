# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class DownLoadPIC(ImagesPipeline):
    def get_media_requests(self, item, info):
        img_url = item['img_url']  # 从item中取出图片地址
        # 构建图片地址的请求, 构建的请求会自动被 ImagesPipeline 处理
        yield scrapy.Request(url=img_url)

    def file_path(self, request, response=None, info=None, *, item=None):
        filename = '/' + request.url.split('/')[-1]
        return './images' + filename

