for a in range(1,100):
    flag=True
    for x in range(1,1000):
        if (((x%2==0)<= (not(x%3==0)))or(x+a>=100))==1:
            flag=True
        else:
            flag=False
            break
    if flag==True:
        print(a)
        break