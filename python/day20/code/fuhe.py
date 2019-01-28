class mylist:
    def __init__(self,iterable=()):
        self.data=[x for x in iterable]
    def __repr__(self):
        return "{}".format(self.data)
    def __add__(self,other):
        print("add方法被调用")
        v=self.data + other.data
        obj=mylist(v)
        return obj
    def __iadd__(self,other):
        print("iadd被调用")
        self.data.extend(other.data)
        return self.data
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
l1+=l2
print("l1=",l1)
print("l2=",l2)