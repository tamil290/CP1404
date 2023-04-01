# Exceptions Demo

"""
CP1404/CP5632 - Practical
Answer the following questions:

1. When will a ValueError occur?
 A ValueError will occur if the user enters a non-integer value (e.g. a letter or a decimal number)
  for either the numerator or denominator.

2. When will a ZeroDivisionError occur?
  A ZeroDivisionError will occur if the user enters 0 as the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
 Yes, we could change the code to avoid the possibility of a ZeroDivisionError by adding an
  additional check before the calculation to ensure that the denominator is not 0.

"""


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)


except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
