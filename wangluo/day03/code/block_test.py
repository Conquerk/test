from socket import *
from time import sleep,ctime
#创建套接字
sockfd=socket()
#绑定本机的地址
sockfd.bind(("127.0.0.1",7777))
sockfd.listen(3)
#设置非阻塞状态
#sockfd.setblocking(False)
#设置超时时间
sockfd.settimeout(5)

while True:
    print("waiting for connect....")
    try:
        connfd,addr=sockfd.accept()
    #捕获非阻塞异常
    #except BlockingIOError:
    #   sleep(2)
    #捕获超时异常
    except timeout:
        print(ctime())
        continue
    else:
        print("connect from ",addr)
        data=connfd.recv(1024)
        print("receive:",data.decode())
        connfd.close()
sockfd.close()
