from threading import Thread
from time import sleep,ctime

class Mythread(Thread):
    def __init__(self,target,args=(),kwargs={},name='mythread-1'):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.name = name
    def run(self):
        self.target(*self.args,**self.kwargs)
def player(sec,song):
    for i in range(2):
        print("%s开始播放，播放时间为%s"%(song,ctime()))
        sleep(sec)
t=Mythread(target=player,args=(3,),
  kwargs={'song':"奇迹再现"},name="风")
t.start()
t.join()