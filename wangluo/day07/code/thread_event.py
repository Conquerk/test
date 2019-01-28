from threading import Thread,Event
from time import sleep

s=None  # 作为通信变量
e=Event()


def bar():
    print("bar 拜山头")
    sleep(2)
    global s
    s="曙光照耀我们前行"
    e.set()

b=Thread(target=bar)
b.start()

print("说对口令为我方英雄")
e.wait() # 阻塞等待分支线程设置e.set()
if s == "曙光照耀我们前行":
    print("确认为曙光女神")
else:
    print("敌方英雄")
e.clear()
b.join()