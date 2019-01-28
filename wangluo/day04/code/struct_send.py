from socket import *
import struct

s=socket()
s.connect(("127.0.0.1",4444))

st=struct.Struct("i5sf")

data=st.pack(1,b"zhang",1.75)
s.send(data)
s.close()