from select import select
from socket import *

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",4444))
s.listen(3)
#添加到关注列表
rlist=[s]
wlist=[]
xlist=[]

while True:
    #IO监控
    rs,ws,xs=select(rlist,wlist,xlist)
    for x in rs:
        #如果x is s 说明ｓ就绪有客户端连接
        if x is s:
            c,addr=x.accept()
            print("connect from ",addr)
            rlist.append(c)
        #某个客户端连接就绪
        else:
            data=x.recv(1024)
            if not data:
                rlist.remove(x)
                x.close()
                continue
            print("收到:",data.decode())
            #x.send("收到消息".encode())
            wlist.append(x)
    for w in ws:
        w.send("收到消息".encode())
        wlist.remove(x)
    for x1 in xs:
        x1.close()
        raise