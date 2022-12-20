a = {"fng": 35261, "awf": 12351, "ilidan": 125167}

def vivers():
    c = {}
    for i, s in a.items():
        c[i] = s
    return c

def main():
    for key, val in vivers().items():
        print(f"сейчас стримит {key} и его смотрит {val} зрителей")

d = {}

def update_directory(d, key, value):
    if key in d:
        d[key] += [value]
    elif key not in d:
        if 2*key in d:
            d[2*key] += [value]
        elif 2*key not in d:
            d[2*key] = [value]

c = {}
b = input().lower().split()

for i in b:
    if i in c:
        c[i] += 1
    elif i not in c:
        c[i] = 1

for key, val in c.items():
    print(key, val)

def f(x):
    return x + 123

d = {}
n = int(input())
a = int(input())
nn = 0
while n != nn:
    if a in d:
        print(d[a])
    elif a not in d:
        d[a] = f(a)
        print(d[a])
    nn += 1
    if nn == n:
        break
    a = int(input())
