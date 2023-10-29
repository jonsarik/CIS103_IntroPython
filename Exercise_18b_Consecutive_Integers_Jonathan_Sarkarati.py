# Jonathan Sarkarati
# 10/9/2023
# Chapter 2, Exercise 18(b) from
# The Practice of Computing Using Python, 3rd Ed

print('\nThis program calculates and shows the sum of consecutive numbers.')
limit=int(input('Please enter a positive whole number: '))
# Validate input > 0
while limit <= 0:
    print('\nThat is not a valid number for this exercise.')
    limit=int(input('Please enter a positive integer greater than zero: '))
print()

# Show each row adding a consecutive integers starting with 1 to the limit.
# Reset sum to zero for each row
for row in range(1, limit+1):
    sum=0

    # Add consecutive integers as columns
    for column in range(1, row+1):
        sum +=column
        if column != row:
            print(f'{column}+', end='') # Adds '+' between each integer in row
        else:
            print(f'{column}', end='')  # Adds '=' at end of row
    print(f'={sum}')
