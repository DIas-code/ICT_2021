P=int(input("pressure: "))
V=int(input("volume: "))
T=float(input("temperature: "))+273.15
R=8.314
n=(P*V)/(R*T)
print("amount of moles is: ",n)