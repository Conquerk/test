import numpy as np
import matplotlib.pyplot as mp
#绘制一条线相关的ＡＰＩ
x = [1,2,3,4,5]
y = [7,8,9,2,3]
mp.plot(x,y,linestyle='dashdot',linewidth='2',color='pink')
#绘制水平线和垂直线
mp.vlines(5,0,10)
mp.hlines(3,0,10)
#绘制一条抛物线 在【－１０，１０】的区间均分十个点
x = np.linspace(-10,10,10)
print(x)
y = x**2
mp.plot(x,y)
mp.show()

