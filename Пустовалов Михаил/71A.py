s=input()
str_c=list(s)
n=len(s)
if(n>10):
    print(str_c[0]+str_c[1]+str_c[n-2]+str_c[n-1])
else:
    print(s)