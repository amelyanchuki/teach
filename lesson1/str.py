def gc():
    a = input()#acggtgttat
    b = 0
    c = 0

    for i in a.lower():
        b += 1
        if i == "g":
            c += 1
        elif i == "c":
            c += 1

    print(c / b * 100)

def dnk(): 
    a = input()#aaaabbcaa
    c = a[0]
    g = 0

    for i in a:
        if c == i:
            g += 1
        elif c != i:
            print(c, end="")
            print(g, end="") 
            g = 1
            c = c.replace(a[0], i)
            c = c.replace(c[0], i)
    print(c, end="")
    print(g, end="")

