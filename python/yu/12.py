list=[]
while True:
    x=int(input("请输入一个数："))
    if len(list)>9:
        break
    list+=[x]
    list.sort(reverse=False)  
print("列表为：",list)
print("排序后的列表为：",list)
