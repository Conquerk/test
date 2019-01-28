# f=open("infos.txt","w")
# while True:
#     x=input("请输入姓名：")
#     if not x :
#         break
#     y=int(input("请输入年龄："))
#     z=input("请输入地址：")
#     y=str(y)
#     f.writelines([x," ",y," ",z," ","\n"])
# f.close()
def get_infos():
    l=[]
    while True:
        n=input("请输入姓名：")
        if not n :
            break
        a=int(input("请输入年龄："))
        addr=input("请输入地址：")
        l.append(dict(name=n,age=a,address=addr))
    return l
def get_save(l):
    try:
        f=open("infos.txt","w")
        for d in l:
            f.write(d["name"])
            f.write(" ")
            f.write(str(d["age"]))
            f.write(" ")
            f.write(d["address"])
            f.write("\n")
            f.close()
    except OSError:
        print("打开文件失败")
l=get_infos()
print(l)
get_save(l)