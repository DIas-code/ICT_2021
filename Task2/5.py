pos=input("Enter position: ")
posw=pos[0]
posn=int(pos[1])
posw=ord(pos[0])-97+49
posw=int(chr(posw))
if (posw%2==0 and posn%2==0) or (posw%2==1 and posn%2==1):
    print("Black square")
else:
    print("White square")