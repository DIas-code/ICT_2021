import math
x1=int(input("x pos: "))
y1=int(input("y pos: "))
def ispointinsquare(x1,y1):
   print("A point is not in square")
if x1>1 or x1<-1 or y1<-1 or y1>1:
    ispointinsquare(x1,y1)
else: 
    print("A point is in square")
