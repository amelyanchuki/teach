def func():
    s = ["asd", 523, 111]
    return s

# aaa = func()

def func1():
    for a in aaa:
        print(f"в функции находится {type(aaa)} со значениями {a}")


def func2(x, a, count = 1):
    if a == False:
        return x
    elif count >= 10:
        return count
    else:
        return a

def up(*args):
    first = []
    for s in args:
        for i in s:
            if i[0].isupper() == True:
                first.append(i)
            else:
                first.append(i.capitalize())
    return first


def f(x):
    if x <= -2:
        a = 1 - (x + 2)**2
        return a
    elif -2 < x <= 2:
        a = -x / 2
        return a
    else:
        a = (x - 2)**2 + 1
        return a

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def modify_list(lst):
    for i in lst[::-1]:
        if i % 2 != 0:
            lst.remove(i)
    f = 0
    for a in lst:
        d = a / 2
        lst.remove(a)
        lst.insert(f, int(d))
        f += 1

modify_list()
print(lst)
      