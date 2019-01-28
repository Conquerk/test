from socket import *
from time import sleep

#目标地址
dest=("10.8.20.224",35555)
s=socket(AF_INET,SOCK_DGRAM)
#设置可以发送接收广播
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
while True:
    sleep(3)
    s.sendto("风里雨里".encode(),dest)
s.close()