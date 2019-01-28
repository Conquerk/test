#此示例示意生成器函数的定义和使用:
def myyield():
    """这是一个生成器函数，
    此函数用来动态生成2，3，5，7"""
    yield 2
    yield 3
    yield 5
    yield 7
#用迭代器访问生成器函数
gen=myyield()  # 生成器函数调用将返回一个生成器
print(gen)  # gen 是一个生成器对象
it=iter(gen)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#print(next(it))  # stopiteration

print("以下用ｆｏｒ　语句访问生成器：")
for x in myyield():
    print(x)