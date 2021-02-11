import math
s1=int(input("1 length: "))
s2=int(input("2 length: "))
s3=int(input("3 length: "))
s=(s1+s2+s3)/2
A=(s*(s-s1)*(s-s2)*(s-s3))
print("Area pf triangle: ",math.sqrt(A) )