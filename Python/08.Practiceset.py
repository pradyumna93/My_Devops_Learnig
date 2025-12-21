# Write a program that prints: Hello, World! Welcome to Python.
print("Hello, World! Welcome to Python.")

# Write a program that prints the following poem using a single print() statement:
# Twinkle, twinkle, little star,
# How I wonder what you are!

print("Twinkle, twinkle, little star,\nHow I wonder what you are!")

# Create variables to store: - Your name (string)
# - Your age (integer)
# - Your height in meters (float)
# - A boolean value representing whether you are a student
# Print all of them in one line.

Name = "Pradyumna"
age = 32
height = 5.4
student = False

print(f"My Name is {Name}, age = {age}, height = {height} and you are student:{student}")

# You are given a string:
# num = "45"
# Convert it into an integer and add 10 to it. Print the result.

num = "45"
num1 = int(num)
print(num1+10)

# Write a program that:
# Asks the user for their favorite food. and print Wow! I also like {food}

food = input("Enter your favorite food : ")
print(f"Wow! I also like {food}")

# Write a program that:
# Takes two numbers as input from the user.
# Prints their sum, difference, product, and quotient.

num1 = int(input("Enter the first numner : "))
num2 = int(input("Enter the second numner : "))

print(f"The Sum of two number is {num1+num2}\nThe difference between two number is {num1-num2}\nThe product between two number is {num1*num2}\nThe quotient between two number is {num1/num2}")

# Print the following output using escape sequences:
# Harry said, "Python is awesome!"
# This is on a new line.
# This is a tab -> <- here

print('Harry said, "Python is awesome!"\nThis is on a new line.\nThis is a tab ->\t<- here')

# Write a program that:
# Takes an integer as input from the user.
# Prints the square and cube of that number.

num = int(input("Enter an integer : "))
c = num**2
d = num**3
print(c)
print(d)


