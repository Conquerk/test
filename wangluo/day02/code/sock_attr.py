from socket import *

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
print("套接字选项值",s.getsockopt(SOL_SOCKET,SO_REUSEADDR))
#套接字的地址族
print(s.family)

#套接字的类型
print(s.type)

#获取套接字绑定地址
s.bind(("0.0.0.0",8888))
print(s.getsockname())

#获取套接字对应的文件描述符
print(s.fileno())
s.listen(5)

c,addr=s.accept()
#客户端连接套接字获取对应客户端地址
print(c.getpeername())