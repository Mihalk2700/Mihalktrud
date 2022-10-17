from this import d

sn=39
sd=39*2
for i in range(1,1000):
    s=sn+sd+4*i
    for k in range(1,1000):
        if s%k==0:
           break
        
