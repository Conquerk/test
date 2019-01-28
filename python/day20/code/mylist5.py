class mylist:
    def __init__(self,iterable=()):
        self.data=[x for x in iterable]
    def __repr__(self):
        return "{}".format(self.data)
    def __getitem__(self,i):
        print('getitem被调用,i=',i)
        l=self.data[i]
        return l
    def __setitem__(self,i,n):
        print('setitem被调用，i=',i,'n=',n)
        print('嘿嘿')
        self.data[i]=n
    def __delitem__(self,i):
        del self.data[i]
l1=mylist([1,-2,3,-4,5])
x=l1[2]  # l1.__getitem__(2)
print(x)
l1[1]=2.2  # l1.__setitem__(1,2.2)
print(l1)
del l1[4]
print(l1)