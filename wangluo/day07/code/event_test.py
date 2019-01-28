from threading import Event

#创建事件对象
e=Event()

e.set()#设置e   设置之后不阻塞

e.wait()#此时阻塞

e.clear()
print(e.is_set())

print("*******")

