from socket import *
from select import *
#创建套接子
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",4444))
s.listen(5)
#c创建一个ｐｏｌｌ对象
p=poll()
#建立查找字典
fdmap={s.fileno():s}
#注册关注的ｉｏ
p.register(s,POLLIN|POLLERR)

while True:
    #监控io
    print("正在监控")
    events=p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr=fdmap[fd].accept()
            print("connect from ",addr)
            #新关注
            p.register(c,POLLIN|POLLHUP)
            fdmap[c.fileno()]=c
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print("receive:",data.decode())
                fdmap[fd].send("收到消息".encode())