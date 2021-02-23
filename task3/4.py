n=int(input())
m=int(input())
d=0
if n>m:
    d=m
else: d=n
while d!=0:
    if m%d==0 and n%d==0:
        print(d)
        break
    d-=1