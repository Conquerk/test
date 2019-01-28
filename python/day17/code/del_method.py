class car:
    def __init__(self,info):
        self.info=info
        print("汽车：",info,"对象被创建")
    def __del__(self):
        print("汽车：",self.info,"对象被销毁")
c1=car("BYD E6")
c2=c1
del c1
input("按回车键继续执行程序：")
print("程序正常退出")
