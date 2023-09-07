n=int(input())
for i in range(n) :
    t=input()
    b=t.split()
    a=int(b[0])
    d=int(b[1])
    n=int(b[2])
    ap=list()
    for i in range(1,n) :
        term=a+(i-1)*d
        ap.append(term)
    squaredap=list()
    for i in ap :
        squaredap.append(i*i)
    print(*ap,sep=' ')
    print(*squaredap,sep=' ')
    print(sum(squaredap))
