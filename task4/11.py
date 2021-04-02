import random
n=int(input())
cnt=0
l=[]
for i in range(0,n):
    a=random.randint(0,1)
    l.append(a)
for i in l:
    if i==1:
        cnt+=1
print(l)
print("Cnt of 1: ",cnt)
        
