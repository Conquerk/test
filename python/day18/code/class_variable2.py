class car:
    #类变量用于保存汽车的个数
    total_count=0
    def __init__(self,info):
        self.info=info
        print("汽车",info,"被创建")
        self.__class__.total_count+=1
    def __del__(self):
        print("汽车",self.info,"被销毁")
        self.__class__.total_count-=1
c1=car("byd e6")
c2=car("吉利 e7")
print("汽车个数为",car.total_count)
del c1
print("汽车剩余个数",car.total_count)   # 1
input("输入空格结束")