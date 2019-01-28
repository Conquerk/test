#此示例示意类内__slots__列表的用法
class human:
    #限制ｈｕｎｍａｎ类只能有name age属性
    __slots__=["name","age"]
    def __init__(self,n,a):
        self.name,self.age=n,a
    def show_info(self):
        print(self.name,self.age)
s1=human("Tarena",15)
s1.show_info()
s1.Age=16
s1.show_info()