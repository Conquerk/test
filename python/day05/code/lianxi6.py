y=int(input("输入开始值："))
z=int(input("输入结束值："))
for x in range(y,z):
    if x%2==0:
        continue
    print(x,end=" ")
print()

