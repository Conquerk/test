import socket

#创建套接字
sockfd=socket.socket(socket.AF_INET,
                    socket.SOCK_STREAM)

#设置绑定地址
sockfd.bind(("0.0.0.0",9999))

#设置监听
sockfd.listen(5)
print("waiting for connect ....")

#等待处理客户端链接
while True:
    connfd,addr=sockfd.accept()
    print("connect from ",addr)  #客户端地址

    #收发消息
    while True:
        data=connfd.recv(1024)
        if not data:
            break
        print("receive message",data.decode())

        n=connfd.send("receive your msg".encode())
        print("send %d bytes"%n)
    connfd.close()
#关闭套接字
sockfd.close()