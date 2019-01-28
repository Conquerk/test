import random
x=random.randrange(0,101)
s=0
def cai():
    global s
    y=int(input("输入一个0-100之间的数:"))
    if y>x:
        print("您猜大了")
        s+=1
    if y<x:
        print("您猜小了")
        s+=1
    if x==y:
        s+=1
        print("恭喜您猜对了")
        print("您猜了",s,"次")
        return
    cai()
cai()
# while True:
#     y=int(input("输入一个0-100之间的数:"))
#     if y>x:
#         print("大")
#         s+=1
#     if y<x:
#         print("小")
#         s+=1
#     if y==x:
#         print("对")
#         s+=1
#         print(s)
#         break



