Values=list(map(int,input("Integers: ").split()))
mn=min(Values)
mx=max(Values)
mdl=Values[1]+Values[0]+Values[2]-mn-mx
print("Sorted values:",mn,mdl,mx)