import random
a=0
up=0
mx=0
for i in range(100):
    a=random.randint(1,100)
    if a>mx:
        mx=a
        print(a,"<== Update")
        up+=1
    else:print(a)
print("The maximum value found was: ",mx)
print("The maximum value was updated: ", up," times")