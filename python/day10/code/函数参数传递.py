#此示例示意函数作为实参传递

def f1():
    print("heoll f1")
def f2():
    print("heollo f2")
def fx(fn):
    print(fn)  #　　　ｆｎ绑定ｆ1
    #print(fn()) # 调用函数    none
    fn()   # 调用函f1的函数
fx(f1)
fx(f2)
