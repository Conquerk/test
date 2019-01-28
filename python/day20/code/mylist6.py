class mylist:
    def __init__(self,iterable=()):
        self.data=[x for x in iterable]
    def __repr__(self):
        return "{}".format(self.data)
    def __getitem__(self,i):
        print('getitem被调用,i=',i)
        if type(i) is int:
            print("索引操作")
        if type(i) is  slice:
            print("切片操作")
            print("起始值",i.start)
            print("终止值",i.stop)
            print("布长",i.step)
        l=self.data[i]
        return l
    def __setitem__(self,i,n):
        print('setitem被调用，i=',i,'n=',n)
        print('嘿嘿')
        self.data[i]=n
    def __delitem__(self,i):
        del self.data[i]
l1=mylist([1,-2,3,-4,5])
x=l1[1::2]
print(x)