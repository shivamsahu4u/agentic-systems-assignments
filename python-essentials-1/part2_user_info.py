# Part 2: User Information and String Concatenation

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

age_input = input("Enter your age: ")

try:
    # Try converting age to integer
    age = int(age_input)

    # Check for negative age
    if age < 0:
        print("Age cannot be negative")
    else:
        full_name = first_name + " " + last_name
        print("Full Name:", full_name)

        print("You will be", age + 1, "next year")

except ValueError:
    # Handle invalid age input
    print("Invalid age input")