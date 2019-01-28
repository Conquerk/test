from socket import * 
from multiprocessing import Process  
import sys

HOST = '0.0.0.0'
PORT = 4444
ADDR = (HOST,PORT)

#客户端处理函数
def handler(c):
    print("Connect from",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break 
        print(data.decode())
        c.send(b'Receive')
    c.close()
    sys.exit(0)

#创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)

#接收客户端请求
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue 
    
    #创建进程
    t = Process(target = handler,args = (c,))
    t.setDaemon(True)
    t.start()
