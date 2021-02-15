red=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black=[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
green="0"
green2="00"
number=input("The spin resulted in ")
if number==green2:
    print("Pay 00")
elif  number==green:
    print("Pay 0")
elif number !="00" and number!="0":
    for i in range(0,len(red)):
        if int(number)==red[i]:
            print("Pay",number)
            print("Pay Red")
            if int(number)%2==0:
                print("Pay Even")
            else: print("Pay Odd")
            if int(number)>18:
                print("Pay 19 to 36")
            else: print("Pay 1 to 18")
    for i in range(0,len(red)):       
        if int(number)==black[i]:
            print("Pay",number)
            print("Pay Black")
            if int(number)%2==0:
                print("Pay Even")
            else: print("Pay Odd")
            if int(number)>18:
                print("Pay 19 to 36")
            else: print("Pay 1 to 18")