def hex2int(hexa):
    if (hexa>="A" and hexa<="F") or (hexa>="a" and hexa<='f'):
        hexa=hexa.upper()
        return ord(hexa)-ord('A')+10
    elif int(hexa)>=0 and int(hexa)<=9:
        return hexa
    return "Error message"
def int2hex(dec):
    if dec>="10" and dec<="15":
        return chr(ord('A')+int(dec)-10)
    elif int(dec)>=0 and int(dec)<=9:
        return dec
    return "Error message"
hexa=input("Enter hexadecimal digit: ")
dec=input("Enter decimal digit: ")
er=hex2int(hexa)
if er=="Error message":
    print(hex2int(hexa))
else: print("Decimal digit is",hex2int(hexa))
er2=int2hex(dec)
if er2=="Error message":
    print(int2hex(dec))
else: print("Hexadecimal digit is",int2hex(dec))