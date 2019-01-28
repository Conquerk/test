#*号元组行参
def func(*args):
    print("用户输入的参数个数是：",len(args))
    print("args",args)
func()
func(1,2,3)
func(1,2,3,1,1,"aaa") 