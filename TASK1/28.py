Ta=float(input("Air temperatue in C: "))
V=float(input("Speed of winf in km/h: "))
WCI=13.12+0.6125*Ta-11.37*V**0.16+0.3965*Ta*V**0.16
print("WCI is: ",WCI)