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
    a=float(input())
    d=input()
    b=float(input())
    if d=="/":
        c=cas(a,b)
    elif d=="*":
        c=pro(a,b)
    elif d=="+":
        c=summ(a,b)
    elif d=="-":
        c=raz(a,b)
    else:
        c="некоректный ввод"
    print(f"результат={c}")