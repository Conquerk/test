a=int(input("输入一个整数："))
print('#'*a)
i=1
while i<=(a-2):
    print('#'+' '*(a-2)+'#')
    i+=1
if i>1:
    print('#'*a)
