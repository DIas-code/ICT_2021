def dtb(num,result):
    if num>=1:
        a=num%2
        r=str(a)
        result+=r
        dtb(num//2,result)
    else: print(result)

num=int(input("Decimal num: " ))
result=""
dtb(num,result)