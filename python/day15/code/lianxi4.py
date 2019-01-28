def get_test():
    l=[]
    while True:
        x=input("请输入:")
        if not x :
            break
        else:
            l.append(x)
    print("输出如下：")
    for x in enumerate(l,1):
        print("第{}行".format(x[0]),x[1])

get_test()