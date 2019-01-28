count=0
def hello(name):
    global count
    print("你好",name)
    count+=1
hello("Tom")
hello("jerry")
print("hello被调用了%d次"%count)