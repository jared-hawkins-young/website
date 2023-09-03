i = 0
list = []

while i < 5:
    list.append(input('Enter a word: '))
    i = i + 1

s = ''
for elem in list:
    s = s + " " + elem

print('Words: ', list)
print('One String: ', s)