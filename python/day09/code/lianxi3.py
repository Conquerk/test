def min_max(*args):
    if len(args)==0:
        return ("报错")
    y=max(args)
    x=min(args)
    return (x,y)
print(min_max(1,2,3,4,5))
x,y=min_max(4,5,6,7,8,9)
print("最小值为：",x)
print("最大值为：",y)
print(min_max())