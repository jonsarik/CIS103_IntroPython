# Created by Jonathan Sarkarati
# 11/5/23
# Homework 5, Problem 2
# Temperature Conversion
# To be translated into C++

# Constants
CEL_MIN = 0             # Celsius minimum
CEL_MAX = 100           # Celsius maximum
FAHR_MIN = 32           # Fahrenheit minimum
FAHR_MAX = 212          # Fahrenheit maximum
NUM_ROWS = 31           # Number of rows per column for Fahrenheit
NUM_ROWS2 = 26          # Number of rows per column for Celsius
def main():
    print_intro()       # Program description
    print_fahr_cel()    # Display Fahrenheit to Celsius table
    print()
    print_cel_fahr()    # Display Celsius to Fahrenheit table
    exit_program()

# Explain purpose of program
def print_intro():
    print("""
+============================================================================================+
| This program displays two tables of temperatures converted to both Fahrenheit and Celsius. |
+============================================================================================+""")

# Calculate and display Fahrenheit to Celsius table
def print_fahr_cel():
    # Display table for Fahrenheit
    print()
    print('Conversion of Fahrenheit to Celsius:')
    print()
    column1 = (f'Fahrenheit\tCelsius\t')*6
    print(f'{column1}')
    print(f'{len(column1)*'-'}-----')

    tally2 = FAHR_MIN + NUM_ROWS        # Control 2nd Fahrenheit column
    tally3 = FAHR_MIN + NUM_ROWS * 2    # Control 3rd Fahrenheit column
    tally4 = FAHR_MIN + NUM_ROWS * 3    # Control 4th Fahrenheit column
    tally5 = FAHR_MIN + NUM_ROWS * 4    # Control 5th Fahrenheit column
    tally6 = FAHR_MIN + NUM_ROWS * 5    # Control 6th Fahrenheit column

    # 1st column of Fahrenheit conversions
    for fahrenheit in range(FAHR_MIN, FAHR_MIN+NUM_ROWS):

        # 2nd column of Fahrenheit conversions
        for fahrenheit2 in range(FAHR_MIN+NUM_ROWS, FAHR_MIN+NUM_ROWS*2 + 1):
            if fahrenheit2 != tally2:
                continue

            # 3rd column of Fahrenheit conversions
            for fahrenheit3 in range(FAHR_MIN+NUM_ROWS * 2, FAHR_MIN+NUM_ROWS * 3 + 1):
                if fahrenheit3 != tally3:
                    continue

                # 4th column of Fahrenheit conversions
                for fahrenheit4 in range(FAHR_MIN + NUM_ROWS * 3, FAHR_MIN+NUM_ROWS*4 + 1):
                    if fahrenheit4 != tally4:
                        continue

                    # 5th column of Fahrenheit conversions
                    for fahrenheit5 in range(FAHR_MIN + NUM_ROWS * 4, FAHR_MIN+NUM_ROWS*5 + 1):
                        if fahrenheit5 != tally5:
                            continue

                        # 6th column of Fahrenheit conversions
                        for fahrenheit6 in range(FAHR_MIN + NUM_ROWS * 5, FAHR_MAX + 1):
                            if fahrenheit6 != tally6:
                                continue

                            print(
                                f'\t{fahrenheit:3}\t\t{convert_to_celsius(fahrenheit):5.1f}'
                                f'\t\t{fahrenheit2:3}\t\t{convert_to_celsius(fahrenheit2):6.1f}'
                                f'\t\t{fahrenheit3:3}\t\t{convert_to_celsius(fahrenheit3):6.1f}'
                                f'\t\t{fahrenheit4:4}\t{convert_to_celsius(fahrenheit4):6.1f}'
                                f'\t\t{fahrenheit5:4}\t{convert_to_celsius(fahrenheit5):6.1f}'
                                f'\t\t{fahrenheit6:4}\t{convert_to_celsius(fahrenheit6):6.1f}')

                        # Continue printing when final column for Fahrenheit reaches max
                        if tally6 > FAHR_MAX:
                            print(
                                f'\t{fahrenheit:3}\t\t{convert_to_celsius(fahrenheit):5.1f}'
                                f'\t\t{fahrenheit2:3}\t\t{convert_to_celsius(fahrenheit2):6.1f}'
                                f'\t\t{fahrenheit3:3}\t\t{convert_to_celsius(fahrenheit3):6.1f}'
                                f'\t\t{fahrenheit4:4}\t{convert_to_celsius(fahrenheit4):6.1f}'
                                f'\t\t{fahrenheit5:4}\t{convert_to_celsius(fahrenheit5):6.1f}')

        tally2 += 1
        tally3 += 1
        tally4 += 1
        tally5 += 1
        tally6 += 1
    print(f'{len(column1) * '-'}-----')

# Calculate and display Celsius to Fahrenheit table
def print_cel_fahr():
    print()
    print('Conversion of Celsius to Fahrenheit:')
    print()
    column2 = (f'Celsius\tFahrenheit\t') * 4
    print(f'{column2}')
    print(f'{len(column2) * '-'}--')

    cel_tally2 = NUM_ROWS2          # Control 2nd Celsius column
    cel_tally3 = NUM_ROWS2 * 2      # Control 3nd Celsius column
    cel_tally4 = NUM_ROWS2 * 3      # Control 4nd Celsius column

    # 1st column of Celsius conversions
    for celsius in range(CEL_MIN, NUM_ROWS2):

        # 2nd column of Celsius conversions
        for celsius2 in range(NUM_ROWS2, NUM_ROWS2 * 2):
            if celsius2 != cel_tally2:
                continue

            # 3rd column of Celsius conversions
            for celsius3 in range(NUM_ROWS2 * 2, NUM_ROWS2 * 3):
                if celsius3 != cel_tally3:
                    continue

                # 4th column of Celsius conversions
                for celsius4 in range(NUM_ROWS2 * 3, CEL_MAX + 1):
                    if celsius4 != cel_tally4:
                        continue

                    print(
                        f'{celsius:5}\t{convert_to_fahrenheit(celsius):7}'
                        f'\t\t{celsius2:5}\t{convert_to_fahrenheit(celsius2):7}'
                        f'\t\t{celsius3:5}\t{convert_to_fahrenheit(celsius3):7}'
                        f'\t\t{celsius4:5}\t{convert_to_fahrenheit(celsius4):7}')

                # Continue printing when final column for Celsius reaches max
                if cel_tally4 > CEL_MAX:
                    print(
                        f'{celsius:5}\t{convert_to_fahrenheit(celsius):7}'
                        f'\t\t{celsius2:5}\t{convert_to_fahrenheit(celsius2):7}'
                        f'\t\t{celsius3:5}\t{convert_to_fahrenheit(celsius3):7}')
        cel_tally2 += 1
        cel_tally3 += 1
        cel_tally4 += 1
    print(f'{len(column2) * '-'}--')

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(degree):
    return (degree * 9/5) + 32

# Convert Fahrenheit to Celsius
def convert_to_celsius(degree):
    return (degree - 32) * 5/9

# End program
def exit_program():
    print()
    print('Exiting program...')
    print('Goodbye!')

if __name__ == '__main__':
    main()
