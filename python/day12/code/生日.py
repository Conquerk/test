#输入出生日期算出算出你出生已经过了多少天算出你出生那天是星期几
y=int(input("年"))
m=int(input("月"))
d=int(input("日"))
t=(y,m,d,0,0,0,0,0,0,)
import time
birth=time.mktime(t)
muqian=time.time()
huo=muqian-birth
day=huo/60/60//24
print(day,"天")

t=time.localtime(birth)
d={0:"一",1:"二",2:"三",3:"四",4:"五",5:"六",6:"日"}
print("出生的那个星期为",d[t[6]])