begin=int(input("输入一个开始值："))
end=int(input("输入一个结束值："))
i=begin
count=0
while i<=end:
    print(i,end=" ")
    count+=1
    if count % 5 == 0:
        print()
    #print(count,end=" ")
    i=i+1
print()