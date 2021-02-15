import math
constantA=int(input())
constantB=int(input())
constantC=int(input())
b=constantB**2
ac4=4*constantA*constantC
D=b-ac4
if D<0:
    print("No real roots")
else:
    Discriminant=math.sqrt(b-ac4)
    if Discriminant==0:
        print("1 real root")
    else:
        print("2 real roots")