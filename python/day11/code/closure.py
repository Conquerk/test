#定义很多个函数　每个函数求x**y y是可变的
# def pow2(x):
#     return x **2
# def pow3(x):
#     return x **3
# # .....
# def pow99(x):
#     return x**99 

def makepow(y):
    def fn (x):
        return x**y
    return fn
pow2=makepow(2)   # ｐｏｗ2　绑定一个闭包
print("5的平方是",pow2(5))  


