with open('17.txt') as f:
    nums=[int(x)for x in f]
    c=list(map(abs,nums))
    count=0
    sp=[]
    for i in range(len(nums)-1):
        if abs(nums[i])%10==3:
            sp.append(nums[i])
    maxi=max(sp)**2
    sqrt=[]
    for i in range(len(c)-1):
        if ((c[i]%10==3 and c[i+1]%10!=3 ) or (c[i]%10!=3 and c[i+1]%10==3)) and (c[i]**2+c[i+1]**2)>=maxi:
            count+=1
            sqrt.append(c[i]**2+c[i+1]**2)
    print(count)
    print(max(sqrt))
