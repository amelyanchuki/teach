a = "qwertyuiopasdfghjklzxcvbnm"
b = "good day"
string = " "
for i in a:
    if i not in b:
        string += i
print(string)
