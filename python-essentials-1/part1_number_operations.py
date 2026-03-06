# Part 1: Number Operations with Error Handling

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    # Try converting inputs to integers
    n1 = int(num1)
    n2 = int(num2)

    # Print sum
    print("Sum:", n1 + n2)

    # Handle division
    if n2 == 0:
        print("Cannot divide by zero")
    else:
        print("Division result:", n1 / n2)

except ValueError:
    print("Invalid input")