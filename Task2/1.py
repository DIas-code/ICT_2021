rate=float(input("Rating of employees: "))
if rate==0.0:
    print("Unacceptable pefomance")
    print("Employees' amount raises for: ", 0.0)
elif rate==0.4:
    print("Acceptable pefomance")
    print("Employees' amount raises for: ", 2400*0.4)
elif rate>=0.6:
    print("Meritorious pefomance")
    print("Employees' amount raises for: ", 2400*rate)
else:
    print("Error rate")