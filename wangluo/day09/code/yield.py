def fun():
    print("启动生成器")
    yield 2
    print("生成器完成")
try:
    g=fun()
    print(next(g))
    print(g.__next__())
    g.close()
except StopIteration:
    print("已结束")