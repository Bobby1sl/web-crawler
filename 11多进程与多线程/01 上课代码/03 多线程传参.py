import threading
import time


def get(url, headers=None):
    print(url)
    time.sleep(5)
    print(headers)


urls = ['https://www.baidu.com','https://www.360.com','https://www.sousou.com']
for i in urls:
    threading.Thread(
        target=get,
        args=(i,),
        kwargs={"headers": {'user-agent': 'python-requests'}}
    ).start()


"""
线程的参数传递
target  传入普通的函数对象, 只需要传递函数对象的名字,不要加括号
args    位置参数,一定传元组(如果只有一个参数, 这个参数后面需要加逗号) **坑**
kwargs  传递关键字参数
"""