l=[]
def guanli():
    while True:
        print("+"+"-"*30+"+")
        print("|"+str("1.添加学生信息").center(24)+"|")
        print("|"+str("2.显示学生信息").center(24)+"|")
        print("|"+str("3.删除学生信息").center(24)+"|")
        print("|"+str("4.修改学生成绩").center(24)+"|")
        print("|"+str("5.按照成绩高低显示信息").center(20)+"|")
        print("|"+str("6.按照成绩低高显示信息").center(20)+"|")
        print("|"+str("7.按照年龄高低显示信息").center(20)+"|")
        print("|"+str("8.按照年龄低高显示信息").center(20)+"|")
        print("|"+str("9.从文件中读取数据(si.txt)").center(22)+"|")
        print("|"+str("10.保存信息到文件(si.txt)").center(23)+"|")
        print("|"+str("q.退出").center(28)+"|")
        print("+"+"-"*30+"+")
        x=input("输入菜单功能:")
        if x=="1":
            myinput()
        elif x=="2":
            mybiaoge()
        elif x=="3":
            delete()
        elif x=="4":
            change()
        elif x=="q":
            break

def myinput():
    global l
    while True:
        n=input("请输入姓名：")
        if  not n :
            break
        while True:
            try:
                s=int(input("请输入年龄："))
            except:
                print("请重新输入")
                continue
            else:
                break
        try:
            a=int(input("请输入成绩："))
        except ValueError:
            print("重新输入成绩")
            a=int(input("请输入成绩："))
        d={}
        d["name"]=n
        d["age"]=s
        d["score"]=a
        l.append(d)
def mybiaoge():
    global l
    print("+-------------+------------+------------+")
    print("|     name    |     age    |    score   |")
    print("+-------------+------------+------------+")
    for x in l :
        line="|"+x["name"].center(11)
        line+="|"+str(x["age"]).center(12)
        line+="|"+str(x["score"]).center(12)+"|"
        print(line)
    print("+-------------+------------+------------+")
def delete():
    global l
    i=0
    y=input("请输入删除的学生信息")
    for x in l:
        i+=1
        if y in x["name"]:
            del l[(i-1)]
def change():
    global l
    y=input("请输入修改学生学生成绩的名字：")
    z=int(input("请输入修改的成绩："))
    for x in l :
        if y in x["name"]:
            x["score"]=z
        else:
            pass
guanli()
    

    
    


