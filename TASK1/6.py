meal=float(input("Cost of meal: "))
tax=meal*0.08
tip=meal*0.18
tot=meal+tax+tip
print("Tax amount: ","%.2f"%tax)
print("Tip amount: ","%.2f"%tip)
print("Total amount: ","%.2f"%tot)