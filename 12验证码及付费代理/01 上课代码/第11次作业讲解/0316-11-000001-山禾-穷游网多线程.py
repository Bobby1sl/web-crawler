"""
    目标网址: https://place.qyer.com/china/citylist-0-0-1/
    
    需求:
        1、用多线程采集170页所有数据保存为csv, 计算程序运行的时间
        2、采集以下信息
            city_name   # 城市名
            travel_people  # 去过的人数
            travel_hot    # 热门景点  比如香港有热门景点[ 香港海洋公园 、 星光大道 、 维多利亚港 、 太平山 、 尖沙咀 、 金紫荆广场 、 香港迪士尼乐园 、 中环 、 弥敦道 、 兰桂坊 、 中银大厦 、 香港杜莎夫人蜡像馆 、 中环至半山自动扶]
            img_url  # 城市图片url
            
请在下方编写代码：
"""
import csv
import time

import parsel
import requests
import threading
import concurrent.futures


lock = threading.Lock()


def send_request(url):
    response = requests.get(url=url)
    return response.text

def parse_data(data):
    selector = parsel.Selector(data)
    lis = selector.xpath('//ul[@class="plcCitylist"]/li')

    data_list = []  # 收集采集到的一页数据, 构建嵌套列表
    for li in lis:
        city_name = li.xpath('.//h3/a/text()').get().strip()
        travel_people = li.xpath('.//p[@class="beento"]/text()').re('\d+')[0]
        travel_hot = li.xpath('.//p[@class="pois"]/a/text()').getall()
        travel_hot = '-'.join([i.strip() for i in travel_hot])
        img_url = li.xpath('.//p[@class="pics"]//img/@src').get()
        print(city_name, travel_people, travel_hot, img_url)
        data_list.append([city_name, travel_people, travel_hot, img_url])

    return data_list

def save_data(data):
    for res in data:
        lock.acquire()
        with open('穷游网.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow(res)
        lock.release()

def run(url):
    html_data = send_request(url)
    parse_result = parse_data(html_data)
    save_data(parse_result)

# 执行主函数, 查看运行是否有误
# run('https://place.qyer.com/china/citylist-0-0-1/')
if __name__ == '__main__':
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        for page in range(1, 171):
            url = f'https://place.qyer.com/china/citylist-0-0-{page}/'
            executor.submit(run, url)

    print('总共花费时间:', time.time() - start_time)