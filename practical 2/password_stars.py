# Password

SECRET_PASSWORD = "Cricket@1234"
user_password = str(input("Enter user_password: "))
if user_password == SECRET_PASSWORD:
    print("Access granted")
else:
    print("Access denied")


