#序列传参
def mymin(a,b,c):
    print(a)
    print(b)
    print(c)
s1=[11,22,33]
mymin(s1[0],s1[1],s1[2])
mymin(*s1)#相当于mymin(11,22,33)
s2=(44,55,66)
s3="ABC"
mymin(*s2)
mymin(*s3)