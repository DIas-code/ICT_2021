s=int(input("Length of side: "))
n=int(input("Number of sides: "))
import math
print("Area of regular polygon: ", (n*s**2)/(4*math.tan(math.pi/n)))