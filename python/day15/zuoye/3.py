def myfilter(fn,iter1):
    for x in iter1:
        if fn(x)==True:
            yield x

