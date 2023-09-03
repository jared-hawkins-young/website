row = input('Enter a row num from 1 to 5: ')

col = input('Enter a col num from 1 to 5: ')

i = 0
k = 0

ii = [int(row) - 1]

kk = [int(col) - 1]

for i in range(5):
    for k in range(5):
        if i in ii and k in kk:
            print('1 ', end = '')
            
        else:
            print('0 ', end = "")
        k = k + 1
    print()
    i = i + 1