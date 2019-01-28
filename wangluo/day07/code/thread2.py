from threading import Thread
from time import sleep

#线程函数
def fun(sec,name):
    print("线程参数传递")
    sleep(sec)
    print("{}线程执行完毕".format(name))
#创建多个线程执行
thread=[]
for i in range(3):
    t=Thread(target=fun,args=(2,),
    kwargs={'name':"曙光%d"%i})
    thread.append(t)
    t.start()
for x in thread:
    x.join()