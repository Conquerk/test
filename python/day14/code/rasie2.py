#示意ｒａｉｓｅ　无参用法
def fa():
    print("fa开始")
    raise ValueError("故意制造一个错误")
    print("fa结束")


def fb():
    print("fb开始")
    try:
        fa()
    except ValueError as err:
        print("ｆａ中发生了错误以处理")
        #此处里将ｅｒｒ再次传递
        raise 
    print("fb结束")
try:
    fb()
except ValueError:
    print("再一次收到ｆｂ内部发生的错误")
