from socket import * 
#创建套接字
sockfd=socket()

#发起链接
server_addr = ("127.0.0.1",4444)
sockfd.connect(server_addr)

#收发消息
while True:
    data=input(">>")
    if not data:
        break
    sockfd.send(data.encode())
    data=sockfd.recv(1024)
    print("from server:",data.decode())

sockfd.close()