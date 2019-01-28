x=float(input("请输入公里数："))
if x<=3:
    print("费用金额为：",13)
elif 3<x<=15:
    print("费用金额为：",round(13+2.3*(x-3)))
elif x>15:
    print("费用金额为：",round(13+2.3*(x-3)+2.3*0.5*(x-15)))