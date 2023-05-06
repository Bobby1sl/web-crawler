import scrapy

"""
爬虫文件:
    1. 收集需要采集的网址
    2. 解析数据
"""
# scrapy.Spider 爬虫基类
class QuotesSpider(scrapy.Spider):
    # 爬虫文件的名字, 通过scrapy genspider 时创建, 后期启动爬虫项目的时候需要指定爬虫的名字
    name = "quotes"

    # 运行爬虫时, 采集哪个域名下的数据, 允许的范围是一个列表
    allowed_domains = []

    # 采集数据的起始网址, 通过 genspider 自动生成的, 一般是错误的, 需要修改
    # 对于有规律的url地址, 一般采用列表推导式取收集所有需要采集的地址
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        # start_urls  起始网址返回的数据, 默认会给 parse 函数进行处理
        # parse 函数必须携带 response
        # response 具有所有相应体的方法和属性 + 也具有 parsel 模块中所有数据解析的方法<css, xpath, re>
        # print(response.text)

        """采用数据二次提取的方式"""
        divs = response.css('.quote')

        for div in divs:
            text = div.css('.text::text').get()
            author = div.css('.author::text').get()
            tags = div.css('.tags>a::text').getall()
            # print(text, author, tags)

            # 如果获取的数据, 通过yield返回的是一个字典, 那么scrapy框架会自动处理
            # scrapy框架里面所有爬虫文件返回的数据  全部用 yield 返回
            # yield 一条一条返回数据内容
            yield {'text': text, 'author':  author, 'tags':  tags}


"""
如何处理反扒?
如何保存数据?
如何知道框架底层调度流程?
"""