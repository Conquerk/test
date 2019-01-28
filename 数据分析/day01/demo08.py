#多维数组的组合与拆分
import numpy as np

a = np.arange(1,7).reshape(2,3)
b = np.arange(7,13).reshape(2,3)
#垂直方向操作
c = np.vstack((a,b))
print(c)
a,b = np.vsplit(c,2)#拆成２份
print(a,'\n',b)

#水平方式操作
d = np.hstack((a,b))
print(d)
a,b = np.hsplit(d,2)
print(a,'\n',b)

#深度方向
e = np.dstack((a,b))
print(e)
a,b = np.dsplit(e,2)
print(a,'\n',b)

a = a.reshape(2,3)
b = b.reshape(2,3)
print(a,'\n',b)

c = np.concatenate((a,b),axis=1)
print(c)
#测试不同长度的数组组合
a = np.arange(1,7)
b = np.arange(10,16)
c = np.pad(b,
pad_width=(0,1),mode='constant',constant_values=-1)
print(a)
print(b)
print(c)

#简单的一维数组的组合方案
a = np.arange(1,10)
b = np.arange(11,20)
#把a与b摞在一起成为两行
c = np.row_stack((a,b))
#把a和b并在一起成为两列
d = np.column_stack((a,b))
print(c)
print(d)


