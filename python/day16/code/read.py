f=open("mynote.txt","rb")    #二进制读

b=f.read()
print("读取的内容长度为",len(b))
print("内容是：",b)
s=b.decode()   # 解码   编码 endecode
print("转为字符串后：",s)
f.close