n=int(input())
sum=0
elements=0
c=0
while n>=c:
    c+=1
    if c%7==0:
        sum+=c
        elements+=1
print("Average is: ", sum/elements)