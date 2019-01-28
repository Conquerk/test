from socket import *
#创建套接子
sockfd=socket(AF_INET,SOCK_DGRAM)

#绑定地址
addr1=("0.0.0.0",12888)
sockfd.bind(addr1)

#消息收发
while True:
    data,addr = sockfd.recvfrom(1024)
    print("发送方的地址是%s","接收到的消息为%s"
    %(addr,data.decode()))
    sockfd.sendto(b"thanks from your msg",addr)
#关闭套接字
sockfd.close()

