l=[1,1]
for i in range(40):
    l.append(l[i]+l[i+1])
    i+=1
#    if l[i]+l[i+1]>40:
    #    break
print(l)