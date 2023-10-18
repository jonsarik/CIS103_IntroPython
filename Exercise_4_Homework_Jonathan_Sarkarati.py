# Created by Jonathan Sarkarati
# 9/23/23
# Roman Numerals
# This program prompts and displays Roman numerals for numbers 1-10.

print('\nThis program will show you the Roman numeral\n'
      'for numbers between 1 and 10.\n')

# Get a number 1-10 from the user
numeral=int(input('Please enter a number from 1-10: '))

# Display Roman numerals
OUTPUT = "The Roman numeral equivalent is"

if (numeral == 1): print(f'{OUTPUT} I.')
elif (numeral == 2): print(f'{OUTPUT} II.')
elif (numeral == 3): print(f'{OUTPUT} III.')
elif (numeral == 4): print(f'{OUTPUT} IV.')
elif (numeral == 5): print(f'{OUTPUT} V.')
elif (numeral == 6): print(f'{OUTPUT} VI.')
elif (numeral == 7): print(f'{OUTPUT} VII.')
elif (numeral == 8): print(f'{OUTPUT} VIII.')
elif (numeral == 9): print(f'{OUTPUT} IX.')
elif (numeral == 10): print(f'{OUTPUT} X.')
else: print('***Please enter a valid number between 1 and 10***')
