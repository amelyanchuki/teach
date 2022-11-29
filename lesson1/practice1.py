import os

mp4 = []
another = []

for i, a, d in os.walk("D:\\films"):
    for name in d:
        if "mp4" in name:
            mp4.append(name)
            mp4.append(i)
        elif "zip" in name:
            continue
        else:
            another.append(name)
            another.append(i)
            print(f"файл {name} находится в {i}")
