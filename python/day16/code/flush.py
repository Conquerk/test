f=open("myflush.txt","w")
f.write("aaaaaaaaaaa")
f.flush()#强制清空缓存区
while True:
    pass
f.close()
