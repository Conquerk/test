class human:
    """此类用于描述人类的共性"""
    def say(self,what):
        print("说",what)
    def walk(self,distance):
        print("走了",distance,"公里")
class student(human):
    def study(self,subject):
        print("正在学习",subject)
h1=human()
h1.say("天真蓝")
h1.walk(5)

s1=student()
s1.say("学习有点累")
s1.walk(1)
s1.study("python")