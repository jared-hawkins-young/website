i = 0
list01 = []

while i < 5:
    list01.append(input('Enter a number for the first list: '))
    i = i + 1

print('List 1: ', list01)

k = 0
list02 = []

while k < 5:
    list02.append(input('Enter a number for the second list: '))
    k = k + 1

list03 = []

for elem in list01:
    if elem in list02:
        list03.append(elem)

print('Common list: ', list03)