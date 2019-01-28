
def fx(f,x,y):
    print(f(x,y))

fx((lambda a,b:a+b),100,200)
fx((lambda a,b:a**b),3,4)
#   f 为　lambda a,b:a+b　　　　
#　　输出为f（100，200） f(3,4)