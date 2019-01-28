def myxrange(start,stop=None,step=1):
    if stop is None:
        stop = start
        start=0
    #正向生成
    if step>0:
        while start < stop:
            yield start
            start+=step
    elif step>0:
        while start > stop:
            yield start
            start += step
l=[x**2 for x in myxrange(1,101,2)]
print(sum(l))