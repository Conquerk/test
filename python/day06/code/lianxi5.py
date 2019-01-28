z=int(input("请输入开始值："))
y=int(input("请输入结束值："))
l=[x for x in range(z,y) if (x%2==0)]
print(l)