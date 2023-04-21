"""
目标站点:https://news.163.com/

往下翻有 要闻 这个新闻类目

    需求:
        爬取网易新闻 要闻 类目第一页数据，将数据保存为csv格式
        保存字段需要以下内容

            title  
            channelname  
            docurl  
            imgurl  
            source  
            tlink
"""
import csv
import json
import re
import requests


url = 'https://news.163.com/special/cm_yaowen20200213/?callback=data_callback'
response = requests.get(url=url)
json_data = response.text
print(json_data)

result = re.findall('data_callback\((.*?)\)', json_data, re.S)

# 反序列化
data = json.loads(result[0])

with open('wangyi_news.csv', mode='a', encoding='utf-8', newline='') as f:
    csv_write = csv.writer(f)
    csv_write.writerow(['标题', 'channelname', 'docurl', 'imgurl', 'source', 'tlink'])

    for res in data:
        title = res['title']
        channelname = res['channelname']
        docurl = res['docurl']
        imgurl = res['imgurl']
        source = res['source']
        tlink = res['tlink']
        print(title, channelname, docurl, imgurl, source, tlink, sep=' | ')

        csv_write.writerow([title, channelname, docurl, imgurl, source, tlink])

