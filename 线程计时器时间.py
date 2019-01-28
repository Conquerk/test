from threading import Thread
import time
def getTime(interval):
    while True:
        time.sleep(interval)
        print(time.ctime().split(" ")[3],end='\r')
if __name__ == '__main__':
    #　创建线程计时器
    t = Thread(target=getTime, args=(1,))
    t.start()
