#此示例　示意用ｓｕｐｅｒ函数显示的调用被覆盖的方法
class A:
    def work(self):
        print("A.work被调用")
class B(A):
    def work(self):
        """此方法覆盖父类的ｗｏｒｋ"""
        print("B.work被调用")
    def mywork(self):
        #调用自己的方法
        #调用父类的方法
        self.work()
        super(B,self).work()
b=B()
# b.work()
# A.work(b)
# super(B,b).work()
b.mywork()