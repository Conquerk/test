#此示例示意类变量的定义方法和用法
class car:
    #类变量用于保存汽车的个数
    total_count=0
print(car.total_count)   # 读取类变量的值
car.total_count+=100   # 修改类变量
print(car.total_count) # 100

c1=car()
c1.total_count=999
print(c1.total_count) # 999 
print(car.total_count)# 100 
#类变量可以通过此类的对象的_class_属性间接访问
c1.__class__.total_count=8888
print(c1.total_count)  # 999
print(car.total_count) # 8888