#此示例　示意创建和使用实例属性
class dog:
    """这是一种可爱的小动物"""
    def eat(self,food):
        """用来描述小狗吃的行为"""
        print(self.color,"的",self.kinds,"正在吃",food)
        #以下让当前的小狗自己记住吃得是什么
        self.last_food=food
    def show_info(self):
        print(self.color,"的",self.kinds,"上次吃得是",self.last_food)
dog1=dog()
dog1.kinds="哈士奇"  # 创建属性
dog1.color="黑白相间"   #创建属性ｃｏｌｏｒ
dog1.color="白色"   #修改属性
print(dog1.color,"的",dog1.kinds)
dog1.eat("骨头")
dog2=dog()
dog2.kinds="藏獒"
dog2.color="黑色"
dog2.eat("狗粮")
dog1.show_info()
dog2.show_info()