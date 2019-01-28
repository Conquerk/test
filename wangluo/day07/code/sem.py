from multiprocessing import Semaphore,Process
from time import sleep
import os
#创建信号量
sem = Semaphore(3)
def fun():
    print("%d 想执行事件"%os.getpid())
    sem.acquire()
    print("%d 执行想执行事件"%os.getpid())
    sleep(3)
    print("%d 事件执行完毕"%os.getpid())
jobs=[]
#创建５个进程 消耗５个信号量　不够则阻塞
for i in range(5):
    p=Process(target=fun)
    jobs.append(p)
    p.start()
#又添加三个信号量　不再阻塞
for i  in range(3):
    sleep(5)
    sem.release()  # 增加一个信号量
#关闭进程
for i in jobs:
    i.join()
#查看信号量
print("信号量剩余 %d"%sem.get_value())