def zifuchuan():
    z=0
    x=input("请输入字符串：")
    for y in x :
        if  0x4e00<=ord(y)<=0x9fff:#中文字符串的编码值范围
            z+=1
    return z
print(zifuchuan())

