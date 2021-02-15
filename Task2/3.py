month=input()
day=int(input())
print("Date:",month,day)
if month=="January" and day==1:
    print("New year's day")
elif month=="July" and day==1:
    print("Canada day")
elif month=="December" and day==25:
    print("Christmas day")
else: print("There is not fixed-date holiday")
    