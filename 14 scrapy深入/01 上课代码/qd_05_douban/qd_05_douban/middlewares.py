# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import requests
from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

"""
middlewares.py 是中间件文件
    两个中间件都能获取到请求体和响应体, 但是使用功能不同
        SpiderMiddleware: 爬虫中间件
            作用: 处理错误请求, 针对状态码做处理, 常见错误请求状态码会被自动过滤
            
        DownloaderMiddleware: 下载中间件
            作用: 处理请求的 cookies  headers  proxies
        
    
"""


class Qd05DoubanSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class Qd05DoubanDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class HeadersDownloaderMiddleware:
    """headers中间件"""

    def process_request(self, request, spider):
        # request.headers 拿到请求体中的请求头, 是一个字典对象
        request.headers.update(
            {
                'Host': 'movie.douban.com',
                'Referer': 'https://www.baidu.com/link?url=-S_3y2LVYYSAeYVNHMmlz_7Ha1MAQLImDvM3_zQrfJtE1KyHRvV51dk_GSiwi2K0&wd=&eqid=a02527b30001159b00000006645a472e',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            }
        )


class CookiesDownloaderMiddleware:
    """Cookies中间件"""

    def process_request(self, request, spider):
        # request.cookies 拿到请求体中cookie, 是一个字典对象
        # 如果整体复制cookies键值对不行, 那么需要构建每一个cookie片段的键值对
        request.cookies.update({'Cookie': 'll="118267"; bid=VrC8tT1GWz8; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1683638062%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D-S_3y2LVYYSAeYVNHMmlz_7Ha1MAQLImDvM3_zQrfJtE1KyHRvV51dk_GSiwi2K0%26wd%3D%26eqid%3Da02527b30001159b00000006645a472e%22%5D; ap_v=0,6.0; __utma=30149280.1169382564.1682168622.1682425549.1683638062.4; __utmb=30149280.0.10.1683638062; __utmc=30149280; __utmz=30149280.1683638062.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1640817040.1683638062.1683638062.1683638062.1; __utmb=223695111.0.10.1683638062; __utmc=223695111; __utmz=223695111.1683638062.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __gads=ID=744f53c3cb2ebb52-22841ef3a4e00021:T=1683638065:RT=1683638065:S=ALNI_MZhRKuML1OBDnNRafe3qd6-ndhaiQ; __gpi=UID=00000c03bafcda5c:T=1683638065:RT=1683638065:S=ALNI_MbkLLsUm467wiS6ZZ6Mn2ohKIWBZw; _pk_id.100001.4cf6=b39d476add4f5658.1683638062..1683638284.undefined.; _pk_ses.100001.4cf6=*; __yadk_uid=iHqVKZD4ZHIVREbOrlu9k4uWFSsAdZtO'})


class ProxyDownloaderMiddleware:
    """代理中间件"""
    def __init__(self):
        url = 'http://zltiqu.pyhttp.taolop.com/getip?count=1&neek=13873&type=2&yys=0&port=2&sb=&mr=2&sep=0'
        response = requests.get(url=url)
        json_data = response.json()
        ip = json_data['data'][0]['ip']
        port = str(json_data['data'][0]['port'])
        print(port)
        proxies = "https://" + ip + ':' + port
        print('构建好的代理:', proxies)
        self.proxy = proxies

    def process_request(self, request, spider):
        request.meta['proxy'] = self.proxy



