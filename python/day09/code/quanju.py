#示例　全局变量与局部变量：
a=100  # 全局变量
b=200   #全局变量
def fx(c):  #c是局部变量
    d=400
    a=10000   #d 局部变量
    print(a,b,c,d)
fx(300)
print("a=",a)
print("b=",b)
#print("c=",c)  # 出错
#print("d=",d)　# 出错