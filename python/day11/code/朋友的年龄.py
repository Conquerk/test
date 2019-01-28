def getage(n):
    if n==1:
        return 10
    return getage(n-1)+2
print(getage(6))