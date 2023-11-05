# Jonathan Sarkarati
# 10/29/2023
# Chapter 2, Exercise 18(c) from
# The Practice of Computing Using Python, 3rd Ed

def main():
    print_intro()           # Program description

    # Controlling the loop
    another_num = 'y'
    while another_num == 'y' or another_num == 'Y':
        limit = get_num()   # Get valid number
        run_num(limit)      # Print the pattern
                
        # Do it again?
        another_num = input('Run it again? (y = yes): ')
    exit_program()
        
# Explain purpose of program
def print_intro():
    print()
    print('\nThis program calculates and displays the sum of consecutive\n'
          'integers if the sum is divisble by the number of operands!')

# Get and validate positive number
def get_num():
    limit=int(input('\nPlease enter a positive integer greater than zero: '))
    while limit <= 0:
        print('That is not a valid number for this exercise.')
        limit = int(input('\nPlease enter a positive whole number: '))
    return limit

# Run the numbers for input
def run_num(limit):
    sum = 0
    operands = 0
    print()
    for row in range(1, limit+1):
        sum += row      # Sum of each row
        operands += 1   # Number of operands for each row
        
        # If sum is divisble by number of operands, show sum of integers
        if sum % operands == 0:     
            for column in range(1, row+1):                
                if column != row:
                    print(f'{column}+', end='') # Adds '+' between each integer in row
                else:
                    print(f'{column}', end='')  # Adds '=' at end of row
                    print(f' = {sum}')
    print('\nDo you notice a pattern?\n')

# End program
def exit_program():
    print()
    print('Exiting program...')
    print('Goodbye!')

if __name__ == '__main__':
    main()
