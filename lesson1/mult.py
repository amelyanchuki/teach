a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(end="  ")
for i in range(a, b+1):
    if i == a:
        for g in range(c, d+1):
            if g == d:
                print(g)
            else:
                print(g, end=" ")
    print(i, end=" ")
    for s in range(c, d+1):
        if s == d:
            print(s * i)
        else:
            print(s * i, end=" ")
