sec=int(input("Seconds: "))
d=int(sec/86400)
if sec>=86400:
    sec=sec-d*86400
print(sec)
h=int(sec/3600)
if sec>=3600:
    sec=sec-h*3600
m=int(sec/60)
if sec>=60:
    sec=sec-m*60
print(d,":","%.2u"%h,":","%.2u"%m,":","%.2u"%sec)
