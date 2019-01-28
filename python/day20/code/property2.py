#示例示意用＠ｐｒｏｐｅｒｔｙ　来实现ｇｅｔｔｅｒ　ｓｅｔｔｅｒ
class student:
    def __init__(self,s):
        self.__score=s  #成绩
    @property
    def score(self):
        """getter"""
        print("调用ｇｅｔｔｅｒ")
        return self.__score
    @score.setter
    def score(self,s):
        """setter"""
        print("调用ｓｅｔｔｅｒ")
        assert 0 <= s <=100,"成绩超出范围"
        self.__score=s
s1=student(65)
print(s1.score) #取值
s1.score=88 #赋值
print(s1.score)
