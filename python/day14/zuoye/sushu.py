def isprime(x):
    if x < 2 :
        return False
    else:
        for y in range(2,x):
            if x % y==0:
                return False
        else:
            return True
