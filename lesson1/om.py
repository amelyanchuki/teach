def amper():
    a = float(input("Введите силу тока: "))
    return a

def volt():
    v = float(input("Введите напряжение в цепи: "))
    return v

def om():
    o = float(input("Введите сопративление: "))
    return o

def main():
    a = amper()
    v = volt()
    o = om()
    if a == 0:
        print(v / o, "Amper")
    elif v == 0:
        print(a * o, "Volt")
    else:
        print(v / a , "Om")

main()

