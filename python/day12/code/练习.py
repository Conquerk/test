import math
x=float(input("输入圆的半径："))
print("圆的面积为：",math.pi*(x**2))

y=float(input("请输入圆的面积："))
r2=math.sqrt(y/math.pi)
print("半径为",r2)