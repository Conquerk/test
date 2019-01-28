class student:
    def __init__(self,name,money,loan):
        self.name=name
        self.money=money
        self.loan=loan
    def jie(self,other,x):
        other.money-=x
        self.money+=x
        self.loan+=x

name1=student("小张",100,0)
name2=student("小李",0,0)
name2.jie(name1,20)
print("小张有",name1.money)
print("小李有",name2.money)
print("小李外债",name2.loan)
