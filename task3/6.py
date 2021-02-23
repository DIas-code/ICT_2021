for i in range(0,11):
    for j in range(0,11):
        if i ==0 and j ==0:
            print("    ", end='')
        elif i==0 or j==0:
            print('%4d' % (i+j), end='')
        else: print('%4d' % (i*j), end='')
    print("")