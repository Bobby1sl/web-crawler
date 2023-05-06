import scrapy

from ..items import Qd02FulibaItem


class FulibaSpider(scrapy.Spider):
    name = "fuliba"
    allowed_domains = ["fuliba2023.net"]
    start_urls = [f"https://fuliba2023.net/page/{page}" for page in range(1, 11)]

    def parse(self, response):
        # print(response.text)

        articles = response.css('.content article')
        for art in articles:
            title = art.css('h2>a::text').get()  # 标题
            put_time = art.css('.meta>time::text').get()  # 发布时间
            reads = art.css('.pv::text').get()  # 阅读数
            stars = art.css('.post-like>span::text').get()  # 点赞数
            yield Qd02FulibaItem(title=title, put_time=put_time, reads=reads, stars=stars)
