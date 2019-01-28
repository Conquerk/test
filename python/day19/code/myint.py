class myint:
    def __init__(self,value):
        self.data=int(value)
    def __int__(self):
        """此方法必须返回整数"""
        return int(self.data)
    def __float__(self):
        return float(self.data)
n1=myint("100")
i=int(n1)   # 将myint类型装化为整数
print(i)
f=float(n1)
print(f)
c=complex(n1)
print(c)
b=bool(n1)
print(b)