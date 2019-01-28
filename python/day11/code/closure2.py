def fx(a,b,c):
    def fx1(x):
        return a*x**2+b*x+c
    return fx1
f1=fx(3,4,5)
print(f1(2))  #给出ｘ　的值  求ｆ1的值
