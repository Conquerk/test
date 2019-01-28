#猜想print 函数的形参 是如何定义的
def myprint(*args,sep=" ",end="\n"):
    print(*args,sep=sep,end=end)
myprint()
myprint(1,2,3,4)
myprint(1,2,3,4,sep="#")
myprint(1,2,3,4,sep="#",end="\n\n")
myprint("==================")