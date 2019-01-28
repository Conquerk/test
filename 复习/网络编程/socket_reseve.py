import socket as sk
import sys

sockfd = sk.socket()
Addr=("0.0.0.0",4444)
sockfd.bind(Addr)
sockfd.listen(5)
while True:
    try:
        conn,addr = sockfd.accept()
    except KeyboardInterrupt:
        sockfd.close()
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue 
    print(
        "{}以连接".format(addr)
    )
    while True:

        data = conn.recv(1024).decode()
        if not data:
            break
        print("接收到{}".format(data))
        conn.send(b"receive your massige")
sockfd.close()