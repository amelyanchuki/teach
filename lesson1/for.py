def check():
    aa = "qwertyuiopasdfghjklzxcvbnm"
    bb = input("writ text \t")
    string = " "
    for i in aa:
        if i not in bb:
            string += i
    print(string)
    
def arethmetic():
    a = int(input())
    b = int(input())
    s = 0
    d = 0

    while a % 3 != 0:
        a += 1

    for i in range(a, b + 1, 3):
        s += i
        d += 1

    print(s / d)

def any():
    a = int(input()) #50
    b = []

    for i in range(1, a + 1):
        if len(b) >= a:
            break
        b += [i] * i
    print(*b[:a])


a = (int(i) for i in input().split())
b = int(input())
c = 0
s = []

for i in a:
    if i == b:
        s.append(c)
    c += 1

if s == []:
    print("Отсутствует")
else:
    print(*s)
