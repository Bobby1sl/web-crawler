import os
import re

import requests


def get_one_chapter(url, times=3):  # times 可以控制异常次数
    """抓取一张小说数据的逻辑"""
    try:
        response_data = requests.get(url, timeout=0.3)

        result_2 = re.findall('<div id="chaptercontent" class=".*?">(.*?)<p class="readinline">.*?</p></div>',
                              response_data.text,
                              re.S)

        contend = result_2[0].replace('\u3000\u3000', '').replace('<br /><br />', '\n')
        # 提取标题
        title = re.findall('<h1 class="wap_none">(.*?)</h1>', response_data.text, re.S)[0]

        # 保存数据
        with open('小说\\' + title + '.txt', mode='w', encoding='utf-8') as f:
            f.write(contend)
            print('保存完成:', title)

    except Exception as e:
        print(e)
        if times >= 1:
            # 异常重试, 利用函数递归的方式
            get_one_chapter(url, times=times-1)  # 控制次数
            print('*' * 50)


if __name__ == '__main__':

    url = 'https://www.bqg70.com/book/1031/'
    response = requests.get(url)
    html_data = response.text
    result = re.findall('<dd><a href ="(.*?)">.*?</a></dd>', html_data, re.S)

    if not os.path.exists('小说'):
        os.mkdir('小说')

    for res in result:
        all_url = 'https://www.bqg70.com' + res
        get_one_chapter(all_url)

