#ndarray数组的掩码操作
import numpy as np

a = np.array([1,2,3,4,5,6,7,8])
f = np.array([True,False,True,False,True,False,
True,False])
print(a[f])
print(a[a > 3])
#把1-100中３的倍数或者７的倍数打印出来
a = np.arange(1,100)
flag_a = a % 3 == 0
flag_b = a % 7 == 0
print(flag_a)
print(flag_b)
flag = np.any([flag_a,flag_b],axis=0)
print(a[flag])