#示例示意用＠ｐｒｏｐｅｒｔｙ　来实现ｇｅｔｔｅｒ　ｓｅｔｔｅｒ
class student:
    def __init__(self,s):
        self.__score=s  #成绩
    def get_score(self):
        """getter"""
        return self.__score
    def set_score(self,s):
        """setter"""
        assert 0<=s <=100,"成绩超出范围"
        self.__score=s
s1=student(59)　　
# print(s1.score) #取值
# s1.score=9999　　#赋值
print(s1.get_score())　　#用方法取值
s1.set_score(100)  #  用方法赋值
