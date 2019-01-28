# 2.	写一个程序，以电子时钟格式显示时间：
# 格式为：
# 	HH:MM:SS  15:58:26
import time
# while True:
#     x=time.time()
#     y=time.localtime(x)
#     time.sleep(1)
#     print(y[3],":",y[4],":",y[5],end="\r")
def clock():
    while True:
        t=time.localtime()
        time.sleep(1)
        print("%02d:%02d:%02d" % (t[3],t[4],t[5]),end="\r")
clock()