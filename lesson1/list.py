a = ["asasdd", [1, 2, "assa"], 155423, "ssa"]
b = []

for i in a:
    if len(i) <= 3:
        b.append(i)
        a.remove(i)
    else:
        ...

    
print(a)
print(b)

