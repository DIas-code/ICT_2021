Price=3.49
Prwithdis=Price*60/100
Amount=int(input("Amount of bread: "))
print("Regular price: %.2f"% Price)
print("Discounted price: %.2f"% Prwithdis)
print("Taotal price: %.2f"%(Amount*Prwithdis) )