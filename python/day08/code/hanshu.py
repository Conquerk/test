#示例　　　写一个函数　　功能为　　给两个数据　把最大值数据打印
def mymax(a,b):
    m=a
    if b > m:
        m=b
        print("最大值为：",m)
mymax(100,200)