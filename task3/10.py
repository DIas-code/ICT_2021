import random
a=random.randint(1,100)
print(a)
up=0
mx=a
for i in range(99):
    a=random.randint(1,100)
    if a>mx:
        mx=a
        print(a,"<== Update")
        up+=1
    else:print(a)
print("The maximum value found was: ",mx)
print("The maximum value was updated: ", up," times")