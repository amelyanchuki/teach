def func():
    s = ["asd", 523, 111]
    return s

aaa = func()

def func1():
    for a in aaa:
        print(f"в функции находится {type(aaa)} со значениями {a}")

func1()