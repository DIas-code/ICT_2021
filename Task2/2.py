year=int(input())
m=month=int(input())
d=day=int(input())
print("Date is: ",year,"-","%.2u"%month,"-","%.2u"%day)
if year%4==0 and m==2 and d==29:
    print("Next days date is: ", year,"- 03 - 01")
elif year%4==0 and m==2 and d==28:
    print("Next days date is: ", year,"- 02 - 29")    
elif year%4!=0 and m==2 and d==27:
    print("Next days date is: ", year,"- 02 - 28")
elif m==2 and d==28:
    print("Next days date is: ", year,"- 03 - 01")
elif (m==1 or m==3 or m==5 or m==7 or m==8 or m==10) and d==31:
    m+=1
    print("Next days date is:", year,"-","%.2u"%m,"- 01")
elif (m==2 or m==4 or m==6 or m==9 or m==11) and d==30:
    m+=1
    print("Next days date is:", year,"-","%.2u"%m,"- 01")
elif m==12 and d==31:
    print("Next days date is:", year+1,"- 01","- 01")
else:
    d+=1
    print("Next days date is:", year,"-","%.2u"%m,"-","%.2u"%d)