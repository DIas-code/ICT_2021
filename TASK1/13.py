cash=int(input("Cash: "))
p=0
n=0
d=0
q=0
l=0
t=0
while cash!=0:
    if cash-200>=0:
        cash-=200
        t+=1
    elif cash-100>=0:
        cash-=100
        l+=1
    elif cash-25>=0:
        cash-=25
        q+=1
    elif cash-10>=0:
        cash-=10
        d+=1
    elif cash-5>=0:
        cash-=5
        n+=1
    elif cash-1>=0:
        cash-=1
        p+=1
print("toonies: ",t)
print("loonies: ",l)
print("quarters: ",q)
print("dimes: ",d)
print("nickels: ",n)
print("pennies: ",p)