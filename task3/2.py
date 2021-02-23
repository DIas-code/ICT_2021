import math
firstx=float(input("Enter the x part ofthe coordinate: "))
firsty=float(input("Enter the x part ofthe coordinate: "))
x = input("Enter the x part ofthe coordinate: (blank to quit): ")
prevx=firstx
prevy=firsty
perimeter=0
dist=0
while x!= "":
    y=float(input("Enter the y part of the coordinate: "))
    nextx=float(x)
    nexty=y
    dist=math.sqrt((prevx-nextx)**2+(prevy-nexty)**2)
    prevx,prevy=nextx,nexty
    perimeter+=dist
    print(perimeter)
    x = input("Enter the x part of the coordinate: (blank to quit): ")
dist = math.sqrt((nextx-firstx)**2 + (nexty-firsty)**2)
perimeter += dist
print("The erimeter of that polygon is ",perimeter)