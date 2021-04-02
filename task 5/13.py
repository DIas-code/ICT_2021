s=set([])
n=int(input())
for i in range(0,n):
    a=input()
    s.add(a)
s=frozenset(s)
try:
    s.add('a')
except:
    print(type(s))