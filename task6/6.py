import random
digits = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
afterdigits = {"ten" : "10", "eleven" : "11", "twelve" : "12", "thirteen" : "13", "fourteen" : "14", "fifteen" : "15", "sixteen" : "16", "seventeen" : "17", "eighteen" : "18", "nineteen" : "19"}
tens = {"twenty" : "2", "thirty" : "3", "fourty" : "4", "fifty" : "5", "sixty" : "6", "seventy" : "7", "eighty" : "8", "ninety" : "9"}
num = random.randint(0,999)
print(num)
convert=''
if num == 0:
    print('zero')
    exit()
while num>0:
    while num>99:
        for x,y in digits.items():
            if int(y) ==int(num/100):
                convert+=x + ' hundred '
                num%=100
                break
    while num>=20:
        for x,y in tens.items():
            if int(y) ==int(num/10):
                convert+=x+" " 
                num%=10
                break
    if num>=10 and num<=19:
        for x, y in afterdigits.items():
            if int(y) == num:
                convert+=x
                print(convert)
                exit()

    for x, y in digits.items():
        if int(y)==num:
            convert += x
            num%=1

print(convert)