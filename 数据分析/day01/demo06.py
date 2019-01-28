import numpy as np
a = np.arange(1,10)
print(a)
print(a[:3])
print(a[3:6])
print(a[6:])
print(a[::-1])
print(a[:-4:-1])
print(a[-7::-1])
print(a[::])
print(a[::3])
print(a[1::3])
print(a[2::3])
a.resize(3,3)
#切出第１／２行　与　１／２／３列
print(a[1:,:])
#切出１／２行与１／２列
print(a[1:,1:])
