# import sushu
# def zhiyinshu(x,l=[]):
#     if sushu.isprime(x):
#         l.append(x)
#         print(l)
#         return l
#     else:
#         for a in range(2,x):
#             if x % a ==0:
#                 x=x//a
#                 l.append(a)
#                 return zhiyinshu(x,l)        
# zhiyinshu(30)
# zhiyinshu(126)



def get_zhiyin_list(x):
    """此函数将返回包含ｘ的所有质因数列表"""
    l=[]
    #循环查找质因数，如果找到质因数就加入到ｌ中
    #到ｘ＝1为止
    while x >1:
        for i in range (2,x+1):
            if x % i==0:
                l.append(i)
                x=int(x/i)
                break
    return l 
print(get_zhiyin_list(90))
