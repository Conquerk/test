l=[]
l1=[]
l2=[]
while True:
    x=int(input("输入整数："))
    if x==0:
        break
    l+=[x]
print("整数列表：",l)
l1=[x for x in l if x>0]
l2=[x for x in l if x<0]
print("正数列表：",l1)
print("负数列表：",l2)