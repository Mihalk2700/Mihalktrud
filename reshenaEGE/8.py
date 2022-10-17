x=0
for i in range(1,8):    
    for k in range(8):
        for a in range(8):
            for b in range(8):
                for c in range(8):
                    s=str(i)+str(k)+str(a)+str(b)+str(c)
                    d=list(s)
                    if d.count('6')==1:
                        if int(d[d.index('6')-2])%2==0 and int(d[d.index('6')])%2==0:
                            x+=1
print(x)
