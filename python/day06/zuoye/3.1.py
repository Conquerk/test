l=[]#准备放入算出来的非波那契数列
a=0
b=1
while len (l)< 40:
    # 当列表长度不够40　就算出一个数
    #每次循环一个数　放入列表
    l.append(b) #已有的数
    c=a+b # 求出下一个斐波那契数
    a=b
    b=c
print(l)