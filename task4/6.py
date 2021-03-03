import random
def lp():
    a=random.randint(1,2)
    print(a)
    LP=""
    if a==1:
        for i in range (0,6):
            if i <3:
                L=random.randint(65,90)
                LP+=chr(L)
            else:
                LP+=str(random.randint(0,9))
    elif a==2:
        for i in range (0,7):
            if i >3:
                L=random.randint(65,90)
                LP+=chr(L)
            else:
                LP+=str(random.randint(0,9))
    return LP

print("Randomly generated license plate is",lp())