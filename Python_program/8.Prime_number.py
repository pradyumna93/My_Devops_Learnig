num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
# This program checks whether a given number is prime or not.   

# list of prime numbers between 1 to 100
print("Prime numbers between 1 and 100 are:")
for num in range(1, 101):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num, end=' ')
# This program also lists all prime numbers between 1 and 100.
# This program checks whether a given number is prime or not.