n=int(input())
hnl=''
for i in range(0,n):
    
    if i+1==n and i%2==0:
        hnl+=" I hate it"
        break
    elif i+1==n and i%2==1:
        hnl+=" I love it"
        break
    if  i%2==0:
        hnl+=" I hate that"
    elif i%2==1:
        hnl+=" I love that"
print(hnl[1:])