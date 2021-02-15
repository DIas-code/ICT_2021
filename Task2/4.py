mag=float(input("Earthquake magnitude: "))
if mag<2:
    print("Micro earthquake")
elif mag<3:
    print("Very minor earthquake")
elif mag<4:
    print("Minor earthquake")
elif mag<5:
    print("Light earthquake")
elif mag<6:
    print("Moderate earthquake")
elif mag<7:
    print("Strong earthquake")
elif mag<8:
    print("Major earthquake")
elif mag<10:
    print("Great earthquake")
elif mag>=10:
    print("Meteoric earthquake")    