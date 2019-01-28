#列表推到式            
l=[x**2 for x in range(1,10)]
print(l)
#　保留偶数
y=[x**2 for x in range(1,10)if (x%2==0)]
print(y)

l=[x+y for x in "abc" for y in "123"]
print(l)
