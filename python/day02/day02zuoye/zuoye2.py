x=int(input("学生的第一科成绩："))
y=int(input("学生的第二科成绩："))
z=int(input("学生的第三科成绩："))
#if x>y>z:
    # print("最高分为：",ｘ,"最低分为：",z,"平局分为：",(x+y+z)/3)
# elif x>z>y:
    # print("最高分为：",ｘ,"最低分为：",y,"平局分为：",(x+y+z)/3)
# elif y>x>z:
    # print("最高分为：",y,"最低分为：",z,"平局分为：",(x+y+z)/3)
# elif y>z>x:
    # print("最高分为：",y,"最低分为：",x,"平局分为：",(x+y+z)/3)
# elif z>x>y:
    # print("最高分为：",z,"最低分为：",y,"平局分为：",(x+y+z)/3)
# elif z>y>x:
    # print("最高分为：",z,"最低分为：",x,"平局分为：",(x+y+z)/3)
a=(x,y,z)
print("成绩最高为：",max(a))
print("成绩最低为：",min(a))
print("平均成绩为：",round((x+y+z)/3))