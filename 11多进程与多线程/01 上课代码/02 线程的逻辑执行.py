import time
import threading  # 线程模块, 内置


def sing():
    for i in range(3):
        print("正在唱歌...%d" % i)
        time.sleep(1)  # 模拟阻塞


def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        time.sleep(1)

        # # 如果要计算线程执行的时间, 只能写在线程对应的函数里面计算时间
        print('程序花费时间:', time.time() - start_time)



start_time = time.time()
# 所有的多任务转化对象都是基于函数对象做转化的
sing_thread = threading.Thread(target=sing)
print(sing_thread)
sing_thread.start()  # 执行线程任务


threading.Thread(target=dance).start()


