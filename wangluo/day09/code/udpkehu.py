from socket import * 
import sys

if len(sys.argv) < 3:
    print('''
    argv is error 
    run as
    python3 udpkefu.py 127.0.0.1 12888
    ''')
    raise
#从命令行接受服务器地址
HOST=sys.argv[1]
PORT=int(sys.argv[2])
ADDR=(HOST,PORT)
# 创建套接字
sockfd=socket(AF_INET,SOCK_DGRAM)

while True:
    data=input("data>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr=sockfd.recvfrom(1024)
    print("收到服务器消息",msg.decode())

sockfd.close()

