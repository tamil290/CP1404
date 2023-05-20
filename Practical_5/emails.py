# Emails

# Initialize an empty dictionary
users = {}

# Loop until the user enters a blank email
while True:
    email = input("Email: ")
    if email == "":
        break
    # Split the email at the "@" symbol
    parts = email.split('@')
    # Take the first part (before the "@") and split it at the dots
    name_parts = parts[0].split('.')
    # Join the name parts with spaces and capitalize each word
    name = ' '.join(name_parts).title()
    # Ask the user if the extracted name is correct
    is_correct = input(f"Is your name {name}? (Y/n)").lower()
    if is_correct == "" or is_correct == "y":
        # Add the name to the dictionary using the email as the key
        users[email] = name
    else:
        # If the extracted name is not correct, ask the user for their name
        name = input("Name: ").title()
        users[email] = name

# Print out the users dictionary
for email, name in users.items():
    print(f"{name} ({email})")
