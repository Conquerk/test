def fn_outter():
    print("fn_outter被调用")
    def fn_inner():
        print("fn_inner被调用")
    fn_inner()#调用一次
    fn_inner()#调用2次
    print("fn_outter调用结束")
    return fn_inner
f=fn_outter()  #相当于(fn_outter())()
#fn_inner()  #不可调用　
f()


def f1():
    print("1")
    def f2():
        print("2")
    return f2
f1()