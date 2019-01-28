from socket import *
#创建套接字
s=socket()
#绑定地址
s.bind(("0.0.0.0",4444))
#创建监听套接字
s.listen(5)
#等待链接
c,addr=s.accept()
print("等待连接...",addr)
#打开文件收发消息
f=open('recv.jpg','wb')
while True:
    data=c.recv(1024)
    if not data:
        break
    f.write(data)

f.close() 
c.close()
s.close()