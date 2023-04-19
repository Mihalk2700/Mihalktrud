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
    costs=[]
    for i in sp:
        pos=i[0]
        cost=0
        for x in sp:
            cost=cost+abs(pos-x[0])*x[1]
        costs.append(cost)
    print(min(costs))
with open ('27_B.txt') as f: #короче тут открываем файл
    n=[x for x in f] # записываем строки
    n.pop(0) #убираме первую строку
    sp=[]
    k=[]
    ind=[]
    for i in n:
        sp.append(list(map(int,i.split()))) # переводим значения в списке в числа
    for i in range(len(sp)):
        k.append((sp[i][1]-1)//36+1) # находим кол-во контейнеров
    for i in range(len(sp)):
        ind.append(sp[i][0])#сохраняем километраж пунктов 
    sp=list(zip(ind,k))#соединяем километраж и кол-во контейнеров
    costs=[]
    for i in range(549715,549735,1):# в этом цикле мы выводим значения приближаясь к минимальному
        pos=sp[i][0]
        cost=0
        for x in sp:
            cost=cost+abs(pos-x[0])*x[1]#вычисляем стоимость в этот пункт
        costs.append(cost)
        print(i,sp[i][0],cost)
#5634689219329
