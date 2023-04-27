import time


def sing():
    for i in range(3):
        print("正在唱歌...%d" % i)
        time.sleep(1)  # 模拟阻塞


def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        time.sleep(1)

start_time = time.time()  # 记录程序执行的开始时间
sing()
dance()
print('程序花费时间:', time.time() - start_time)


