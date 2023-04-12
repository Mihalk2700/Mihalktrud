with open ('27_A.txt') as f:
    n=[x for x in f]
    n.pop(0)
    sp=[]
    k=[]
    ind=[]
    for i in n:
        sp.append(list(map(int,i.split())))
    for i in range(len(sp)):
        k.append((sp[i][1]-1)//36+1)
    for i in range(len(sp)):
        ind.append(sp[i][0])
    sp=list(zip(ind,k))
    print(sp)
