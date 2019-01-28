sn=0.0
fenmu=1
i=0
sign=1  # 代表+　　-　　　号　
while i<10000000 :
    r=sign*1/fenmu
    sn+=r  #累加操作
    sign*=-1
    fenmu+=2
    i+=1
print(sn)
print(sn*4)