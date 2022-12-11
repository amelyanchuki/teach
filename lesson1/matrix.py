def summ_ij():
    a = input()
    b = []
    c = []
    while a != "end":
        for i in a.split():
            c.append(int(i))
        b.append(c)
        c = []
        a = input()
    c = [[0 for j in range(len(b[0]))] for i in range(len(b))]

    for i in range(len(b)):
        for j in range(len(b[i])):
            c[i][j] = b[i - 1][j] + b[(i + 1) % len(b)][j] + b[i][j - 1] + b[i][(j + 1) % len(b[i])]
            print(c[i][j], end=' ')
        print()
        