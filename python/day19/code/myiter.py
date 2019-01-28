class mylist:
    def __init__(self,iterable=()):
        self.data=[x for x in iterable]
    def __repr__(self):
        return "{}".format(self.data)
    def __iter__(self):
        """必须返回迭代器"""
        return mylist_iterator(self.data)
class mylist_iterator:
    def __init__(self,data):
        self.data=data   # 绑定可迭代对象的数据
        self.cur_index=0 # 设置迭代器的起始位置
    def __next__(self):
        """此方法用啦实现迭代器协议"""
        if self.cur_index >=len(self.data):
            raise StopIteration
        #拿到当前索引指向的数
        r=self.data[self.cur_index]
        #将索引数指向下一个数
        self.cur_index+=1
        return  r
l=mylist("ABCD")
print(l)
for x in l:
    print(x)