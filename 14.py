for x in range(15):
    a='123'+str(x)+'5'
    b='1'+str(x)+'233'
    if (int(a,15)+int(b,15))%14==0:
        print((int(a,15)+int(b,15))/14)
