word1={

}
a=input()
a=a.lower()
for i in range(len(a)):
    if a[i]>='a' and a[i]<='z':
        word1[str(i)]=a[i]
cntofic=len(word1)
b=input()
b=b.lower()
cnt=0

for j in range(len(b)):
    for x,y in word1.items():
        if b[j]==y:
            cnt+=1
            del word1[x]
            break
if cnt == cntofic:
    print("They are anagrams")   
else:     print("They are not anagrams")