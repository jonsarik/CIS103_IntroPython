# Created by Jonathan Sarkarati
# 9/23/23
# Roulette Wheel Colors
# This program prompts and displays color patterns on a roulette wheel.

print('\nThis program will tell you the color of any '
      'pocket on a roulette wheel.\n')

# Get a number 0 through 36 from user
pocket=int(input('Please enter the number of the pocket between 0 and 36: '))

# Determine if pocket is odd or even, where true is odd
parity = pocket % 2

# Display the colors for odd/even numbered pockets
OUTPUT = "The color of the pocket is"

if (pocket == 0): print(f'{OUTPUT} green.')
elif 1 <= pocket <= 10:
    if parity: print(f'{OUTPUT} red.')
    else: print(f'{OUTPUT} black.')
elif 11 <= pocket <= 18:
    if parity: print(f'{OUTPUT} black.')
    else: print(f'{OUTPUT} red.')
elif 19 <= pocket <= 28:
    if parity: print(f'{OUTPUT} red.')
    else: print(f'{OUTPUT} black.')
elif 29 <= pocket <= 36:
    if parity: print(f'{OUTPUT} black.')
    else: print(f'{OUTPUT} red.')    
else: print('***Please enter a valid pocket between 0 and 36***')
