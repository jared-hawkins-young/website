b = input("Enter a string: ")

upper = ""
lower = ""

for char in b:
    if char.isupper():
        upper += char
    elif char.islower():
        lower += char

result = lower + upper

print(result)