list = []
uList = []
x = 1
while len(list) < 10:
    print('Enter number', x, ': ', end = '')
    list.append(int(input()))
    x = x + 1
print('Original List: ', list)
for elem in list:
    list.remove(elem)
    if elem not in list:
        uList.append(elem)
    


print('Nums that appear once: ', uList)