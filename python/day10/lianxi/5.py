    #      1
    #     1 1 
    #    1 2 1 
    #   1 3 3 1 
    #  1 4 6 4 1 
    # 1 5 10 10 5 1 
def newlist(l):
    #用给定的Ｌ　返回下一行
    rl=[1]  #左边的1
    #中间的数字(循环获取从0开始的索引)
    for i in range(len(l)-1):
        v=l[i]+l[i+1]
        rl.append(v) 
    rl.append(1)   #最后的1
    return rl

def yhlist(n):  #n为行数
    rl=[]
    l=[1]
    while len(rl)<n:
        rl.append(l)  #加入当前行
        l=newlist(l)
    return rl
def getlist(l):
    rl=[]
    for line in l:
        strlist=[str(x) for x in line]
        s=" ".join(strlist)
        rl.append(s)
    return rl
#打印杨辉三角
def sanjiao(l):
    maxlen=len(l[-1])
    for s in l:
        print(s.center(maxlen))

l=yhlist(6)
sl=getlist(l)
sanjiao(sl)

