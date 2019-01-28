l1=['大王','小王']
def paizu(a):
    global l1
    x=ord(a)
    y=chr(x)
    l=['A','2','3','4','5','6','7','8','9','J','Q','K','10']
    for a in l:
            a=y+a
            l1+=[a]
    return l1
paizu('\u2660')
paizu('\u2663')
paizu('\u2665')
paizu('\u2666')
print(l1)
import random
def fapai1():
    global l1
    l2=random.sample(l1,17)
    l3=[]
    for x in l1:
        if x not in l2:
            l3+=[x]
    l1=l3
    return l2
def kaishi():
    global l
    while True:
        x=input("第一个人的牌")
        if not x :
            print(fapai1())
            break
    while True:
        x=input("第二个人的牌")
        if not x :
            print(fapai1())
            break
    while True:
        x=input("第三个人的牌")
        if not x :
            print(fapai1())
            break
    while True:
        x=input("底牌")
        if not x :
            print(l1)
            break
kaishi()



