n=int(input())
for i in  range(n) :
    inv=dict()
    num=int(input())
    for j in range(num) :
        item=input().split()
        name=item[0]
        quantity=int(item[1])
        inv.setdefault(name,quantity)
    changes=int(input())
    for j in range(changes) :
        query=input().split()
        name=query[1]
        quantity=int(query[2])
        change=query[0]
        if change=="ADD" :
            if name in inv :
                inv[name]+=quantity
            else :
                inv[name]=quantity
            print("ADDED"+" "+name)
        if change=="DELETE" :
            if name in inv :
                if quantity>(inv[name]) :
                    print("Item"+" "+name+" could not be DELETED")
    total=str(sum(inv.values()))
    print("Total Items in Inventory:"+total)
