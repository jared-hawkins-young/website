
size = int(input('Enter a number: '))

list = []

x = 1

while x < size + 1:
    print('Enter number', x, ':', end = '')
    f = float(input())
    x = x + 1
    list.append(f)

print('List: ', list)

total = 0

for elem in list:
    total = total + elem

avg = total / size

print('Average: ', avg)