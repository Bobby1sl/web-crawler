"""
    使用 css 选择器将豆瓣250 十页的全部电影信息全部提取出来。
    目标网址：https://movie.douban.com/top250

    title（电影名）
    info（导演、主演、出版时间）
    score（评分）
    follow（评价人数）
	
	提取出来print（）打印即可
"""
import requests
import parsel


for page in range(0, 226, 25):

    # 1. 找数据地址
    url = f'https://movie.douban.com/top250?start={page}&filter='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }

    # 2. 发送数据请求
    response = requests.get(url, headers=headers)
    html_data = response.text
    # print(html_data)  # 在解析数据之前一定要打印数据查看有没有获取到

    # 3.数据解析
    # 3.1 转数据类型
    selector = parsel.Selector(html_data)

    # 3.2 数据提取
    """一次提取"""
    lis = selector.css('.grid_view>li')
    # print(lis)
    # print(len(lis))

    """二次提取"""
    for li in lis:
        title = li.css('.title::text').get()
        info = li.css('.bd>p:nth-child(1)::text').getall()
        info = ' | '.join([i.strip() for i in info])
        score = li.css('.rating_num::text').get()
        follow = li.css('.inq::text').get()
        commom = li.css('.star>span:nth-child(4)::text').get()
        print(commom)

    print('-----------------------------------------\n')