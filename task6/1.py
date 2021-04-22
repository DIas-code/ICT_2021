import random
def reverseLookup(myDict,a):
    lis=[]
    for x,y in myDict.items():
        if y == a:
            lis.append(x)
    return lis
def main():
    myDict={
        "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 2, "K": 5, "L": 1,
        "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8,
        "Y": 4, "Z": 10
    }
    value=random.randint(1, 10)
    lis=reverseLookup(myDict, value)
    print(lis)
    print(value)
main()