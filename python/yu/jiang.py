# break 结束循环
# continue 终止当前循环　　　　　语句专属

# return      函数专属

# 1.实现什么功能
# 2.需要什么原材料
# 3.返回什么函数
# def outer():
#     x=1
#     def inner():
#         def inner_inner():
#             print(x)                闭包
#         inner_inner()
#         print(x)
#     inner()
# outer()

# def add(x, y):
#     return x + y
# def sub(x, y):
#     return x - y                 函数式编程
# def apply(func, x, y):
#     return func(x, y)
# print(apply(add, 10, 5))

# def outer():
#     def inner():
#         print("inner1") 
#     return inner
# x=outer()
# x()

def outer(some_func):
    def inner():
        print("before some_func")
        s=some_func()
        return s+1
    return inner
def foo():
    return 1
sss=outer(foo)
print(sss())
