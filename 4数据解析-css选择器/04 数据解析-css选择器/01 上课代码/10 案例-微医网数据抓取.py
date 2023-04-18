import requests
import parsel


# 1. 确认请求地址
url = 'https://www.wedoctor.com/expert/61409/%E5%86%85%E7%A7%91'

# 2. 发送请求
response = requests.get(url=url)
html_data = response.text
print(html_data)  # 发送请求以后一定要确认数据是请求到了的


# 3.数据解析
selector = parsel.Selector(html_data)

# 数据第一次提取
lis = selector.css('.g-doctor-item')
# print(len(lis))

for li in lis:
    name = li.css('.wrap>a::text').get()
    level = li.css('dl dt::text').getall()[1].strip()
    kind = li.css('dl dd p:nth-child(1)::text').get()
    Belonging = li.css('dl dd p:nth-child(2)>span::text').get()
    score = li.css('.star>em::text').get()
    good_for= li.css('.skill>p::text').get().strip().replace('\n', '').replace(' ', '')
    pic_see_price= li.css('.infos.image>span>em:nth-child(2)::text').get().strip()
    video_see_price= li.css('.infos.video>span>em:nth-child(2)::text').get().strip()
    print(video_see_price)
