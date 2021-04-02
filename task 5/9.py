s=set([])
s1=set([])
n=int(input())
for i in range(0,n):
    a=input()
    s.add(a)
m=int(input())
for i in range(0,m):
    a=input()
    s1.add(a)
s2=s.symmetric_difference(s1)
print(s2)