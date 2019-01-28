# 多继承标识符冲突问题
#狗写的一个发方法
class a:
    def m(self):
        print("a.m被调用")
#猫写的方法
class b:
    def m(self):
        print("b.m被调用")
#456觉得　猫　狗　写的类都能用
class c(a,b):
    def m(self):
        print("ab.m被调用")
ab=c()
ab.m()