def primes_m2n(m,n):
    l=[]
    for x in range(m,n):
        isprime=True
        if x < 2 :
            isprime=False
        else:
            for i in range(2,x):
                if x % i ==0: 
                    isprime=False
                    break
        if isprime:
            l.append(x) 
    print(l)      
primes_m2n(3,50)
primes_m2n(1,100)  
     


        

         
