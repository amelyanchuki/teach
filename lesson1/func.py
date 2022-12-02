def func():
    s = ["asd", 523, 111]
    return s

aaa = func()

def func1():
    for a in aaa:
        print(f"в функции находится {type(aaa)} со значениями {a}")

func1()

def func2(x, a, count = 1):
    if a == False:
        return x
    elif count >= 10:
        return count
    else:
        return a

print(func(1))

def up(*args):
    first = []
    for s in args:
        for i in s:
            if i[0].isupper() == True:
                first.append(i)
            else:
                first.append(i.capitalize())
    return first



a = ["ilya", "Vova", "alex"]
s = ["luda", "Grisha", "dasha"]
d = ["sveta", "Sasha", "Lexa"]
t = up(a, s, d)
print(t)
