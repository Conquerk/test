class a :
    def go(self):
        print("a")
class b(a):
    def go(self):
        print("b")
        super().go()
class c(a):
    def go(self):
        print("c")
class d (b,c):
    def go(self):
        print("d")
        super().go()
x=d()
x.go()
x1=d.__mro__
print(x1)