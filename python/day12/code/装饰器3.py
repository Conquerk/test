#此装饰器用来增加权限验证
def zhuangshi(fn):
    def fx(name,x):
        print("正在进行权限认证.")
        fn(name,x)
    return fx
#此装饰器用来增加短消息提醒功能
def tixing(fn):
    def fy(name,x):
        fn(name,x)
        print("正在发送.....")
    return fy
#以下是..写的程序
@zhuangshi
@tixing
def save_moeny(name,x):
    #添加正在进行权限验证
    print(name,"存钱",x,"元")
@tixing
@zhuangshi
def withdraw(name,x):
    print(name,"取钱",x,"元")
#以下为...写的程序
save_moeny("小王",200)
save_moeny("小赵",400)
withdraw("小李",500)