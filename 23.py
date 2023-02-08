from itertools import product
def f(d,y,z):
    c=0
    for i in range(1,z):
        b=product('12',repeat=i)
        for n in b:
            a=d
            if a==10 and n.count('2')>1:continue
            for x in n:
                if x=='1':a+=1
                else:a*=2
                if a==17:break
            if a==y:c+=1
    return c
a=f(1,10,10)
b=f(10,35,24)
print(a)
print(b)
print(a*b)
