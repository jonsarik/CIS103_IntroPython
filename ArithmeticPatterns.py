# Jonathan Sarkarati
# 10/9/2023
# Chapter 2, Exercise 21 from
# The Practice of Computing Using Python, 3rd Ed
# Updated 11/2/23

LIMIT = 9   # Constant for the number of rows

def main():
    print_intro()
    print_pattern1()
    print_pattern2()
    print_pattern3()
    print_pattern4()
    exit_program()      

# Explain purpose of program
def print_intro():
    print()
    print('This program generates arithmetic patterns using stings of numbers.')
    print()

# Display pattern of consecutive integers times eight plus row value.
def print_pattern1():
    for row in range(1, LIMIT+1):
        string=''
        for column in range(1, LIMIT+1):
            string = string + str(column)
            if column == row:
                sum = int(string) * (LIMIT-1) + row
                print(f'{string} * {LIMIT-1} + {row} = {sum}')
    print()

# Display pattern of consecutive integers times nine plus (row + 1) value.
def print_pattern2():
    for row in range(1, LIMIT+1):
        string=''
        for column in range(1, LIMIT+1):
            string = string + str(column)
            if column == row:
                sum = int(string) * LIMIT + (row + 1)
                print(f'{string} * {LIMIT} + {row + 1} = {sum}')
    print()
                
# Display pattern of decreasing integers times nine plus (row - 2) value.
def print_pattern3():
    for row in range(LIMIT, 1, -1):
        string=''
        for column in range(LIMIT, 1, -1):
            string = string + str(column)
            if column == row:
                sum = int(string) * LIMIT + (row - 2)
                print(f'{string} * {LIMIT} + {row  - 2} = {sum}')
    print()

# Display pattern of ever expanding series of ones times itself.
def print_pattern4():
    for row in range(1, LIMIT+1):
        string=''
        for column in range(1, LIMIT+1):
            string = string + str(column**0)
            if column == row:
                sum = int(string) * int(string)
                print(f'{string} * {string} = {sum}')
    print()

# End program
def exit_program():
    print('Press ENTER to exit program.')
    input()
    print('Exiting program...')
    print('Goodbye!')

if __name__ == '__main__':
    main()
