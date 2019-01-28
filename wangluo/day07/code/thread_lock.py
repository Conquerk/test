from threading import Thread,Lock
from time import sleep
a=b=0
lock=Lock()
def value():
    while True:
        lock.acquire()
        if  a != b:
            print("a={},b={}".format(a,b))
        lock.release()
t=Thread(target=value)
t.start()
while True:
    with lock:
        a+=1
        b+=1
t.join()