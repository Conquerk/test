s1={"曹操","刘备","孙权"}   #经理
s2={"曹操","孙权","张飞","关羽"} # 技术员
print("即是经理也是技术员的人：",s1&s2)
print("是经理但不是技术员的人：",s1-s2)
print("是技术员但不是经理的人：",s2-s1)
if "张飞"in s1 :
    print("张飞是经理")
else:
    print("张飞不是经理")
print("身兼一职的人为：",s1^s2)
print("经理和技术员共有",len(s1|s2),"人")