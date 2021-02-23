myfile = open('input.txt', 'r', encoding = 'utf-8')

arrayWord = dict()

for i in myfile.read().split():
    if i in arrayWord:
        arrayWord[i] +=1
    else :
        arrayWord[i] = 1
    
myfile.close()

arrayWord = sorted(((-value,key) for key, value in arrayWord.items()))
for i in arrayWord:
    for j in i:
        print(i[1])
        break
print (arrayWord)

print(*(_[1] for _ in arrayWord))

