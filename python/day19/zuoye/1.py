#示意　斐波拿妾　数列
class fibonacci:
    def __init__(self,n):
        self.count=n # 要生成数据的个数
    def __iter__(self):
        return feibo_it(self.count)
class feibo_it:
    def __init__(self,cnt):
        self.count=cnt
        self.a=0
        self.b=1   # 绑定当前斐波那契数
        self.cnt_count=0 # 记录已经生成多少
    def __next__(self):
        """由迭代器生成斐波那契数"""
        # 将以生成的数　+1
        self.cnt_count+=1
        if self.cnt_count > self.count:
            raise StopIteration # 生成完毕
        v=self.b   # 要返回的值
        # 算出下一个数
        self.a,self.b=self.b,self.a+self.b
        return v
l=fibonacci(5)
for x in l:
    print(x)