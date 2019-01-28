#示例示意　ｉｎ　ｎｏｔ　ｉｎ　运算符
class mylist:
    def __init__(self,iterable=()):
        self.data=[x for x in iterable]
    def __repr__(self):
        return "{}".format(self.data)
    def __contains__(self,e):
        """重载ｉｎ　运算符　
        只需要判断　ｅ　是否在　ｓｅｌｆ里"""
        return e in self.data
l1=mylist([1,-2,3,-4,5])
print(3 in l1)  # true
print(3 not in l1)  # false
print(4 not in l1)  #  true
print(-4 in l1)  #  true