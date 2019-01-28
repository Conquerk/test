z=0
for i in range(1,5):
    for x in range(1,5):
        for y in range(1,5):
            if i!=x and x!=y and y!=i:
                z+=1
                print(i,x,y)
print('共有%d种组合'%z)

#有四个数字：1、2、3、4，
# 能组成多少个互不相同且无重复数字的三位数？各是多少？