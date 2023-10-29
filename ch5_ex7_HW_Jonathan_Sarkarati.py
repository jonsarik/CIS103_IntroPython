# Created by Jonathan Sarkarati
# 10/25/23
# Paint Job Estimator
# This program calculates the total cost of a paint job.
import math

# Constants for labor and material
CONVERSION_PAINT = 112
HOURS_PER_112SF = 8
COST_PER_GALLON = 40
COST_LABOR = 35

def main():
    print_intro()   # Program description

    # Controlling the loop
    more_jobs = 'y'
    while more_jobs == 'y' or more_jobs == 'Y':
        wall_space = get_job_size()                     # Size of job       
        gallons = get_gallons(wall_space)               # Amount of paint
        hours = get_hours(wall_space)                   # Number of hours
        paint_cost = get_paint_cost(gallons)            # Cost of paint
        labor_cost = get_labor(hours)                   # Cost of labor
        sum_total = get_total(paint_cost, labor_cost)   # Job total
    
        # Print job details
        print_job(gallons, hours, paint_cost, labor_cost, sum_total)
        
        # Any more jobs?
        more_jobs = input('Do you have more jobs? (y = yes): ')
    exit_program()
        
# Explain purpose of program
def print_intro():
    print()
    print('This program calculates material and labor costs of a job')
    print('for the measured wall space in square feet.')

# Determine square footage of wall to be painted
def get_job_size():
    print()
    job_size = float(input('Square footage of walls to be painted? '))
    # Validate input
    while job_size <= 0:
        job_size = float(input('Please enter a valid square footage: '))
    return job_size

# Calculate gallons of paint needed per 112 sf rounded up
def get_gallons(wall):
    return math.ceil(wall / CONVERSION_PAINT)

# Calculate hours of labor for job per 112 sf rounded up
def get_hours(wall):
    return math.ceil(wall / CONVERSION_PAINT * HOURS_PER_112SF)

# Calculate cost of paint
def get_paint_cost(paint):
    return paint * COST_PER_GALLON

# Calculate cost of labor
def get_labor(total_hours):
    return total_hours * COST_LABOR

# Calculate total cost of job
def get_total(paint, labor):
    return paint + labor

# Show job details
def print_job(gallons, hours, paint_cost, labor_cost, sum_total):
    print()
    print('--------------------------------------------------')
    print(f'The number of gallons of paint required: {gallons:<3}')
    print(f'The hours of labor required: \t\t{hours:<3}')
    print(f'The cost of the paint:\t\t\t${paint_cost:>9,.2f}')
    print(f'The labor charges:\t\t\t${labor_cost:>9,.2f}')
    print(f'The total cost of the paint job:\t${sum_total:>9,.2f}')
    print('--------------------------------------------------')
    print()

# End program
def exit_program():
    print()
    print('Exiting program...')
    print('Goodbye!')

if __name__ == '__main__':
    main()
