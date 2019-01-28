 #此　示例示意用生成器函数创建生成从0到ｎ结束的一系列整数
def myinteger(n):
    i=0  #　初始值为ｏ
    while i<n:
        yield i  #生成ｉ给　ｎｅｘｔ（ｉｔ）使用
        i+=1#为生成下一个数据做准备
for x in myinteger(5):
    print(x)