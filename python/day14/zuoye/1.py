# def qiu(n,count=0,a=100):
#     x=n/2
#     count+=1
#     if count <10:
#         a=a+n
#     if count==10:
#         print("第{}次落地后反弹：".format(count),x)
#         print("十次后经过的总路程为：",a)
#         return 
#     qiu(x,count,a)
# qiu(100)

# s=100
# a=100
# for x in range(10):
#     s=s/2
#     a+=s*2
# print("落地十次后反弹：",s)
# print(a)


def get_height(meter,times):
    """根据小球的初始高度ｍｅｔｅｒ和次数,返回最后的反弹高度"""
    for _  in range(times):
        meter/=2
    return meter
print("球落地十次后弹起的高度为",get_height(100,10))


def get_distance(meter,times):
    s=0 #记录球的总行程
    for _ in range(times):
        #记录下落时行程，算出反弹高度，在记录反弹行程
        s+=meter
        meter/=2
        s+=meter
    return s
print("球在第十次反弹后的总行程是：",get_distance(100,10))