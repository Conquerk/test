#此示例　示意静态方法的定义和使用
class x:
    @staticmethod
    def myadd(a,b):
        """这是静态方法"""
        return a+b
print(x.myadd(100,200))
a=x()
print(a.myadd(100,200))