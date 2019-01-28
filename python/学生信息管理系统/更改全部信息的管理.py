l=[]
def guanli():
    while True:
        print("+"+"-"*20+"+")
        print("|"+str("1.添加学生信息").center(14)+"|")
        print("|"+str("2.显示学生信息").center(14)+"|")
        print("|"+str("3.删除学生信息").center(14)+"|")
        print("|"+str("4.修改学生成绩").center(14)+"|")
        print("|"+str("q.退出").center(18)+"|")
        print("+"+"-"*20+"+")
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
        s=int(input("请输入年龄："))
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
    for x in l:                 # a  aa   aaa   aaaa
        i+=1                    # 1   2    3      4
        if y in x["name"]:      # aa
            del l[(i-1)]        # 1
def change():
    global l
    y=input("请输入要修改学生信息的名字：")
    for x in l :
        if y in x["name"]:
            a=input("请输入要修改的信息")
            if a =="name":
                n=input("新的名字")
                x["name"]=n
            if a =="age":
                p=int(input("请输入新的年龄"))
                x["age"]=p
            if a=="score":
                t=int(input("请输入新的成绩："))
                x["score"]=t
guanli()