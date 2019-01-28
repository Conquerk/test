class car:
    def __init__(self,c,b,m):
        self.color=c
        self.brand=b
        self.model=m
        print("此方法被调用")
    def run(self,speed):
        print("{}的{}{}正在以{}公里/小时的速度行驶"
        .format(self.color,self.brand,self.model,speed))
a4=car("红色","奥迪","A4")
a4.run(199)
print(dir(a4))
print(a4.__dict__["color"])