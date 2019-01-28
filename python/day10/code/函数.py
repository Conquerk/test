#示例　函数变量名绑定函数
def fn():
    print("hello world")
f1=fn   # fn绑定ｆｎ（）这个函数
print(f1)  #<function fn at 0x7fc742139f28>
fn() #hello world
f1()#hello world
f2=fn()
print(f2)   #none 返回了空


def f1():
    print("heoll f1")
def f2():
    print("heollo f2")
f1,f2=f2,f1
f1()   # hello f2    交换