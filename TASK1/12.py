import math
t1=int(input("1 latitude: "))*math.pi/180
g1=int(input("1 longtitude: "))*math.pi/180
t2=int(input("2 latitude: "))*math.pi/180
g2=int(input("2 longtitude: "))*math.pi/180

dist=6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
print("Distance between point eqaul: ",dist)