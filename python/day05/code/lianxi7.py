s=0
for x in range(1,101):
    if (x%2==0)or(x%3==0)or(x%5==0)or(x%7==0):
        continue
    print(x,end=" ")  
    s+=x
print(s)
