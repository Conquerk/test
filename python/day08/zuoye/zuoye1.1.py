def zifu(s):
    x=0 # 个数　
    #用来记录中文数
    for ch in s:
        if  ord(ch)>127:
            x+=1
    return x 
s=input("请输入字符：")
print(zifu(s))

