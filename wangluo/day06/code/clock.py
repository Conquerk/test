from multiprocessing import Process
from time import ctime,sleep
class ClockProcess(Process):
    def __init__(self,values):
        self.values=values
        #父类的＿init__
        super().__init__()
    def run(self):
        for i in range(5):
            print("the time is {}".format(ctime()))
            sleep(self.values)
p=ClockProcess(2)
p.start()  #会自动运行run方法
p.join()