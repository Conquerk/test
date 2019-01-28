# def myfac(n):
#     z=1
#     for x in range(1,n+1):  #1 2 3 4 5
#         z=z*x
#     print(z)
# myfac(5)
# myfac(6)
# myfac(4)
#递归：
def myfac(n):
    #如果n=1则知道1的阶乘是一　直接返回
    if n == 1:
        return 1
    #否则进入递推阶段等待下一个结果后返回
    return n*myfac(n-1)
print(myfac(5))

