s=0 # 次变量用来保存输入的数字的和
while True:
    n=int(input("请输入整数："))
    if n<0:
        break
    s+=n  # 累加
print("和是：",s)