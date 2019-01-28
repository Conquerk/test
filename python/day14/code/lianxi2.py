def get_age():
    try:
        x=int(input("输入1-140之间的整数"))
    except ValueError:
        raise ValueError("不是数字")
    if x<1:
        raise ValueError("年龄太小")
    if x>140:
        raise ValueError("年龄太大")
    return x
try:
    age=get_age()
    print("你的年龄是{}".format(age))
except ValueError as err:
    print("你输入的不是1-140之间的数",err)
    