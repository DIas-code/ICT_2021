x=int(input())
y=int(input())
k=int(input())
c=int(input())
a=x-k
b=y-c
if k<c and k<b and k<a :
    print(k)
elif c<k and c<b and c<a :
    print(c)
elif a<b :
    print(a)
else :
    print(b)