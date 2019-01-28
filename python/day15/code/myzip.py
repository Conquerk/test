Numbers=[10086,10000,10010,95588]
Names=["中国移动","中国电信","中国联通"]

def myzip(iter1,iter2):
    #先拿到两个对象的迭代器
    it1=iter(iter1)
    it2=iter(iter2)
    while True:
        try:
            a=next(it1)
            b=next(it2)
            yield(a,b)
        except StopIteration:
            return
    #yield (next(iter1),next(iter2))
for t in zip(Numbers,Names):
    print(t)
d=dict(zip(Numbers,Names))
print(d)
for a in myzip(Numbers,Names):
    print(a)
z=dict(myzip(Numbers,Names))
print(z)