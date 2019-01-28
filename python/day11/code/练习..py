#求： 1**2+2**2+3**2++………9**2的和
# def x(x):
#     return x **2
# s=0
# for x in map(x,range (1,10)):
#     s+=x
# print(s)
#方法2
# m=map(x,range(1,10))
# print(sum(m))
#求： 1**3+2**3+3**3++………9**3的和
print(sum(map(lambda x:x**3,range(1,10))))
#求： 1**9+2**8+3**7++………9**1的和
print((sum(map(pow,range(1,10),range(9,0,-1)))))
