go = 0
nums = []
while go == 0:
    n = input('Enter a number or QUIT to quit: ')
    if n == 'QUIT':
        go = 1
    else:
        nums.append(int(n))
eNums = []

for elem in nums:
    if (elem % 2) == 0:
        eNums.append(elem)

print('All nums: ', nums)
print('Even nums: ', eNums)