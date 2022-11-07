def prost(s):
    for k in range(2,1000):
        if s%k==0 and s!=k :
            return(0)
            break
        elif s%k==0 and s==k:
            return(s)
            break 
sn=39
sd=39*2
for i in range(1,1000):
    s=sn+sd+4*i
    if prost(s)!=0:
        print(i)
        break
