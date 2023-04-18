"""
	- 课上的搜狗图片案例，先自己实现一遍, 构建查询参数请求数据
	- 将前三页的图片数据保存到文件夹里面
	    有错误需要解决报错<可以根据情况使用（异常捕获 + 请求参数）>
		
请在下方编写代码
"""
import requests
requests.packages.urllib3.disable_warnings()  # 忽略警告


url = 'https://pic.sogou.com/napi/pc/searchList'


count = 1  # 定义一个变量, 用于命名图片的问题件名字
for page in range(0, 97, 48):
    params = {
        'mood': '7',
        'dm': '0',
        'mode': '1',
        'start': str(page),
        'xml_len': '48',
        'query': '风景'
    }
    response = requests.get(url=url, params=params)
    json_data = response.json()
    # print(json_data)

    data_list = json_data['data']['items']
    for data in data_list:
        img_url = data['picUrl']
        print(img_url)

        try:
            # 请求图片数据
            img_response = requests.get(url=img_url, verify=False, timeout=3).content
            # 准备文件名
            file_name = str(count) + '.jpg'

            count += 1

            with open('img\\' + file_name, mode='wb') as f:
                f.write(img_response)
                print('保存完成:', file_name)
        except Exception as e:
            print(e)
    print('------------------------------------------------------------------\n')
