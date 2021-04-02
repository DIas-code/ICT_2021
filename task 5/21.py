s=set(map(str,input().split()))
s1=set(map(str,input().split()))
s.difference_update(s1)
print(s)
