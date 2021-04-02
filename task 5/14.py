s=set(map(int,input().split()))

mx=-12481803751903260294680246
mn=123512956912756928569124569
for i in s:
    if mx<i:
        mx=i
    if mn>i:
        mn=i

print("max:",mx, "min:",mn)