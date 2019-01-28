from multiprocessing import Pool
from time import sleep,ctime

def worker(msg):
    sleep(2)
    print(msg)
    return ctime()
#创建进程池
pool=Pool(processes=3)

l=[]
#向进程池添加事件
for i in range(10):
    msg="大魔王%s"%i
    #异步执行
    r=pool.apply_async(func=worker,args=(msg,))
    #存储函数事件对象
    l.append(r)
    #同步执行
    #pool.apply(............)
#关闭进程池
pool.close()
#回收进程池
pool.join()
for i in l:
    i.get()#可以获取进程函数事件的返回值
    print(i.get())
