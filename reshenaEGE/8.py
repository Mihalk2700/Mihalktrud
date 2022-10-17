x=0
for i in range(1,8):    
    for k in range(8):
        for a in range(8):
            for b in range(8):
                for c in range(8):
                    s=str(i)+str(k)+str(a)+str(b)+str(c)
                    d=list(s)
                    if d.count('6')==1 and d.index('6')==len(d)-1 and int(d[d.index('6')-1])%2==0:
                        print(d)
                        x+=1
                    if d.count('6')==1 and d.index('6')==1 and int(d[d.index('6')+1])%2==0:
                        x+=1
                        print(d)
                    if d.count('6')==1 and d.index('6')<len(d)-1 and int(d[d.index('6')-1])%2==0 and int(d[d.index('6')+1])%2==0:
                        x+=1
                        print(d)                   
print(x)
                    
