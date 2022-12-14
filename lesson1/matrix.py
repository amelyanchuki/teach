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

def snake():
    a = int(input())
    b = 1
    c = [[0 for j in range(a)] for i in range(a)]
    d = 0

    while b != a*a +1:
        for i in range(a):
            for j in range(a):
                if i == 0 + d and j <= len(c):
                    if c[i][j] == 0:
                        c[i][j] = b
                        b += 1

        for i in range(a):
            for j in range(a):         
                if i <= len(c) and j == len(c) -1 -d:
                    if c[i][j] == 0:
                        c[i][j] = b
                        b += 1

        for i in range(a):
            for j in range(a-1, -1, -1):
                if i == len(c) - 1 - d and j <= len(c):
                    if c[i][j] == 0:
                        c[i][j] = b
                        b += 1
                        
        for i in range(a-1, -1, -1):
            for j in range(a):
                if i <= len(c) and j == 0 + d:
                    if c[i][j] == 0:
                        c[i][j] = b
                        b += 1
        d += 1
    for snake in c:
        print(snake)


