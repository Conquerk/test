def sushu(m,n):
    for x in range (m,n):
        if x<2:
            pass
        else:
            for y in range(2,x):
                if x % y ==0:
                    break
            else:
                yield x
l=list(sushu(10,20))
print(l)
print(sum(sushu(0,200)))
        
