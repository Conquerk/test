def myrange(a,b=None,c=None):
    if b is None:
        start=0
        stop=a
    else:
        start=a
        stop=b
    if c is None:
        step=1
    else:
        step=c
    return list(range(start,stop,step))
print(myrange(4,6))
print(myrange(4))
print(myrange(1,10,3))
