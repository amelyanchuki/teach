a = "qwertyuiopasdfghjklzxcvbnm"
b = input("writ text \t")
string = " "
for i in a:
    if i not in b:
        string += i
print(string)
