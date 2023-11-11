# Created by Jonathan Sarkarati
# 11/5/23
# Homework 5, Problem 1
# Find the Hypotenuse
# To be translated into C++

def main():
    print_intro()  # Program description
    leg1 = get_leg("first")         # Get first leg of triangle
    while leg1:
        leg2 = get_leg("second")    # Get second leg of triangle

        # Get the hypotenuse
        hypotenuse = get_hypot(leg1, leg2)
        result = f'The length of the hypotenuse is {hypotenuse:,.2f}'
        print()
        print(result)
        print('-' * len(result))

        # More calculations?
        leg1 = get_leg("first")
    exit_program()

# Explain purpose of program
def print_intro():
    print("""
+===================================================+
| This program calculates the hypotenuse of a right |
| triangle when the other two sides are known.      |
+===================================================+""")

#  Get and validate triangle leg
def get_leg(leg):
    if leg == "first":
        print()
        side = input(f'Enter the length of the {leg} leg'
                     '\nof the triangle, or 0 to exit: ')
        if side.lower() == 'o':
            return False
    else:
        print()
        side = input(f'Enter the length of the {leg} leg'
                     '\nof the triangle: ')
    while float(side) < 0:
        side = input('Please enter a valid number: ')
    return float(side)

# Calculate the hypotenuse using the Pythagorean Theorem
def get_hypot(sideA, sideB):
    return (sideA ** 2 + sideB ** 2) ** (1 / 2)

# End program
def exit_program():
    print()
    print('Exiting program...')
    print('Goodbye!')

if __name__ == '__main__':
    main()
