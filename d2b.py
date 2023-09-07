def dtb(n) :
    return bin(n).replace("0b", "")
n=int(input())
for i in range(n):
    a=int(input())
    print(dtb(a))