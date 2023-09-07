n=int(input())
for i in range(n) :
    num=int(input())
    max=0
    for j in range(num) :
        marks=input()
        t=(marks.split())
        name=t[0]
        score=float(t[1])
        if(max<score) :
            max=score
            topper=name
    print(topper)