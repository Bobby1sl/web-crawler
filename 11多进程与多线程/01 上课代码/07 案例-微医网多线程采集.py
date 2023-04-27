import csv
import threading
import time

import requests
import parsel

lock = threading.Lock()


def send_request(url):
    """发送请求的函数"""
    response = requests.get(url)
    return response.text  # 返回的响应体


def parse_data(data):
    """解析数据的方法, 传入数据进行解析"""
    selector = parsel.Selector(data)
    lis = selector.css('.g-doctor-item')

    data_list = []  # 定义一个空列表, 用于收集每一条数据
    for li in lis:
        name = li.css('.wrap>a::text').get()
        level = li.css('dl dt::text').getall()[1].strip()
        kind = li.css('dl dd p:nth-child(1)::text').get()
        Belonging = li.css('dl dd p:nth-child(2)>span::text').get()
        score = li.css('.star>em::text').get()
        good_for = li.css('.skill>p::text').get().strip().replace('\n', '').replace(' ', '')
        pic_see_price = li.css('.infos.image>span>em:nth-child(2)::text').get().strip()
        video_see_price = li.css('.infos.video>span>em:nth-child(2)::text').get().strip()
        print(name, level, kind, Belonging, score, good_for, pic_see_price, video_see_price)
        data_list.append([name, level, kind, Belonging, score, good_for, pic_see_price, video_see_price])

    return data_list  # 返回嵌套列表, 嵌套的是一条一条数据


def save_data(data_list):
    for data in data_list:
        with lock:
            with open('微医网.csv', mode='a', encoding='utf-8', newline='') as f:
                csv_write = csv.writer(f)
                csv_write.writerow(data)
        # lock.release()


def main(url):
    """主函数: 调度其他三个函数的执行"""
    # 1. 调用发送请求的函数
    html_data = send_request(url)
    # 2. 调用解析数据的函数
    data_list = parse_data(html_data)  # 嵌套列表
    # 3. 调用保存数据的方法
    save_data(data_list)
    print('程序花费时间:', time.time() - start_time)


# main('https://www.wedoctor.com/expert/61409/%E5%86%85%E7%A7%91')

if __name__ == '__main__':
    start_time = time.time()  # 记录程序执行的开始时间
    for page in range(1, 39):
        url = f'https://www.wedoctor.com/expert/61409/%E5%86%85%E7%A7%91/p{page}'

        threading.Thread(target=main, args=(url,)).start()