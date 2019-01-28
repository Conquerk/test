from select import select
from socket import *

s=socket()
s.bind(("0.0.0.0",4444))
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.listen(3)


#关注套接字ｉｏ
print("监控IO")
s,ws,xs=select([s],[],[],3)
print("处理IO")

