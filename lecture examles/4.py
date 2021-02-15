import math
x1=int(input("First x pos: "))
y1=int(input("First y pos: "))
x2=int(input("Second x pos: "))
y2=int(input("Second y pos: "))
def f(x1,y1,x2,y2):
    d1=(x2-x1)
    d2=(y2-y1)
    print("Distance:",math.sqrt(d1**2+d2**2))
f(x1,y1,x2,y2)