import socket

s = socket.socket()
s.connect(("0.0.0.0",4444))
while True:
    data = input(">>")
    if not data:
        break
    s.send(data.encode())
    msg = s.recv(1024)
    print(msg.decode())