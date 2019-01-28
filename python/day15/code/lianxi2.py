l=[2,3,5,7,10,15]
print("生成器函数")
def sh():
    for x in l:
        yield (x**2)+1
for x in sh():
    print(x)
print("生成器表达式")
gen=((x**2)+1 for x in l)
for x in gen:
    print(x)
print("列表")
l1=[x**2+1 for x in l]
print(l1)                   