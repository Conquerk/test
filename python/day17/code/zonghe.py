class human:
    def __init__(self,name,age):
        self.get_name=name # 姓名
        self.get_age=age   #年龄
        self.money=0        #钱
        self.skill=[]   #年龄
    def teach(self,other,skill):
        print(self.get_name,"教",other.get_name,skill)
        other.skill.append(skill)
    def work(self,money):
        print(self.get_name,"上班赚了",money,"元")
        self.money+=money
    def borrow(self,other,money):
        print(self.get_name,"向",other.get_name,"借了",money)
        self.money+=money
        other.money-=money
    def show_info(self):
        print(self.get_age,"岁的",self.get_name,"有钱",self.money,"元","他学会的技能为",",".join(self.skill))
zhang3=human("张三",35)
li4=human("李四",8)
zhang3.teach(li4,"python")
li4.teach(zhang3,"英雄联盟")
zhang3.work(1000)
li4.borrow(zhang3,200)
zhang3.show_info()
li4.show_info()
