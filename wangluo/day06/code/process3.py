from multiprocessing import Process
from time import sleep

#带参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("i am %s"%name)
        print("i am working........")
#p=Process(target=worker,args=(2,"大魔王"))
p=Process(target=worker,kwargs={"sec":2,"name":'李相赫'})
p.start()
p.join(4)
print("--------------------")