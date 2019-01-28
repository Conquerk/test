def read_from_file():
    l=[]
    try:
        f=open("si.txt","r")
        for line in f :
            line=line.split()  # 去掉\n
            items=line.split(",")
            n,a,s=items
            a=int(a)
            s=int(s)
            l.append(dict(name=n,age=a,score=s))
        f.close()
    except OSError:
        print("打开失败")
    return l
def save_from_file():
    try:
        f=open("si.txt","w")
        for d in l:
            f.write(d["name"])
            f.write(",")
            f.write(str(d["age"]))
            f.write(",")
            f.write(str(d["score"]))
            f.write("\n")
        print("保存成功")
        f.close()
    except OSError:
        print("保存失败")
        
