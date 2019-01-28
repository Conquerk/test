for x in range(1,10):
    #每循环一次打印一行
    for y in range(1,x+1):
        print("{}x{}={}\t".format(y,x,x*y),end="")
    print()