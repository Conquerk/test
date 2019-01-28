import math
def fun(n):
    s=1
    for x in range(1,n+1):
        y=math.factorial(x)
        s+=1/y
    return s
print(fun(20))