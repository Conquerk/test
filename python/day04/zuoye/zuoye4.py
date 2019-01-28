n=int(input("输入一个整数："))
line=1
while line<=n:
    #　以ｌｉｎｅ为开始打印ｎ个数　打印在一行内
    start=line  #起始值是行号
    while start<=line:
        print(n,end=" ")
        n+=1
        print() #换行　
    line+=1
