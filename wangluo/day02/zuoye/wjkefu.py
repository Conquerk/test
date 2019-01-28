from socket import *

#创建套接字
s=socket()

#发起链接
host=("127.0.0.1",4444)
s.connect(host)
f=open('send.JPG','rb')
while True:
    data=f.read(1024)
    if not data:
        break
    s.send(data)

s.close()