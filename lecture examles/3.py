n = int(input("Input n : "))
average = 0
for i in range (0 , n) :
    if(i % 7 == 0):
        average = (average + i) / n
print(average)