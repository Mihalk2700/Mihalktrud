def summ(a,b):
    c=a+b
    return c
def raz(a,b):
    c=a-b
    return c
def pro(a,b):
    c=a*b
    return c
def cas(a,b):
    c=a/b
    return c
x=True
while x==True:
    s=input()
    str_c=s.split()
    if str_c[1]=="/" and str_c[2]!=0:
        print(cas(float(str_c[0]),float(str_c[2])))
    elif str_c[1]=="*":
        print(pro(float(str_c[0]),float(str_c[2])))
    elif str_c[1]=="+":
        print(summ(float(str_c[0]),float(str_c[2])))
    elif str_c[1]=="-":
        print(raz(float(str_c[0]),float(str_c[2])))
    else:
        print("некоректный ввод")