class car:
    def run(self,speed):
        print("以",speed,"km/h的速度行驶")
class plane:
    def fly(self,height):
        print("以",height,"米高度飞行")
class planecar(car,plane):
    pass
p1=planecar()
p1.run(500)
p1.fly(10000)
