a=1
b=2
c=3

def fn(c,d):
    e=300
    print("locals()返回：",locals())
    print("globas()返回：",globals())
    print(c)
    print(globals()["c"])
fn(100,200)
