import random
lia=[' 2.78',' 5.56',' 8.33','11.11','13.89','16.66','13.89','11.11',' 8.33',' 5.56',' 2.78']
myDic={
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
    '10': 0,
    '11': 0,
    '12': 0
}

b=1
n=1000
def rols(n,b):
    for i in range(1000):
        a=random.randint(1, 6)
        d=random.randint(1, 6)
        if a+d==2:
            myDic['2']+=1
        elif a+d==3:
            myDic['3']+=1
        elif a+d==4:
            myDic['4']+=1
        elif a+d==5:
            myDic['5']+=1
        elif a+d==6:
            myDic['6']+=1
        elif a+d==7:
            myDic['7']+=1
        elif a+d==8:
            myDic['8']+=1
        elif a+d==9:
            myDic['9']+=1
        elif a+d==10:
            myDic['10']+=1
        elif a+d==11:
            myDic['11']+=1
        elif a+d==12:
            myDic['12']+=1
sx=''
sy=''
rols(n,b)
print("Total        Simulated         Expected")
print("               Percent          Percent")
i=0
for x,y in myDic.items():

    if int(x)<10:
        sx=' '+x
    else: sx=x
    if y/10<10:
        sy=' '+str(y/10)+'0'
    else: sy = str(y/10)+'0'
    print("  ",sx,"          ",sy,"          ",lia[i])
    i+=1
