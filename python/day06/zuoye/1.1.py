l=[1,2,3,1,2,3,4,6,1,2,6]
l1=[]
l2=[]
for i in l:
    if i  not in l1:
        l1.append(i)
    elif i not in l2:
        if l.count(i)==2:
            l2.append(i)

print(l1)
print(l2)


