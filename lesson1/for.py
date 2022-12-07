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
