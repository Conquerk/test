#示意多态中的动态
class shape:
    def draw(self):
        print("shape.draw被调用")
class point(shape):
    def draw(self):
        print("point.self被调用")
class circle(point):
    def draw(self):
        print("circle.self被掉用")
def my_draw(s):
    s.draw()   # 此处显示出多态中的动态
s1=circle()
s2=point()
my_draw(s2)
my_draw(s1)