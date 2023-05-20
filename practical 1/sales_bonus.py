#1. Sales Bonus

"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

BONUS_RATE_LOW = 0.1  # 10%
BONUS_RATE_HIGH = 0.15 # 15%


while True:
    sales = float(input("Enter sales: $"))
    if sales < 0:
        break
    elif sales < 1000:
        bonus = sales * BONUS_RATE_LOW
    else:
        bonus = sales * BONUS_RATE_HIGH
    print("Your bonus amount is: $", bonus)



