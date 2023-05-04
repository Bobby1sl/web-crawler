"""
	目标网址：https://www.duitang.com/

	作业描述：请在网页最上面搜索框输入关键字 “蜡笔小新” 进行搜索图片，根据搜索到的结果采集前十页图片

	作业要求：用多进程嵌套多线程的方式实现
"""
import concurrent.futures
import time
import requests


def send_request(url):
    response = requests.get(url=url)
    return response

def parse_data(data):
    data_list = data['data']['object_list']

    img_url_list = []
    for data_ in data_list:
        img_url = data_['photo']['path']
        img_url_list.append(img_url)
    return img_url_list

def save_data(img_url):  # 传入一个图片地址
    img_data = send_request(img_url).content  # 请求一张图片数据
    file_name = img_url.split('/')[-1]
    with open('img\\' + file_name, mode='wb') as f:
        f.write(img_data)
        print('保存完成:', file_name)


def run(url):
    json_data = send_request(url).json()
    imgUrl_list = parse_data(json_data)

    """将一张图片的任务通过多线程分发"""
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for imgUrl in imgUrl_list:
            executor.submit(save_data, imgUrl)

# 测试主函数是否能运行
# run('https://www.duitang.com/napi/blogv2/list/by_search/?kw=%E8%9C%A1%E7%AC%94%E5%B0%8F%E6%96%B0&after_id=72&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&_=1683201134731')
if __name__ == '__main__':
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        for page in range(10):
            url = f'https://www.duitang.com/napi/blogv2/list/by_search/?kw=%E8%9C%A1%E7%AC%94%E5%B0%8F%E6%96%B0&after_id={page * 24}&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&_=1683201134731'
            executor.submit(run, url)

    print('总共花费时间:', time.time() - start_time)