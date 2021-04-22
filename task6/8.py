word1={

}
a=input()
for i in range(len(a)):
    word1[str(i)]=a[i]
b=input()
if len(a)!=len(b):
    print("They are not anagrams")
    exit()
cnt=0

for j in range(len(b)):
    for x,y in word1.items():
        if b[j]==y:
            cnt+=1
            del word1[x]
            break
if cnt == len(b):
    print("They are anagrams")   
else:     print("They are not anagrams")