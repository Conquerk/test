l=[]#   保存字典
# 循环输入　，姓名为空结束输入
while True:
    x=input("请输入姓名：")
    if not x:
        break
    y=input("请输入年龄：")
    z=input("请输入成绩：")
    d={"name":x,"age":y,"score":z}
    l+=[d]
print(l)