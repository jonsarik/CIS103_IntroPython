# Created by Jonathan Sarkarati
# 11/5/23
# Homework 5, Problem 1
# Find the Hypotenuse
# To be translated into C++

def main():
    print_intro()           # Program description

    leg1 = get_leg1()       # Get first leg
    while leg1:
        leg2 = get_leg2()   # Get second leg
        print()
        # Calculate and return the result
        hypot = get_hypot(leg1, leg2)
        result = (f'The length of the hypotenuse is {hypot:,.2f}')
        print(result)
        print('-'*len(result))

        # More triangles?
        print('\nRun again?', end='')
        leg1 = get_leg1()

    exit_program()

# Explain purpose of program
def print_intro():
    print("""
+===================================================+
| This program calculates the hypotenuse of a right |
| triangle when the other two sides are known.      |
+===================================================+""")

#  Get and validate the first leg
def get_leg1():
    print()
    sideA = input("Enter the length of the first leg"
                  "\nof the triangle, or 0 to exit: ")
    if sideA.lower() == 'o':
        return False
    while float(sideA) < 0:
        sideA = input('Please enter a valid number: ')
    return float(sideA)

# Get and validate the second leg
def get_leg2():
    print()
    sideB = input("Enter the length of the second leg"
                  "\nof the triangle: ")
    while float(sideB) < 0:
        sideB = input('Please enter a valid number: ')
    return float(sideB)

# Calculate the hypotenuse as A^2 + B^2 = C^2
def get_hypot(sideA, sideB):
    return (sideA**2 + sideB**2)**(1/2)

# End program
def exit_program():
    print()
    print('Exiting program...')
    print('Goodbye!')

if __name__ == '__main__':
    main()
