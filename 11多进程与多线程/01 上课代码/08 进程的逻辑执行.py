import time
import multiprocessing  # 进程模块, 内置


def sing():
    for i in range(3):
        print("正在唱歌...%d" % i)
        time.sleep(1)  # 模拟阻塞


def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        time.sleep(1)

        # 多进程无法计算时间消耗
        # print('程序花费时间:', time.time() - start_time)


if __name__ == '__main__':
    # 把普通的函数对象转换成一个进程对象
    sing_process = multiprocessing.Process(target=sing)
    # 执行进程对象
    sing_process.start()

    sing_process = multiprocessing.Process(target=dance).start()


