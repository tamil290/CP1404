# files




# 1


name = input("Enter name: ")

"""Open the file for reading"""
file = open("name.txt", "w")

"""write the file"""
file.write(name)

"""close file"""
file.close()


# 2


"""Open the file for reading"""
file = open("name.txt", "r")
name = file.read()

"""Print the name"""
print("Your name is", name)
file.close()


# 3

"""Open the file for reading"""
file = open("numbers.txt", "r")

"""Read the numbers from the file and convert them to integers"""
number1 = int(file.readline().strip())
number2 = int(file.readline().strip())

"""Add the two numbers together"""
result = number1 + number2

"""Print the result"""
print(result)

"""Close the file"""
file.close()



# 4



"""Open the file for reading"""
file = open("numbers.txt", "r")

"""Initialize the total to zero"""
total = 0

"""Loop through each line in the file"""
for line in file:
    # Convert the line to an integer and add it to the total
    number = int(line)
    total += int(number)

"""Print the total"""
print(total)

"""Close the file"""
file.close()






