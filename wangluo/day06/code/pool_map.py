from multiprocessing import Pool
import time

def fun(n):
    time.sleep(1)
    s="%s,LOL"%n
    return  s
pool=Pool()
r=pool.map(fun,['李相赫','简自豪','厂长','MLXG','Ming'])
pool.close()
pool.join()
for x in r:
    print(x)