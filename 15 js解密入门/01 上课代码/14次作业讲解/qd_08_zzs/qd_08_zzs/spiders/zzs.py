import scrapy

from ..items import Qd08ZzsItem


class ZzsSpider(scrapy.Spider):
    name = "zzs"
    allowed_domains = ["zhangzs.com"]

    # start_urls = ["http://zhangzs.com/"]

    def start_requests(self):
        for page in range(1, 11):
            yield scrapy.FormRequest(
                url='https://www.zhangzs.com/wp-admin/admin-ajax.php',
                formdata={'action': 'wpcom_load_posts',
                          'page': str(page),
                          'type': 'default'},
                callback=self.parse,
                # meta=
            )

    def parse(self, response):
        # print(response.text)
        # with open()
        divs = response.css('.item')
        for div in divs:
            title = div.css('h2>a::text').getall()
            if len(title) == 1:
                title = title[0].strip()
            else:
                title = title[1].strip()

            info = div.css('.item-excerpt>p::text').get()  # 简介
            if not info:  # 如果没有简介
                info = 'null'

            time = div.css('.item-meta-li.date::text').get()  # 距今发布时间
            likes = div.css('.item-meta-li.hearts::text').get()  # 喜欢数
            stars = div.css('.item-meta-li.likes::text').get()  # 点赞数

            yield Qd08ZzsItem(title=title, info=info, time=time, likes=likes, stars=stars)