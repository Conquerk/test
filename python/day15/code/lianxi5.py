ba=bytearray(b'a1b2c3d4')
b1=ba[::2]
b1=bytes(b1)
b2=ba[1::2]
b2=bytes(b2)
print(b1)
print(b2)
ba[::2]=[65,66,67,68]
print(ba)
# l=[1,2,3,4,5,6]
# l[::2]=['10',"10",'10']
# print(l)
x=bytes("中文","utf-8")
print(x)