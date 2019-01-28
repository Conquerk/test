#字典行参
def fun(**kwargs):
    print("关键字传参个数是",len(kwargs))
    print("kwargs",kwargs)
fun(a=1,b="BBBB",c=[2,3,4])#关键字传参
fun(a=1,b=2,c=3,d=4)