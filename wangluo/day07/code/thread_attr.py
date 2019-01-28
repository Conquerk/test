from threading import Thread
from time import sleep
from threading import currentThread

def fun():
    sleep(3)
    print("线程属性测试")
    print("当前线程对象:%s"%currentThread().getName())
t=Thread(target=fun,name="光")
t.setDaemon(True)
#t.daemon=True
t.start()
#设置　获取　线程名
t.setName("暗")
print("thread name:",t.name)
print("thread get name:",t.getName())
#线程状态
print("is alive:",t.is_alive())
#t.join()
print("*****主线程结束*****")