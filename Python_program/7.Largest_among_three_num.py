num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

#method 1
# if (num1 >= num2) and (num1 >= num3):
#     largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#     largest = num2
# else:
#     largest = num3

# print(f"The largest number is {largest}")   

#method 2
largest = max(num1, num2, num3)
print(f"The largest number is {largest}")
# --- IGNORE ---
# This program finds the largest among three numbers entered by the user.

