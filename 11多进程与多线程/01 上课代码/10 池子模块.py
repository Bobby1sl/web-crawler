import concurrent.futures  # 池子模块功能, 内置
import time


def thread_function(name):
    print("子线程 %s: 启动" % name)
    time.sleep(2)  # 模拟阻塞
    print("子线程 %s: 完成" % name)


if __name__ == "__main__":

    # ThreadPoolExecutor 线程池
    # ProcessPoolExecutor 进程池
    # max_workers  最大任务数量
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(10):

            # submit 想6多任务池子中添加任务
            # 多个参数按照位置直接传递
            executor.submit(thread_function, i)
