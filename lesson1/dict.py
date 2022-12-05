a = {"fng": 35261, "awf": 12351, "ilidan": 125167}



def vivers():
    c = {}
    for i, s in a.items():
        c[i] = s
    return c

def main():
    for key, val in vivers().items():
        print(f"сейчас стримит {key} и его смотрит {val} зрителей")


main()