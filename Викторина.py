def prov(c):
    n=c.index(0)
    return n
def main():
    a=['Верно ли, что если концы отрезка лежат в данной плоскости, то и его середина лежит в этой плоскости:\n','Могут ли две плоскости иметь общую точку, но не иметь общей прямой:\n','Верно ли, что если три точки лежат в данной плоскости то они не лежат на одной прямой:\n','Могут ли три прямые иметь общую точку, но не иметь общей плоскости:\n',]
    b=['Да','Нет','Нет', 'Да']
    c=[0,0,0,0]
    nk=0
    while 0 in c:
        o=input(a[prov(c)])
        if o==b[prov(c)]:
            print('ВЕРНО')
            c[prov(c)]=1
        else:
            print('ПОЗОР')
            c[prov(c)]=0
            nk+=1
    print(f'Вай, ты маладэц на {4-nk}')
    print(f'Ты позорник на {nk}')
    if nk==0:
        print('Ольга Больга довольна')
d=1
while d==1:
    main()
    d=int(input('Продолжим?'))
