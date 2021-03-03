def isprime(n):
    x=True
    i=2
    while i*i<=n:
        if n%i==0:
            x=False
        i+=1
    if x==True:
        return "it is prime number"
    else:
        return "it is not prime number"
n=int(input())
print(isprime(n))