def gcd(n, m):
    if n>m:
        d=m
    else: d=n
    while d!=0:
        if m%d==0 and n%d==0:
            return d
        d-=1
n=int(input("Enter numerator: "))
m=int(input("Enter denominator: "))
print( "The lowest fraction of numerator and denominator are ",n//gcd(n,m),"and", m//gcd(n,m),", respectively")