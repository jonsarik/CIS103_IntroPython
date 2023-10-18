# Created by Jonathan Sarkarati
# 10/3/23
# Pennies for Pay
# This program calculates your income if your pay doubled
# each day starting with a single penny.

print('\nThis program calculates your "salary" if you earned' +
      '\na penny that doubles for each day that follows!')
# Ask how many days user wants to track
days = int(input('\nHow many days do you want to track your pay: '))

# Make sure user picks a nonnegative number of days
while days <= 0:
    print ('\nPlease pick a day of one or more and try again.')
    days = int(input('How many days do you want to track: '))

pay = 0.0
# Calculate pay for each day doubling
for pennies in range(days):
    pay  += (2**pennies)/100

# Display total salary.
if pay < 1E12: print(f'Your total pay would be: ${pay:,.2f}')
else: print(f'Your total pay would be: ${pay:.3E}')
