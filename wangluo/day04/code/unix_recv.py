from socket import *

#确定套接字文件
sock_five="./sock"

#创建本地套接字
s=socket(AF_UNIX,SOCK_STREAM)

#绑定套接字文件
s.bind(sock_five)

#监听
s.listen(5)

#消息的收发

while True:
    c,addr=s.accept()
    while True:
        data=c.recv(1024)
        if not data:
            break
        print(data.decode())
    c.close()
s.close()