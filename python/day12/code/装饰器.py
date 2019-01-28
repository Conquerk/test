def mydeco(fn):
    def fx():
        print("++++这是ｆｎ被调用之前+++")
        fn()
        print("---这是ｆｎ被调用之后---")
    return fx    # 函数装饰器

@mydeco
def myfunc():
    print("myfunc被调用")

#以上＠mydeco等同于在ｍｙｆｕｎｃ之后了如下语句
#myfunc=mydeco(myfunc)
myfunc()
