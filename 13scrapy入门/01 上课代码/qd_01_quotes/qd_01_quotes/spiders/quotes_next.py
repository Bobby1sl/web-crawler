import scrapy

from ..items import Qd01QuotesItem


class QuotesNextSpider(scrapy.Spider):
    name = "quotes_next"
    allowed_domains = []
    # start_urls = ["http://quotes.toscrape.com/"]

    # 重写 start_urls
    def start_requests(self):
        # 构建地址
        yield scrapy.Request(url='http://quotes.toscrape.com/', callback=self.parse)

    def parse(self, response):
        divs = response.css('.quote')

        for div in divs:
            text = div.css('.text::text').get()
            author = div.css('.author::text').get()
            tags = div.css('.tags>a::text').getall()
            yield Qd01QuotesItem(text=text, author=author, tags=tags)

        # 处理翻页
        next_page = response.css('.next>a::attr(href)').get()  # 下一页部分地址
        if next_page:
            all_url = 'https://quotes.toscrape.com' + next_page  # 完整地址
            # scrapy.Request  构建一个requests请求, 让下载中间件进行下载, 也会返回response响应体
            # callback 参数就是指定当前的请求要交给那个函数做处理, 回调函数
            yield scrapy.Request(url=all_url, callback=self.parse)