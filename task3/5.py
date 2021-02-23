import math
def is_prime(n):
    while n%2==0:
        print(2)
        n/=2
    i=3
    while i*i<=n:
        if n%i==0:
            print(i)
            n/=i
        else:i+=2
    if n>2:
        print(int(n))

n=int(input("Enter an integer(2 or greater): "))
print("The prime factors of ",n , " are")
is_prime(n)