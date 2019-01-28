# 示意ｔｅｌｌ的用法
f=open("tell.txt","rb")
f.read(3)
print("当前的读写位置是：",f.tell())
f.read(7)
print("当前的读写位置是：",f.tell())

f.close()