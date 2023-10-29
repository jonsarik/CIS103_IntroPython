# Created by Jonathan Sarkarati
# 10/3/23
# Population
# This program predicts the size of a poppulation of organisms.

print('\nThis program calculates the approximate population of organisms' +
      '\nfor a given starting population, growth rate, and total days.')

# Get starting population, growth rate, and days.
starting_pop = int(input('\nEnter the number of organisms ' +
                         'you want to start with: '))
while starting_pop <= 0:    # Validate for starting population
    print('\nPlease pick a nonnegative number and try again.')
    starting_pop = int(input('Enter the number of starting organisms: '))

daily_growth = float(input('Enter the average daily ' +
                           'population growth as a percentage (%): '))
total_days = int(input('Enter the number of days the organisms ' +
                       'are left to multiply: '))
while total_days <= 0:      # Validate for days
    print('\nPlease pick a nonnegative number and try again.')
    total_days = int(input('Enter the number of days: '))

# Show variables and set table
print()
print('Starting number of organisms:', starting_pop)
print(f'Average daily increase: {daily_growth:.0f}%')
print('Number of days to multiply:', total_days)

print()
print('Day\tApproximate Population')
print('------------------------------')

# Calculate and display population growth as
# starting population times the growth rate
# raised to the power of the number of days
for day in range (total_days):
    population = starting_pop * ((1 + daily_growth/100)**(day))
    if population < 1E8: print(f'{day+1}\t{population:>14,.3f}')
    else: print(f'{day+1}\t{population:>14.3E}')
