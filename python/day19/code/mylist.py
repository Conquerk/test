class mylist:
    def __init__(self,iterable=()):
        self.data=[x for x in iterable]
    def __str__(self):
        return "mylist({})".format(self.data)
    def __len__(self):
        """此方法必须返回整数"""
        return len(self.data)   
    def __abs__(self):
        """此方法实现把self的所有元素取局对值后
        返回全为正数字符串列表"""
        lst=[abs(x) for x in self.data]
        l=mylist(lst)
        return  l  
myl=mylist([1,-2,3,-4])
print(myl)
print("myl的长度是：",len(myl)) #调用myl.__len__()

myl3=(abs(myl))
print(myl3)    #  mylist([1,2,3,4])
# myl2=mylist()
# print(myl2)