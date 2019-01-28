# def jisuan(n):
#     z=0
#     for x in range(1,n+1):
#         z=z+x**x
#     return z
# print(jisuan(2))
# print(jisuan(3))
# print(jisuan(5))
#方法2
def f(n):
    return sum(map(lambda x:x**x,range(1,n+1)))
print(f(5))