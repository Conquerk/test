# 示例示意用ｗｉｔｈ　管理的对象
class A:
    """此类的对象将可用于ｗｉｔｈ中"""
    def __enter__(self):
        print("已经进入到ｗｉｔｈ语句内部")
        return self   #把自己返回由ａｓ绑定
    def __exit__(self,e_t,e_v,e_tb):
        """e_t 绑定异常类型
            e_v 绑定异常对象
            e_yb 绑定追踪对象"""
        if e_t is None:
            print("以正常离开")
        else:
            print("出现异常，走异常流程离开ｗｉｔｈ")
with A() as a:
    print("这是ｗｉｔｈ语句内的ｐｒｉｎｔ")
    int(input("请输入整数"))