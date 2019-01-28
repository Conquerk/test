from multiprocessing import Process,Pipe
import time
#创建管道对象
fd1,fd2=Pipe(True)

def fun(name):
    time.sleep(3)
    fd2.send(name)
jobs=[]
for x in range(5):
    p=Process(target=fun,args=(x,))
    jobs.append(p)
    p.start()
for x in range(5):
    data=fd1.recv()
    print(data)
for x in jobs:
    x.join()