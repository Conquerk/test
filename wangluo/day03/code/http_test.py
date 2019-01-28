from socket import *

#创建套接子
s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(5)

while True:
    c,addr=s.accept()
    print("connect from ",addr)
    data=c.recv(4096)
    print("###############")
    print(data)
    print("###############")
    #HTTP响应个格式
    data='''HTTP/1.1 200 ok
    Content-Encoding: gzip
    Content-Type: text/html

    <h1>welcome to tedu python</h1>
    <p>这是一个测试</p>'''

    c.send(data.encode()) #发送给浏览器
c.close()
s.close()