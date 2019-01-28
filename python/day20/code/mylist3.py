class mylist:
    def __init__(self,iterable=()):
        self.data=[x for x in iterable]
    def __repr__(self):
        return "{}".format(self.data)
    def __neg__(self):
        """重载负号运算符"""
        # l=[-x for x in self.data]
        l=(-x for x in self.data)
        return mylist(l)
    def __pos__(self):
        """重载正号运算符"""
        l=(abs(x) for x in self.data)
        return mylist(l)
l1=mylist([1,-2,3,-4,5])
l2=-l1
print(l2)
l3=+l1
print(l3)