n=int(input())
cnt=0
for i in range (0,n):
    RP=input()
    if RP=="Tetrahedron":
        cnt+=4
    elif RP=="Cube":
        cnt+=6
    elif RP=="Octahedron":
        cnt+=8
    elif RP=="Dodecahedron":
        cnt+=12
    elif RP=="Icosahedron":
        cnt+=20

print(cnt)