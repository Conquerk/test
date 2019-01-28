class human:
    def __init__(self,n,a):
        self.name=n
        self.age=a
        print("human.__init__被调用")
    def show_info(self):
        print("姓名",self.name)
        print("年龄",self.age)
class student(human):
    def __init__(self,n,a,s=0):
        super(student,self).__init__(n,a)
        self.score=s
        print("student.__init__被调用")
    def show_info(self):
        super().show_info()
        print("成绩",self.score)
s=student("小张",20,100)
s.show_info()         