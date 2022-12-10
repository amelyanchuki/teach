def chet():
    x = int(input("введите число\t"))
    while x < 100:
        y = 1 
        x += y
        if x % 2 != 0:
            continue
        if x == 100:
            print("x больше 100")
            break
        print(x)
    else:
        print(f"Х больше 100 или ввели строку длинной {len(x)} символа")

def summ_multipl():
    b = 0
    c = 0
    while True:
        a = int(input())
        c += a * a
        b += a
        if b == 0:
            print(c)
            break