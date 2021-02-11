n=int(input())
dep=0.00
for x in range(0, n):
    x=float(input())
    if x>=1:
        dep+=0.25
    else:
        dep+=0.10
print("$","%.2f"%dep)