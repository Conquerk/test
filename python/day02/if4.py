num=input("请输入月份：")
num=int(num)
if 1<=num<=3:
    print("春季")
elif 4<=num<=6:
    print("夏季")
elif 7<=num<=9:
    print("秋季")
elif 10<=num<=12:
    print("冬季")
else :
    print("您输入错了")
