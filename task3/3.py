n=15
pi=3
i=0
c=2
nextpi=0
while i<n:
    nextpi=4/(c*(c+1)*(c+2))
    c+=2
    if i%2==0:
        pi+=nextpi
    else: pi-=nextpi
    i+=1
print(pi)