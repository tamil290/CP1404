# Shop Calculator

"""
Shop Calculator
CP1404/CP5632 - Practical
"""

MIN_ITEMS = 0
DISCOUNT_RATE = 0.9

while True:
   no_of_items = int(input("Number of items: "))
   if no_of_items < MIN_ITEMS:
      print("Invalid number of items!")
   else:
       break

total_price = 0
for i in range(no_of_items):
    while True:
       item_cost = float(input("Price of item: $ "))
       if item_cost < 0:
           print("Invalid price!")
       else:
           break
    total_price += item_cost

if total_price >= 100:
    total_price *= DISCOUNT_RATE

print(f"Total price for {no_of_items} items is ${total_price:.2f}")

