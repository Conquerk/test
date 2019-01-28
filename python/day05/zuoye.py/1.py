n=int(input("输入一个整数："))
#x=1
#while x<=n:
#    print("*"*x)
#    x+=1

#for y in range(n,0,-1):
 #   print("*"*y)
for y in range(1,n+1):
    z=n-y     #  计算空格个数
    print(" "*z+"*"*y)
print("----------")
for y1 in range(n,0,-1):
    z1=n-y1
    print(" "*z1+"*"*y1)