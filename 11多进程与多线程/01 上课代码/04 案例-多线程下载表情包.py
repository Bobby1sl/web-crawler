import re
import threading
import time
import requests


# start_time = time.time()  # 记录程序执行的开始时间
#
# def data():
#     for page in range(1, 6):
#         url = f'https://www.biaoqingbao.net/gaoxiao/page_{page}.html'
#         response = requests.get(url)
#         html_data = response.text
#         # print(html_data)
#
#         # <img class="waitpic" src=".*?" data-original="(.*?)" alt=".*?" >
#         result = re.findall('<img class="waitpic" src=".*?" data-original="(.*?)" alt=".*?" >', html_data, re.S)
#         # print(result)
#
#         for img_url in result:
#             img_data = requests.get(img_url).content
#             # 文件名
#             file_name = img_url.split('/')[-1]
#
#             with open('img\\' + file_name, mode='wb') as f:
#                 f.write(img_data)
#                 print('保存完成:', file_name)
#
# print('程序花费时间:', time.time() - start_time)

# 1. 找数据地址
# 2. 请求数据
# 3. 解析数据
# 4. 保存数据

def send_request(url):
    """发送请求的函数"""
    response = requests.get(url)
    return response  # 返回的响应体


def parse_data(data):
    """解析数据的方法, 传入数据进行解析"""
    result = re.findall('<img class="waitpic" src=".*?" data-original="(.*?)" alt=".*?" >',
                        data,
                        re.S)

    return result  # 解析出来所有图片地址


def save_data(file_name, img_data):
    """
    保存数据的函数
    :param file_name: 文件名
    :param img_data: 图片数据
    """
    with open('img\\' + file_name, mode='wb') as f:
        f.write(img_data)
        print('保存完成:', file_name)


def main(url):
    """主函数: 调度其他三个函数的执行"""
    # 1. 调用发送请求的函数
    html_data = send_request(url).text
    # 2. 调用解析数据的函数
    imgUrl_list = parse_data(html_data)  # 一页会解析到很多图片地址--> 返回列表

    for imgUrl in imgUrl_list:  # 遍历图片地址列表
        file_name = imgUrl.split('/')[-1]  # 图片文件名
        img_data = send_request(imgUrl).content  # 图片数据

        # 3. 调用保存数据的方法
        save_data(file_name, img_data)

    print('程序花费时间:', time.time() - start_time)


# 主函数写完以后, 一定要测试运行是否有错误
# main('https://www.biaoqingbao.net/gaoxiao/page_4.html')

if __name__ == '__main__':
    start_time = time.time()  # 记录程序执行的开始时间

    for page in range(1, 6):
        url = f'https://www.biaoqingbao.net/gaoxiao/page_{page}.html'

        threading.Thread(target=main, args=(url,)).start()
