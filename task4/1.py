import math
def hyp(a,b):
    c=math.sqrt(a**2+b**2)
    return c
a=int(input("First side: "))
b=int(input("Second side: "))
print("The length of hypotenuse is ",end='')
print(hyp(a,b))