# Jonathan Sarkarati
# Programming exercise #6 from Chapter 2
# This program calculates and displays sales tax of a purchase

STATE_TAX_RATE = .05
COUNTY_TAX_RATE = .025

price=float(input('What is the price of the item? $'))  # Purchase price
state_tax = price * STATE_TAX_RATE                      # Calculate state tax
county_tax = price * COUNTY_TAX_RATE                    # Calculate local tax
total_price = price + state_tax + county_tax            # Calculate total price

# Display price information
print(f'Initial purchase price:  ${price:12,.2f}')
print(f'State tax due:           ${state_tax:12,.2f}')
print(f'County tax due:          ${county_tax:12,.2f}')
print(f'Total price after tax:   ${total_price:12,.2f}')
