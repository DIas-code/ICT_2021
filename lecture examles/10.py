a=input()
b=[i for i in a]
cnt=1
while len(b)!=0:
    j=1
    while j<len(b):
        if b[0]==b[j]:
            cnt+=1
            b.remove(b[j])
        j+=1
    print(b[0], " : " ,cnt)
    cnt=1
    b.remove(b[0])
