words=input()
words=words.replace(" ","")
words=words.lower()
flag=0
for i in range(0,int(len(words)/2)):
    if words[i]==words[-i-1]:
        continue
    else: 
        flag+=1
        break
if flag==0:
    print("Palindrome")
else:
    print("NoPolindrome")