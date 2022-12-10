def sort():
    a = ["asasdd", ['123', 123, '12322'], [1, 2, "assa", 225], 155423, "skjhsa", "2321", 1253, "asdasf"]
    b = []
    c = []
    d = []
    for i in a:
        print(type(i))
        if type(i) == str:
            b.append(i)
            
        elif type(i) == int:
            c.append(i)
            
        else:
            d.append(i)

        
    
    print(a)
    print("все строки из списка",b)
    print("все целочисленные", c)
    print("всё остольное",d)

def summ_sosed():
    a = input().split()
    b = []
    c = 0

    for i in a:
        if len(a) > 1:
            if c == 0:
                b.append(int(a[c + 1]) + int(a[len(a) - 1]))
                c += 1
            elif c == len(a) - 1:
                b.append(int(a[c - 1]) + int(a[0]))
                c = 0
            else:
                b.append(int(a[c - 1]) + int(a[c +1]))
                c += 1
        else:
            b.append(i)

    print(*b)

def sort_spiska():
    a = [int(i) for i in input().split()]
    a.sort()
    b = []
    for i in a:
        if a.count(i) > 1:
            if b.count(i) > 0:
                continue
            else:
                b.append(i)
        
    print(*b)


