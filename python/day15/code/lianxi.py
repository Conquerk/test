def even(n,m):
    for x in range(n,m):
        if x % 2 ==0:
            yield x 
it=list(even(10,20))
print(it)
for x in even(5,10):
    print(x)
l=[x for x in even(0,10)]
print(l)
