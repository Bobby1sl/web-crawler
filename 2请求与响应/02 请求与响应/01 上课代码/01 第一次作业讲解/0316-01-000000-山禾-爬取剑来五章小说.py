"""
按照以下网址爬取小说。爬取《剑来》前面五章的小说数据,分别保存在不同的txt文件下

	-- 网址： https://www.bige7.com/book/1031/

请下下方开始编写代码
"""
import os
import re

import requests

url = 'https://www.bqg70.com/book/1031/'
response = requests.get(url)
html_data = response.text
# print(html_data)

# <dd><a href ="(.*?)">.*?</a></dd>
result = re.findall('<dd><a href ="(.*?)">.*?</a></dd>', html_data, re.S)
# print(result)
# print(len(result))

if not os.path.exists('小说'):
    os.mkdir('小说')

for res in result[:5]:
    # 拼接完整地址
    all_url = 'https://www.bqg70.com' + res
    # print(all_url)

    """抓取一张小说数据的逻辑"""
    response_data = requests.get(all_url)

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

