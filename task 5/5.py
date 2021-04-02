s=set([])
n=int(input())
for i in range(0,n):
    a=input()
    s.add(a)
a=input()
s.discard(a)
print(s)