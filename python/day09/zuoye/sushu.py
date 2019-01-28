def isprime(x):
    if x < 2 :
        print(False)
    else:
        for y in range(2,x):
            if x % y==0:
                print(False)
                break
        else:
            print(True)
isprime(55)
isprime(9)
isprime(47)
isprime(1)
isprime(2)