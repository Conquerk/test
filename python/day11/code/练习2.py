def sushu(x):
    if x <2:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

even=[x for x in filter(sushu,range(100))]
print(even)