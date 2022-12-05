a = ["asasdd", ['123', 123, '12322'], [1, 2, "assa", 225], 155423, "skjhsa", "2321", 1253, "asdasf"]
b = []
c = []
d = []
for i in a:
    print(type(i))
    if type(i) == str:
        b.append(i)
        
    elif type(i) == int:
        c.append(i)
        
    else:
        d.append(i)

    
   
print(a)
print("все строки из списка",b)
print("все целочисленные", c)
print("всё остольное",d)