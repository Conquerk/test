import gevent
from gevent import monkey
monkey.patch_all()
from socket import * #执行脚本插件修改阻塞行为

#创建套接字
def server():
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(('0.0.0.0',4444))
    s.listen(3)
    while True:
        c,addr=s.accept()
        print("connect from ",addr)
        #handle((c) 循环方案
        gevent.spawn(handle,c)#协程方案

def handle(c):
    while True:
        data=c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send("receive you msg".encode())
    c.close()

server()
