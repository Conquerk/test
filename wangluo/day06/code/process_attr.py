from multiprocessing import Process
from time import sleep,ctime
def tm():
    for i in range(4):
        sleep(2)
        print(ctime())
p=Process(target=tm,name="英雄联盟")
p.daemon=False  #要在子进程开始之前设置
p.start()
print("process name:",p.name)
print("process　PID:",p.pid)
print("process is_alive:",p.is_alive())
#p.join()