class mylist:
    def __init__(self,iterable=()):
        self.data=[x for x in iterable]
    def __repr__(self):
        return "{}".format(self.data)
    def __add__(self,other):
        v=self.data + other.data
        obj=mylist(v)
        return obj
    def __mul__(self,n):
        v=self.data * n
        obj=mylist(v)
        return obj
    def __rmul__(self,n):
        v=self.data * n
        obj=mylist(v)
        return obj
l1=mylist(range(1,4))
l2=mylist([4,5,6])
l3=l1+l2
l4=l1.__mul__(3)
l5=l2+l1
l6=l1.__rmul__(2)   #  反向运算符的重载
print(l3)
print(l4)
print(l5)
print(l6)