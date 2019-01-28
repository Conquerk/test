def myadd(x,y):
    print(100,200)

#不可重入函数
s=0
def myadd2(x,y):
    global  s
    s+=x+y
    return s
