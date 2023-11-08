# Created by Jonathan Sarkarati
# 11/5/23
# Homework 5, Problem 2
# Temperature Conversion
# To be translated into C++

# Constants
CEL_MIN = 0         # Celsius minimum
CEL_MAX = 100       # Celsius maximum
FAHR_MIN = 32       # Fahrenheit minimum
FAHR_MAX = 212      # Fahrenheit maximum
NUM_ROWS = 51       # Number of rows per column
def main():
    print_intro()   # Program description
    print_chart()   # Display conversion table
    exit_program()

# Explain purpose of program
def print_intro():
    print("""
+=========================================================================================+
| This program displays a table of temperatures converted to both Fahrenheit and Celsius. |
+=========================================================================================+""")

# Calculate and display conversion table
def print_chart():
    print()
    column1 = (f'Fahrenheit\tCelsius\t')*4
    column2 = (f'\tCelsius\tFahrenheit')*2
    print(f'{column1}||{column2}')
    print(f'{len(column1)*'-'}{len(column2)*'-'}--------')

    tally2 = FAHR_MIN+NUM_ROWS          # Control 2nd Fahrenheit column
    tally3 = FAHR_MIN+NUM_ROWS * 2      # Control 3rd Fahrenheit column
    tally4 = FAHR_MIN+NUM_ROWS * 3      # Control 4th Fahrenheit column

    cel_tally = CEL_MIN                 # Control 1st Celsius column
    cel_tally2 = CEL_MIN + NUM_ROWS  # For 2nd Celsius column

    # 1st column of Fahrenheit conversions
    for fahrenheit in range(FAHR_MIN, FAHR_MIN+NUM_ROWS):

        # 2nd column of Fahrenheit conversions
        for fahrenheit2 in range(FAHR_MIN+NUM_ROWS, FAHR_MIN+NUM_ROWS*2+1):

            # 3rd column of Fahrenheit conversions
            for fahrenheit3 in range(FAHR_MIN+NUM_ROWS*2, FAHR_MIN+NUM_ROWS*3 +1):

                # 1st column of Celsius conversions
                for celsius in range(NUM_ROWS):

                    # 2nd column of Celsius conversions
                    for celsius2 in range(NUM_ROWS, CEL_MAX + 1):

                        # 4th column of Fahrenheit conversions
                        for fahrenheit4 in range(FAHR_MIN+NUM_ROWS*3, FAHR_MAX + 1):

                            if celsius == cel_tally and celsius2 == cel_tally2 and fahrenheit2 == tally2 and fahrenheit3 == tally3 and fahrenheit4 == tally4:
                                print(
                                    f'\t{fahrenheit:3}\t\t{convert_to_celsius(fahrenheit):5.1f}'
                                    f'\t\t{fahrenheit2:3}\t\t{convert_to_celsius(fahrenheit2):6.1f}'
                                    f'\t\t{fahrenheit3:3}\t\t{convert_to_celsius(fahrenheit3):6.1f}'
                                    f'\t\t{fahrenheit4:4}\t{convert_to_celsius(fahrenheit4):6.1f}'
                                    f'\t||\t{celsius:5}\t{convert_to_fahrenheit(celsius):7}'
                                    f'\t\t{celsius2:5}\t{convert_to_fahrenheit(celsius2):7}')

                        # Continue printing when final column for Fahrenheit reaches max
                        if tally4 > FAHR_MAX:
                            if celsius == cel_tally and celsius2 == cel_tally2 and fahrenheit2 == tally2 and fahrenheit3 == tally3:
                                print(
                                    f'\t{fahrenheit:3}\t\t{convert_to_celsius(fahrenheit):5.1f}'
                                    f'\t\t{fahrenheit2:3}\t\t{convert_to_celsius(fahrenheit2):6.1f}'
                                    f'\t\t{fahrenheit3:3}\t\t{convert_to_celsius(fahrenheit3):6.1f}'
                                    f'\t\t\t\t\t\t||\t{celsius:5}\t{convert_to_fahrenheit(celsius):7}'
                                    f'\t\t{celsius2:5}\t{convert_to_fahrenheit(celsius2):7}')

                    # Continue printing when final columns for Celsius and Fahrenheit reach max
                    if cel_tally2 > CEL_MAX:
                        if celsius == cel_tally and fahrenheit2 == tally2 and fahrenheit3 == tally3:
                            print(
                                f'\t{fahrenheit:3}\t\t{convert_to_celsius(fahrenheit):5.1f}'
                                f'\t\t{fahrenheit2:3}\t\t{convert_to_celsius(fahrenheit2):6.1f}'
                                f'\t\t{fahrenheit3:3}\t\t{convert_to_celsius(fahrenheit3):6.1f}'
                                f'\t\t\t\t\t\t||\t{celsius:5}\t{convert_to_fahrenheit(celsius):7}')

        tally2 += 1
        tally3 += 1
        tally4 += 1
        cel_tally += 1
        cel_tally2 += 1
    print(f'{len(column1) * '-'}{len(column2) * '-'}--------')

#  Convert Celsius to Fahrenheit
def convert_to_fahrenheit(degree):
    return (degree * 9/5) + 32

#  Convert Fahrenheit to Celsius
def convert_to_celsius(degree):
    return (degree - 32) * 5/9

# End program
def exit_program():
    print()
    print('Exiting program...')
    print('Goodbye!')

if __name__ == '__main__':
    main()
