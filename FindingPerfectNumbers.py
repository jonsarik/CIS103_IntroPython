# Created by Jonathan Sarkarati
# 11/2/23
# Derived from Chapter 5, Exercise 2.1.6 in
# The Practice of Computing Using Python, 3rd Ed
# Finding Perfect Numbers
import math

def main():
    print_intro()               # Program description

    number = get_number()       # Range of numbers to evaluate
    print()
    while number:
        for integer in range(1, number +1):     # Evaluate each number in range
            total = check_divisors(integer)     # Get sum of divisors
            get_result(integer, total)          # Evaluate sum with number
        
        # Any more to evaluate?
        number = get_number()
        print()
        
    exit_program()
        
# Explain purpose of program
def print_intro():
    print("""
+===========================================+
| This program evaluates numbers and labels |
| them as perfect, deficient, or abundant!  |
+===========================================+""")

#   Get a number to evaluate
def get_number():
    print()
    number = input("Enter a positive number for range of"
                   "\nintegers to evaluate, or 0 to exit: ")
    if number.lower() == 'o':
        return False
    while int(number) < 0:
        number = input('Please enter a valid number: ')
    return int(number)

# Find divisors and their sum
def check_divisors(limit):
    sum = 0
    for divisor in range(1, limit):
        if limit % divisor == 0:            
            sum += divisor
    return sum

# Evaluate the result
def get_result(number, sum):
    if number == sum:
        print(number, 'is perfect!')
    elif number > sum:
        print(number, 'is deficient.')
    else:
        print(number, 'is abundant.')

# End program
def exit_program():
    print()
    print('Exiting program...')
    print('Goodbye!')

if __name__ == '__main__':
    main()
