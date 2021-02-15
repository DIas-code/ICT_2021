import math
Frequency=int(input("Frequency range(Hz): "))
if Frequency<3*pow(10,9):
    print("Radio waves")
elif Frequency<3*pow(10,12):
    print("Microwaves")
elif Frequency<4.3*pow(10,14):
    print("Infared light")
elif Frequency<7.5*pow(10,14):
    print("Visible light")
elif Frequency<3*pow(10,17):
    print("Ultraviolet light")
elif Frequency<3*pow(10,19):
    print("X-rays")
elif Frequency>=3*pow(10,19):
    print("Gamma rays")    