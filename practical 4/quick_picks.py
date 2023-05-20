# Quick picks

import random

NUM_QUICK_PICKS = 5
MIN_NUM = 1
MAX_NUM = 45
NUM_PER_QUICK_PICK = 6

def generate_quick_pick():
    """Generates a single quick pick (line of 6 random numbers)"""
    nums = []
    while len(nums) < NUM_PER_QUICK_PICK:
        num = random.randint(MIN_NUM, MAX_NUM)
        if num not in nums:
            nums.append(num)
    nums.sort()
    return nums

# Ask user for number of quick picks to generate
num_quick_picks = int(input("How many quick picks? "))

# Generate and print the quick picks
for i in range(num_quick_picks):
    quick_pick = generate_quick_pick()
    print(" ".join("{:2d}".format(num) for num in quick_pick))
