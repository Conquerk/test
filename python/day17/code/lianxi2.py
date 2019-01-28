class student:
    def __init__(self,name,age,score="0"):
        self.get_name=name
        self.get_age=age
        self.get_score=score
    def set_score(self,num):
        self.get_score=num
        print("修改完成")
    def show_info(self):
        print("姓名：",self.get_name,"年龄：",
        self.get_age,"成绩：",self.get_score)
l=[]
l.append(student("小张",20,100))
l.append(student("小李",18))
l.append(student("小赵",19,85))
for s in l:
    s.show_info()
l[1].set_score(70)
for s in l :
    s.show_info()
