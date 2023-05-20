# Score with Menu




LOW_SCORE = 0
MAX_SCORE = 100
PASS_SCORE = 50
HIGH_SCORE = 90

Menu = """G - Get a valid score
P - Print result
S - show stars
Q - Quit"""


def main():
    score = get_valid_score()
    while True:
        print(Menu)
        choice = input("Enter your choice: ")
        if choice.upper() == "G":
            score = get_valid_score()
        elif choice.upper() == "P":
            print(get_result(score))
        elif choice.upper() == "S":
            print_stars(score)
        elif choice.upper() == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


def get_valid_score():
    score = int(input("Enter a score between 0 and 100: "))
    if score < LOW_SCORE or score > MAX_SCORE:
      print("Invalid score. Try again.")
    else:
      return score

def print_stars(score):
    print("*" * score)

def get_result(score):
    if score < LOW_SCORE or score > MAX_SCORE:
        return "Invalid score"
    elif score >= PASS_SCORE and score < HIGH_SCORE:
        return "Passable"
    elif score >= HIGH_SCORE:
        return "Excellent"
    else:
        return "Bad"




main()
