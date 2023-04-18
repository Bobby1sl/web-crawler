"""
思路:
    在静态页面中解析每个音频的id值
    根据每个id发送音频地址的请求
    请求每个音频地址数据, 保存
"""
import parsel
import requests


# 1.找数据地址
url = 'https://www.ximalaya.com/youshengshu/2684034/'
headers = {
    'authority': 'www.ximalaya.com',
    'cookie': '_xmLog=h5&4770c3c5-f5cc-49e5-8eeb-fac7cc1a2a85&process.env.sdkVersion; xm-page-viewid=ximalaya-web; impl=www.ximalaya.com.login; x_xmly_traffic=utm_source%253A%2526utm_medium%253A%2526utm_campaign%253A%2526utm_content%253A%2526utm_term%253A%2526utm_from%253A; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1681565485; Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1681565485',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

# 2. 发送请求
response = requests.get(url=url, headers=headers)
html_data = response.text
# print(html_data)

# 3. 数据解析
selector = parsel.Selector(html_data)
lis = selector.xpath('//li[@class="Mi_"]')
# print(len(lis))

for li in lis:
    title = li.xpath('.//span[@class="title Mi_"]/text()').get()
    href = li.xpath('.//div[@class="text Mi_"]/a/@href').re('\d+')[0]

    # m4a_id = href.split('/')[-1]  # 提取音频的id值
    # # print(title, m4a_id)

    m4a_url = f'https://www.ximalaya.com/revision/play/v1/audio?id={href}&ptype=1'
    m4a_json = requests.get(url=m4a_url, headers=headers).json()
    m4a_url_get = m4a_json['data']['src']  # 解析音频地址
    # print(m4a_url_get)

    # 请求音频数据
    m4a_data = requests.get(url=m4a_url_get, headers=headers).content

    # 准备文件名
    file_name = title + '.m4a'
    # print(title, m4a_url_get)

    with open('video\\' + file_name, mode='wb') as f:
        f.write(m4a_data)
        print('保存完成:', file_name)



# css 和 xpath 可以互补
# 有的网站用css可以解析, 但是用xpath解析不了
# 有的网站用xpath可以解析, 但是用css解析不了

