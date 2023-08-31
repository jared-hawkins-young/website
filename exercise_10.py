s = input("Enter a string: ")

str = list(s)

newList = []

for k in range(0, len(str), 3):
    new = []
    for i in range(0, 3):
        if (k + i) < len(list):
            new.append(list[k + i])
    newList.append(new)
print(newList)

