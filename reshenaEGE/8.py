for i in range(7):
    d=[]
    d.append(i)
    for k in range(7):
        d.append(k)    
        for a in range(7):
            d.append(a)
            for b in range(7):
                d.append(b)
                for c in range(7):
                    d.append(c)
                    if i=6 or k=6 or a=6 or b=6 or c=6:
                        n=d.index(6)
                        print(n)
                        break
