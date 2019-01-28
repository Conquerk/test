#先遍历1-100　之间的数，如果这个数是素数加入到一个列表
l=[]#准备加入素数
for x in range(1,101):
    #如果ｘ是素数则加入ｌ　中：
    isprime=True # 先假设ｘ　是素数
    #如果不是素数则把ｉｓｐｒｉｍｅ置为ｆａｌｓｅ
    if x < 2 :
        isprime=False
    else:
        for i in range(2,x):
            if x % i ==0: # 整除　不是素数
                isprime=False
                break
    if isprime:#一定为素数
        l.append(x)      
print(l)      