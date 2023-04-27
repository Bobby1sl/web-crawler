import threading
import time
import random


def add1(n):
    for i in range(100):
        time.sleep(random.randint(1,3))  # 模拟阻塞
        with open('hello.txt', mode='a', encoding='utf-8') as f:
            f.write(f'{n} hello world !' + 'hello world !' * 1024)
            f.write('\n')


if __name__ == '__main__':
    for n in range(10):
        t1 = threading.Thread(target=add1, args=(n, ))
        t1.start()

"""
    多任务中会有敏感资源:  会产生资源竞争导致数据错误
        对单个文件多任务操作
        对一个全局变量多任务操作
        
    
    解决方案: 加锁
"""