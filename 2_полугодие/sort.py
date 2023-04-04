def pusyr(sp,l):
    a=True
    while a:
        for i in range(l-1):
            if sp[i]>=sp[i+1]:
                sp[i],sp[i+1]=sp[i+1],sp[i]
        if all(sp[i]<=sp[i+1] for i in range(l-1)):
            a=False
    return sp
def dih(sp,l):
    while l>2:
        l=l//2
        if (sp[l]>=sp[l-1]):
            sp=sp[:l]
            print(sp)
        else:
            sp=sp[l:]
            print(sp)
    return min(sp)
sp=[20,18,13,11,0,9,10,12,15]
l=len(sp)-1
print(dih(sp,l))
