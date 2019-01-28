import random
def daoru():
    while True:
        try:
            x=input("请用户导入文件:")
            f=open(x)
            y=f.read()
            z=y.split(",")
        except:
            print("导入错误，")
            continue
        else:
            return z
def dian(z):
    try:
        l=[]
        while True:
            l1=[]
            a=random.choice(z)
            l+=[a]
            print("点到的学员姓名为：",a) 
            for x in z :
                if x not in l:
                    l1+=[x]
            z=l1
            f=open("x.csv","w")
            for x in l1:
                f.write(x)
                f.write(",")
            f1=open("x1.csv","w")
            for x in l:
                f1.write(x)
                f1.write(",")
            shuru=input("是否继续输入（1/0）：")
            if shuru == "0":
                print("结束")
                break
            if shuru == "1":
                continue
    except IndexError:
        print("人员以全部选完")
        f=open("x.csv","w")
        for x in l:
            x=[x,","]
            f.writelines(x)
        f.close()
dian(daoru())