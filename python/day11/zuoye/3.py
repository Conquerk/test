l=[[3,5,8],10,[[13,14],15,18],20]
def lis(n):
    for x in n :
        if type(x) is list:
            lis(x)
        else:
            print(x)
lis(l)
def li(n):
    s=0
    for x in n:
        if type(x) is int :
            s+=x
        if type(x) is list :
            s+=li(x)
    return  s 
print(li(l))
