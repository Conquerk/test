l2=[]
temp=[]
l3=[]
temp2=[]
l=[1,1,1,1,2,2,2,3,3,4,4,5,5,5,6,6]
for x in l:
    if l.count(x)==2:
        temp2+=[x]
    elif l.count(x)>=2:
        temp+=[x]
for a in temp2:
    if a not in l2:
        l2+=[a]
print(l2)
for y in temp:
    if y not in l3:
        l3+=[y]
print(l3+l2)