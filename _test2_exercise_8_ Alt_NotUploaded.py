limit=int(input('Enter a number between 1 and 10: '))
print('\n------------------------------------------')
if limit != 1:
    print(f'sum of even integers less or equal to {limit} is:')
    sum = 0
    for row in range(2, limit+1, 2):
        sum+= row
        if row != 2:
            print(f' + ' + str(row), end='')
        else:
            print(f'' + str(row), end='')
    print(f' = {sum}')
    print('\n------------------------------------------\n')
print(f'sum of odd integers less or equal to {limit} is:')
sum = 0
for row in range(1, limit+1, 2):
    sum+= row
    if row != 1:
        print(f' + ' + str(row), end='')
    else:
        print(f'' + str(row), end='')
print(f' = {sum}')
print('\n------------------------------------------')
