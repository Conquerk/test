from multiprocessing import Process,Array
import time 

#开辟五个整形空间
#shm = Array('i',5)
#存入字符串
shm=Array("c",b'Hello')


def fun():
    for i in shm:
        print(i,end=" ")
    shm[0]=b'h'
    print("")
p = Process(target=fun)
p.start()
p.join()
for x in shm:
    print(x,end=" ")
print("")
print(shm.value)