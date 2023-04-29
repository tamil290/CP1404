# guitar test

from Guitar import Guitar


def main():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1000)

    print(f"{guitar1} get_age() - Expected 101. Got {guitar1.get_age()}")
    print(f"{guitar2} get_age() - Expected 10. Got {guitar2.get_age()}")
    print(f"{guitar1} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2} is_vintage() - Expected False. Got {guitar2.is_vintage()}")


main()
