#此示例　示意发送错误通知的用发

def make():
    print("函数开始")
    
    #发出ZeroDivisionError类型的错误给调用者
    e=ValueError("值错误")  #  (xxxx)　创建一个错误对象
    raise e
    print("函数结束")
try:
    make()
except ZeroDivisionError:
    print("接收到ｍａｋｅ发出的错误通知")
except ValueError as ree:
    print("va...",ree)
print("函数正常结束")