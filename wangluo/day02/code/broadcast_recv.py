from socket import *

s=socket(AF_INET,SOCK_DGRAM)
#设置可以发送接收广播
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(("0.0.0.0",35555))

while True:
    try:
        msg,addr = s.recvfrom(1024)
        print("从{}获取广播：{}".format(addr,
        msg.decode()))
    except KeyboardInterrupt:
        print("退出接收")
        break
    except Exception as e:
        print(e)
s.close()

