s=input("输入的字符串为：")
print("第一个字符为：",s[0])
print("最后一个字符为：",s[-1])
if len(s) % 2 ==1:
    print("中间字符是：",s[len(s)//2])