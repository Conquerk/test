l=[[x,x+1,x+2] for x in range(1,8,3)]
print(l)

l=[[y for y in range(x,x+3)] for x in range(1,8,3)]
print(l)

#改为ｆｏｒ语句
l=[]
for x in range(1,8,3):
    l1=[]
    for y in range(x,x+3):
        l1.append(y)
    l.append(l1)
print(l)