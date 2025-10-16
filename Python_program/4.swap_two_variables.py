a = 5
b = 10

# method 1: Using a temporary variable
temp = a
a = b
b = temp    

print("After swapping (using temporary variable):")
print("Value of a:", a)
print("Value of b:", b) 

# method 2: Without using a temporary variable
a = 5
b = 10
a, b = b, a 
print("After swapping (without using temporary variable):")
print("Value of a:", a)
print("Value of b:", b) 

# method 3: Using arithmetic operations
a = 5
b = 10
a = a + b  # a now becomes 15
b = a - b  # b becomes 5
a = a - b  # a becomes 10   
print("After swapping (using arithmetic operations):")
print("Value of a:", a)
print("Value of b:", b) 
# method 4: Using bitwise XOR operator      
a = 5
b = 10
a = a ^ b  # a now becomes 15 (binary 1111)
b = a ^ b  # b becomes 5 (binary 0101)
a = a ^ b  # a becomes 10 (binary 1010)
print("After swapping (using bitwise XOR operator):")
print("Value of a:", a)
print("Value of b:", b) 
# --- IGNORE ---
# method 5: Using Python's tuple unpacking
a = 5
b = 10
a, b = b, a
print("After swapping (using tuple unpacking):")
print("Value of a:", a)
print("Value of b:", b) 
# --- IGNORE ---        


# method 6: Using list