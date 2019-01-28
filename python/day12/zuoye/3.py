import time
# def nao():
#     b=int(input("日"))
#     y=int(input("时"))
#     m=int(input("分"))
#     d=int(input("秒"))
#     l=(2018,9,b,y,m,d,0,0,0)
#     x=time.mktime(l)
#     z=time.time()
#     c=x-z
#     time.sleep(c)
#     print("时间到")
# nao()
def alarm(h,m):
    print("设置的时间为：%02d:%02d" % (h,m))
    while True:
        t=time.localtime()
        t2=t[3:5]
        if t2 ==(h,m):
            print("时间到")
            break 
        print("%02d:%02d:%02d" % (t[3:6]),end="\r")
        time.sleep(1)
hour=int(input("时"))
minute=int(input("分"))
alarm(hour,minute)
