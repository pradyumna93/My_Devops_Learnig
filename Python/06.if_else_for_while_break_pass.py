# ✅ **1. if, elif, else Statements**

### ✔ **Simple if**


age = 20

if age >= 18:
    print("You are an adult")


### ✔ **if–else**


age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")


### ✔ **if–elif–else**

'''
marks = 75

if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
else:
    print("Fail")
'''



# ✅ **2. for Loop**

# Used for looping through a sequence (list, tuple, string, range).

### ✔ Example 1: Loop through a list

'''
fruits = ["apple", "banana", "mango"]

for item in fruits:
    print(item)
'''

### ✔ Example 2: Using range()

'''
for i in range(1, 6):  
    print(i)
'''

# #Output: `1 2 3 4 5`



# ✅ **3. while Loop**

# Runs until a condition becomes False.

### ✔ Example:

'''
i = 1

while i <= 5:
    print(i)
    i += 1
'''



# 🚫 **4. break Statement**

# Used to **exit the loop immediately**.

### ✔ Example:

'''
for i in range(1, 10):
    if i == 5:
        break
    print(i)
'''

#Output: `1 2 3 4`



# 🔁 **5. continue Statement**

# Used to **skip the current iteration** and move to next.

### ✔ Example:

'''
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
'''

#Output: `1 2 4 5`



# 🕳 **6. pass Statement**

# Used as a **placeholder** when empty code is needed.

### ✔ Example:

'''
for i in range(5):
    pass   # TODO: write logic later
'''
