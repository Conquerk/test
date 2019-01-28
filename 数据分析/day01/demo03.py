import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a)
print('a.shape:',a.shape)
print('a.size:',a.size)
print('a.len:',len(a))
ary = np.arange(1,28)
ary.shape=(3,3,3)
print(ary,'ary.shape:',ary.shape)
#数组中的第一页第一行
print('ary[0]:',ary[0][0])
#数组第一页第一行第一个
print('ary[0]:',ary[0][0][0])
print('ary[0]:',ary[0,0,0])

for i in range(ary.shape[0]):
    for j in range(ary.shape[1]):
        for k in range(ary.shape[2]):
            print(ary[i,j,k],end='')

