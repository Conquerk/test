#此示例　示意用ｓｅｅｋ来改变文件的读写位置
f=open("tell.txt","rb")
b=f.read(3)
print("你读取的是:",b)
print("当前读写的位置是:",f.tell())
#以下读取　5到10个字节的ｂ'abcde'
f.seek(5,0)
print("当前读写的位置是:",f.tell())
b1=f.read(5)
print("读写的是",b1)