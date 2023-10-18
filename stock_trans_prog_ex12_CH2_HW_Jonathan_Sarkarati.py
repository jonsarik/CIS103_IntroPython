# Jonathan Sarkarati
# Programming exercise #12 from Chapter 2
# This program calculates and displays capital gain or loss

# Number and price of shares bought and sold
total_shares = 2000
share_price_initial = 40.00
share_price_sold = 42.75
BROKER_COMMISSION = .03

# Display stock transaction details
print('This program shows your net gain/loss in Acme Software stock.\n')
print(f'Total paid for shares bought @ ${share_price_initial:,.2f}:    ${total_shares * share_price_initial:10,.2f}')   # Price times shares
print(f'Commission paid at purchase:              ${share_price_initial * BROKER_COMMISSION * total_shares:10,.2f}\n')  # Commission paid at purchase

print(f'Amount received for shares sold @ ${share_price_sold}: ${share_price_sold * total_shares:10,.2f}')              # Price sold times shares
print(f'Commission paid at sale:                  ${share_price_sold * BROKER_COMMISSION * total_shares:10,.2f}\n')     # Commission paid at sale

# Calculate net gain or loss after commission
cost_basis = share_price_initial * (1 + BROKER_COMMISSION) * total_shares                                               # Total paid at purchase
proceeds = share_price_sold * (1 - BROKER_COMMISSION) * total_shares                                                    # Total gross at sale
print(f'Net gain or loss of transaction:          ${proceeds - cost_basis:10,.2f}')                                     # Proceeds minus cost basis
