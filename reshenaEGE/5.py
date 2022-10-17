for i in range(1,100):
    n=(bin(i)[2:])
    if num.count('1')%2==0:
        c='10'+n[2:]+'0'

    if num.count('1')%2!=0:
        c='11'+n[2:]+'1'
    if int(c,2)>40:
        print (i, int(c,2))
        break
