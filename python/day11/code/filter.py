def isodd(x):
    return x%2==1   #奇数返回ｔｒｕｅ　　偶数为ｆａｌｓｅ

#生成1-100内的奇数

for x in filter(isodd,range(100)):
    print(x)

#生成1-100的偶数放到ｅｖｅｎ中
even=[ x for x in filter(lambda x :x%2==0,range(100))]
print(even)