#示例示意自定义模块
"""这是一个自定义模块

这是一个模块的文档描述
此模块两个函数两个变量"""

def mysum(n):
    print("正在计算1+2+3+4+....ｎ",n,"的和")
def myfac(n):
    print("正在计算%d!"%n)
name1="Audi"
name2="Tesls"
print("mymod模块被加载")
print(__name__)