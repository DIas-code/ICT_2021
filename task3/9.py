binary=(input("Binary number: "))
num=0
for i in range (0,len(binary)):
    if binary[i]=="1":
        num+=2**i
print("Decimal: ", num)