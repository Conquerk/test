#array数组的维度操作
import numpy as np
a = np.arange(1,9)
#视图变维使用的还是原始数组中的数据
b = a.reshape((2,4))
print(a,b)
c = b.ravel()
print(c)

#测试flatten()方法
d = b.flatten()
d[0]=111
print(b,d)

#就地变维
d.resize(2,2,2)
print(d)
d.shape = (2,4)
print(d)
