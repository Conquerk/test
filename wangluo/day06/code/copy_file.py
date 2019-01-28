# 创建父子进程同时复制一个文件，
# 各复制文件的一半到新的文件中
import os

filename="./test.jpg"
size=os.path.getsize(filename)
# 父子进程共用一个文件对象便宜量会相互影响
# f=open(filename,'rb')
#子进程复制上半部分
def copy1():
    f=open(filename,'rb')
    n = size // 2
    fw = open("1.jpg","wb")
    while True:
        if n < 1024:
            data = f.read(n)
            fw.write(data)
            break
        data=f.read(1024)
        fw.write(data)
        n -= 1024
    f.close()
    fw.close()
#父进程复制下半部分
def copy2():
    f=open(filename,"rb")
    fw=open("2.jpg",'wb')
    f.seek(size//2,0)

    while True:
        data=f.read(1024)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()
pid=os.fork()
if pid < 0:
    print("create process failed")
elif pid == 0:
    copy1()
else:
    copy2()
