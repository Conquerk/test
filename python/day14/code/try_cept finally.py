def div_apple(n):
    print("现在有%d个苹果你想分给几个人？"% n)
    s=input("请输入人数")
    count= int(s) #可能触发　ｖａｌｕｅｅｒｒｏｒ　错误
    result=n/count#zeroDivisionerror
    print("每个人分了%d个苹果" %result)

try :
    div_apple(10)
except ValueError:
    print("分苹果时发生错误异常，已捕获并转为正常状态")
    print("拿回苹果")
except ZeroDivisionError:
    print("没有人拿苹果，苹果被收回")
else:   #  此语句只在此ｔｒｙ语句没有发生异常时执行
    print("未发生异常")
finally:
    print("分苹果结束")
    print("一定执行")