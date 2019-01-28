l=[1,2,3,4,4,5,5,5,6,6,6,6,7,7,8]
l2=[]# 准备存放出现过得数字
for x in l: #遍历所有数
    if x not in l2:    #如果第一次出现则添加ｌ2中
        l2.append(x)
print(l2)
l3=[]
for x in l:
    #第一次出现并且出现了两次
    if x not in l3 and l.count(x)==2:
        l3.append(x)
print(l3)
