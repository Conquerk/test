x=input("输入一段字符串：")
d={}
for y in x:
    if y not in d:
        d[y]=1
    else :
        d[y]+=1
for k,v in d.items():
    print(k,":",v,"次")