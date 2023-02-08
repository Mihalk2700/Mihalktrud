from itertools import product
for i in range(2,6):
    b=product('12',repeat=i)
    for n in b:
        a=12
        for x in n:
            if x=='1':
                a-=1
            else :
                a*=7
        if a==489:
            print(n)
        
