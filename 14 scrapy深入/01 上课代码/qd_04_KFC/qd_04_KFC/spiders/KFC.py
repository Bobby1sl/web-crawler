import scrapy


class KfcSpider(scrapy.Spider):
    name = "KFC"
    allowed_domains = ["kfc.com.cn"]
    # start_urls = ["http://kfc.com.cn/"]

    def start_requests(self):
        # for page in range(1, 11):
        yield scrapy.FormRequest(
            url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword',
            formdata={
                'cname': '',
                'pid': '',
                'keyword': '北京',
                'pageIndex': '1',
                'pageSize': '10'
            },
            callback=self.parse,
            # 用于翻页
            meta={'page': 2}
        )

    def parse(self, response):
        # print(response.json())
        json_data = response.json()
        res_data = json_data['Table1']
        for res in res_data:
            storeName = res['storeName']
            addressDetail = res['addressDetail']
            cityName = res['cityName']
            pro = res['pro']
            print(storeName, addressDetail, cityName, pro, sep=' | ')

        page = response.meta.get('page')
        print('这是上一个函数传过来的meta参数:', page)

        if page <= 10:
            yield scrapy.FormRequest(
                url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword',
                formdata={
                    'cname': '',
                    'pid': '',
                    'keyword': '北京',
                    'pageIndex': str(page),
                    'pageSize': '10'
                },
                callback=self.parse,
                # 用于翻页
                meta={'page': page + 1}
            )

# meta作用: 用与函数与函数之间的数据传递
# meta需要构建字典, 键是自己设置, 后续要取值就要用这个键取值
# meta传递是一次性的传递, 不能跨函数传递