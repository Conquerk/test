def input_numbers():
    l=[]
    while True:
        x=int(input("请输入一个数"))
        if x < 0:
            break
        l+=[x]
    return l
l=input_numbers()
print(l)
print(max(l))
print(min(l))
print(sum(l))
