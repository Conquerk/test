from multiprocessing import Process,Array
import time 

#创建共享内存
shm = Array('i',[1,2,3,4,5])

def fun():
    for i in shm:
        print(i,end=" ")
    shm[2]=10000
    print("")
p = Process(target=fun)
p.start()
p.join()
for x in shm:
    print(x,end=" ")
print("")