a = (123, "asd", 1222, 123, "asd", "dsa", "dsa")
b = a
w = 0
for i in a :
    for q in b:
        if q == i:
            w += 1
        
print(f"в кортеже 'а' {len(a)} элементов из которых {int((w - len(a))/2)} повтора")