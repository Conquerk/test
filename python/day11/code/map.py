#pow(x,y,z=none)   1**4 2**3,3**2,4**1
for x in map(pow,range(1,5),range(4,0,-1)):
    print(x)


def pow2(x):
    return(x**2)
for x in map(pow2,range(1,10)):
    print(x)