def is_magic_date(d,m,y):
    if d*m==y%100:
        return True
    else: return False


days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
for year in range (1900,2000):
    for month in range (1,13):
        if year%4==0:
            days[2]=29
        else:
            days[2]=28
        for day in range(1,days[month]+1):
            if is_magic_date(day,month,year)==True:

                print("%02d:%02d:{} is magic date".format(year)%(day,month))

