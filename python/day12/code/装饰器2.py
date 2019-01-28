#此示例用装饰器改变流程:
#银行业务：
#....写的装饰器：
def zhuangshi(fn):
    def fx(name,x):
        print("正在进行权限认证.")
        fn(name,x)
    return fx
#以下是..写的程序
@zhuangshi
def save_moeny(name,x):
    #添加正在进行权限验证
    print(name,"存钱",x,"元")
@zhuangshi
def withdraw(name,x):
    print(name,"取钱",x,"元")
#以下为...写的程序
save_moeny("小王",200)
save_moeny("小赵",400)
withdraw("小李",500)