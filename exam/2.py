lis=list(map(int,input().split()))

n=lis[0]
m=lis[1]
a=lis[2]
rls=n/a
if rls>int(rls):
    rls=int(rls)+1
else: rls=int(rls)
uds=m/a
if uds>int(uds):
    uds=int(uds)+1
else: uds=int(uds)
print(rls*uds)