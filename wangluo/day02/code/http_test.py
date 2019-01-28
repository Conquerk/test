from socket import *

#创建套接子
s=socket(AF_INET,SOCK_STREAM)
s.bind(("0.0.0.0",8000))
s.listen(5)

while True:
    c,addr=s.accept()
    print("connect from ",addr)
    data=c.recv(4096)
    print("###############")
    print(data)
    print("###############")
    c.close()
s.close()