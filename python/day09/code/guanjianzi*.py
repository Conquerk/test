#示例关键字行参
def f1(*,c,d):
    print("c=",c)
    print("d=",d)
 #f1(3,4)       报错
f1(c=3,d=4)
d={"c":30,"d":40}
f1(**d)


def f2(a,b,*args,c,d):
    print(a,b)
    print(args)
    print(c,d)
f2(1,3,4,5,c=200,d=500)