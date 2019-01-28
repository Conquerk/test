#此示例　示意覆盖
class A:
    def work(self):
        print("A.work被调用")
class B(A):
    def work(self):
        """此方法覆盖父类的ｗｏｒｋ"""
        print("B.work被调用")
b=B()
b.work()