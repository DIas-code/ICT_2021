import math
x1=int(input("x pos: "))
y1=int(input("y pos: "))
def ispointinsquare(x1,y1):
   return abs(x1)+abs(y1)
if ispointinsquare(x1,y1)<=1:
    print("A point is in square")
else: 
    print("A point is not in square")
