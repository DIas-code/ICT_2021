def median(a,b,c):
    med=a+b+c-max(a,b,c)-min(a,b,c)
    return med
a=float(input("First value: "))
b=float(input("Second value: "))
c=float(input("Third value: "))
print("Median of three values is ",median(a,b,c))