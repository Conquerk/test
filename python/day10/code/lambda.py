#示例　匿名函数
def myadd(x,y):
    return x+y
#可以用ｌａｍｂｄａ改写如下：
myadd=lambda x,y:x+y
print("20+30=",myadd(20,30))
print("100+200=",myadd(100,200))
