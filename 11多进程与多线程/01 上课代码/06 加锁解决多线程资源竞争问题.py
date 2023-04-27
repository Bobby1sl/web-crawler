import threading
import time
import random


# 创建一把锁
lock = threading.Lock()

def add1(n):

    for i in range(100):
        time.sleep(random.randint(1,3))  # 模拟阻塞

        lock.acquire()  # 加锁
        with open('hello.txt', mode='a', encoding='utf-8') as f:
            f.write(f'{n} hello world !' + 'hello world !' * 1024)
            f.write('\n')
        lock.release()  # 解锁  上完锁任务执行完以后一定要记得解锁, 不然会出现死锁引发报错


if __name__ == '__main__':
    for n in range(10):
        t1 = threading.Thread(target=add1, args=(n, ))
        t1.start()

