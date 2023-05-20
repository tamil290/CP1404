
#2. Debugging

"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

LOW_SCORE = 0
MAX_SCORE = 100
PASS_SCORE = 50
HIGH_SCORE = 90

score = float(input("Enter score: "))
if score < LOW_SCORE or score > MAX_SCORE:
    print("Invalid score")
elif score > PASS_SCORE:
    print("Passable")
elif score > HIGH_SCORE:
    print("Excellent")
else:
    print("Bad")