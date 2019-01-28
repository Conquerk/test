from socket import *
import struct
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",4444))
s.listen(5)

st=struct.Struct("i5sf")

c,addr=s.accept()
data=c.recv(1024)
data=st.unpack(data)
print(data)
c.close()
s.close()