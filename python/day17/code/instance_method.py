#为ｄｏｇ类添加　吃　玩　睡　等示例方法，以实现ｄｏｇ对象的相应行为
class dog:
    """这是一种可爱的小动物"""
    def eat(self,food):
        """用来描述小狗吃的行为"""
        print("id为{}的".format(id(self)),end="")
        print("小狗正在吃{}".format(food))
    def sleep(self,hour):
        """描述小狗睡觉"""
        print("id为{}的小狗睡了{}个小时".format(id(self),hour))
    def play(self,xi):
        """描述小狗玩的行为"""
        print("id为{}的小狗正在玩{}".format(id(self),xi))

dog1=dog()
dog1.eat("骨头")
dog1.sleep(1)
dog1.play("球")
dog2=dog()
dog2.eat("狗粮")
dog2.sleep(2)
dog2.play("飞盘")