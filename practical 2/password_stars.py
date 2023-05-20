# Password

def main():
    MIN_PASSWORD_LENGTH = 9
    password = get_password(MIN_PASSWORD_LENGTH)
    print_password(password)

def get_password(MIN_PASSWORD_LENGTH):
    password = input("Enter a password: ")
    while len(password) < MIN_PASSWORD_LENGTH:
        print(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long")
        password = input("Enter a password: ")
    return password


def print_password(password):
    print("*" * len(password))



main()
