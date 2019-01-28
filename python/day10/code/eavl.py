x=100
y=200
s="100+200"
print(eval(s))


# 让　结果改变
#设局部作用域内　x=1，y=2
v2=eval(s,None,{"x":1,"y":2})
print(v2)
#设局部作用域有y=2，全局作用域有x=10,y=30
v3=eval(s,{"x":10,"y":30},{"y":2})
print(v3)