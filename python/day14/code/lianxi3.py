s={"悟空","八戒","三藏","杀生"}
it=iter(s)
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        print("遍历结束")
        break