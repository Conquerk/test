#先将字符串去重
x=input("输入一段字符串：")
l=[]
for ch in x:
    if ch not in l:
        l.append(ch)
for ch in l:
    print(ch,":",x.count(ch),"次")