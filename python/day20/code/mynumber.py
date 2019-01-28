#示意运算符的重载
class mynumber:
    def __init__(self,value):
        self.data=value
    def __repr__(self):
        return "{}".format(self.data)
    def __add__(self,other):
        v=self.data+other.data
        obj=mynumber(v)
        return obj
    def __sub__(self,other):
        v=self.data-other.data
        obj=mynumber(v)
        return obj
n1=mynumber(100)
n2=mynumber(200)
n3=n1+n2  # 等同于　n1.__add__(n2)
print(n1,"+",n2,"=",n3)
n4=n1-n2
print(n1,"-",n2,"=",n4)