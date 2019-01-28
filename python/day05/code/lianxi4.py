a=input("输入字符串")
y=0
for x in a:
    if ord(x)>127:
        y+=1
print(y)