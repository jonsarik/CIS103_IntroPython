# Jonathan Sarkarati
# 10/9/2023
# Chapter 2, Exercise 21 from
# The Practice of Computing Using Python, 3rd Ed

print('\nThis program generates arithmetic patterns.')
print()

# Constant for the number of rows
LIMIT = 9

# Show pattern #1 of consecutive integers times eight plus row value.
for row in range(1, LIMIT+1):
    string=''
    for column in range(1, LIMIT+1):
        string = string + str(column)
        if column != row:
            continue
        if column == row:
            sum = int(string) * 8 + row
            print(f'{string} * 8 + {row} = {sum}')
print()
# Show pattern #2 of consecutive integers times nine plus (row + 1) value.
for row in range(1, LIMIT+1):
    string=''
    for column in range(1, LIMIT+1):
        string = string + str(column)
        if column != row:
            continue
        else:
            sum = int(string) * 9 + (row + 1)
            print(f'{string} * 9 + {row + 1} = {sum}')
print()
# Show pattern #3 of decreasing integers times nine plus (row - 2) value.
for row in range(LIMIT, 1, -1):
    string=''
    for column in range(LIMIT, 1, -1):
        string = string + str(column)
        if column != row:
            continue
        else:
            sum = int(string) * 9 + (row - 2)
            print(f'{string} * 9 + {row  - 2} = {sum}')
print()
# Show pattern #4 of ever expanding series of ones times itself.
for row in range(1, LIMIT+1):
    string=''
    for column in range(1, LIMIT+1):
        string = string + str(column**0)
        if column != row:
            continue
        else:
            sum = int(string) * int(string)
            print(f'{string} * {string} = {sum}')
