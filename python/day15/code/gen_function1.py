#示意生成器函数的调用顺序
def myyield():
    """这是一个生成器函数，
    此函数用来动态生成2，3，5，7"""
    print("即将生成2") 
    yield 2
    yield 3
    yield 5
    yield 7
    print("生成器函数调用结束") 
gen=myyield()
it=iter(gen)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))