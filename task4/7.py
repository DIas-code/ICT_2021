import random
def Gp(a):
    
    GP=""
    for _ in range (0,a):
        L=random.randint(33,126)
        GP+=chr(L)
    islow=False
    isup=False
    isnum=False
    for i in GP:
        if i>="a" and i<="z":
            islow=True
        elif i>="A" and i<="Z":
            isup=True
        elif i>="0" and i<="9":
            isnum=True
    if isnum==True and islow==True and isup==True:
        return GP
    else:
        return Gp(a)
a=random.randint(8,20)
print(a)
print("Random good password",Gp(a))