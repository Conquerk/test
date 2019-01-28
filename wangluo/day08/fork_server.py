from socket import *
import sys,os

#客户端处理函数
def client_handler(c):
    print("客户端：",c.getpeername())
    while True:
        data=c.recv(1024)
        if not data:
            break
        print("收到：",data.decode())
        c.send("Receive you message".encode())
    c.close()
    sys.exit(0) #销毁子进程    

#创建套接子
HOST='0.0.0.0'
PORT=4444
ADDR=(HOST,PORT)

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)

#循环等待客户端连接
print("listen to 4444....")
while True:
    try:
        c,addr=s.accept()
    except KeyboardInterrupt:
        sys.exit('退出服务器')
    except Exception as e:
        print('Error',e)
        continue
    #创建新的进程处理客户端请求
    pid=os.fork()
    #子进程处理客户端请求
    if pid == 0:
        p=os.fork()
        if p==0:
            s.close()
            client_handler(c)  # 客户端处理参数
        else:
            sys.exit(0)
    #父进程或者创建进程失败都继续等待下一个客户端连接
    else:
        c.close()
        os.wait() # 等待一级子进程退出
        continue