#字典关键字传参
def mymin(a,b,c):
    print(a)
    print(b)
    print(c)
d1={"c":33,"b":22,"a":11}
mymin(d1["a"],d1["b"],d1["c"])
mymin(**d1)#等同于mymin(a=11,b=22,c=33)