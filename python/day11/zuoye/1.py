# def jiecheng(x):
#     z=1
#     s=0
#     for x in range(1,x+1):
#         z*=x
#         s+=z
#     print(s)
# jiecheng(20)
# jiecheng(4)
def myfac(n):
    #如果n=1则知道1的阶乘是一　直接返回
    if n == 1:
        return 1
    #否则进入递推阶段等待下一个结果后返回
    return n*myfac(n-1)
def s(n):
    l=0
    for x in range(1,n+1):
        y=myfac(x)
        l+=y
    print(l)
s(20)


