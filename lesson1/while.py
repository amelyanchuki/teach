
a = input("введите число\t")
x = int(a)
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