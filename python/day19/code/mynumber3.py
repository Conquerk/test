class mynumber(object):
    """此类定义一个自定义的数字类型"""
    def __init__(self,value):
        self.data=value

    def __str__(self):
        """重写ｏｂｊｅｃｔ类中的__str__(obj)"""
        return "数字%d" % self.data
    def __repr__(self):
        return "mynumber({})".format(self.data)
n1=mynumber(100)
s1=str(n1)    #s1＝ 数字100
s2=repr(n1)
print(s1)
print(s2)