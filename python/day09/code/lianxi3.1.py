def min_max(a,*args):
    zuixiao=a
    for x in args:
        if x < zuixiao :
            zuixiao=x
    zuida=a
    for z in args:
        if z > zuida :
            zuida=z
    return(zuixiao,zuida)
print(min_max(10,20,30))
x,y=min_max(1,2,3,45,89,78,0)
print("最小值为：",x)
print("最大值为：",y)
#print(min_max())     　　　