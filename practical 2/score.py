"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

LOW_SCORE = 0
MAX_SCORE = 100
PASS_SCORE = 50
HIGH_SCORE = 90


def main():
    score = float(input("Enter score: "))
    print(get_result(score))
    random_score = random.randint(LOW_SCORE, MAX_SCORE)
    print(f"Random score ({random_score}): {get_result(random_score)}")

def get_result(score):
    if score < LOW_SCORE or score > MAX_SCORE:
        return "Invalid score"
    elif score > PASS_SCORE:
       return "Passable"
    elif score > HIGH_SCORE:
        return "Excellent"
    else:
        return "Bad"




main()