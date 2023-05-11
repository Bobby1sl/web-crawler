import scrapy


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ['taolop.com', 'douban.com']  # 添加代理以后, 可以把域名限制干掉, 不然会过滤
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        print(response.text)
        print(response.request.headers)
