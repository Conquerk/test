# 用ｉｆ语句嵌套
num=input("请输入月份：")
num=int(num)
if 1<=num<=12:
    print("用户输入的是合法月份")
    if num<=3:
        print("春季")
    elif num<=6:
        print("夏季")
    elif num<=9:
        print("秋季")
    elif num<=12:
        print("冬季")
else:
    print("用户您出错了")