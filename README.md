# itsc-3155-modules-1-and-2

# exercise 1
k = input("Enter a string: ")

upper = ""
lower = ""

for char in k:
    if char.isupper():
        upper += char
    elif char.islower():
        lower += char

result = lower + upper

print(result)