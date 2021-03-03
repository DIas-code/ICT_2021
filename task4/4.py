def isTriangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False
a=float(input())
b=float(input())
c=float(input())
print("Is it valid triange?",isTriangle(a,b,c))