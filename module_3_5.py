# Recursion = a function that calls itself from within, helps to visualize
# a complex problem into basic steps.
# Problems can be solved more easily iteratively than recursively upon the case.
# Iterative = Faster, Complex
# Recursive = Slower, Simpler

# Writing a function and assigning values
# Convert the number to string representation
def get_multiplied_digits(number):
    str_number = str(number)
    if len(str(number)) <= 1:
        return int(str_number)

    first = int(str_number[0])
    return first * get_multiplied_digits(int(str_number[1:]))

# Function Usage
result = get_multiplied_digits(9986755)
print(result)

def multiply_digits(num_str):
    if not num_str:
        return 1

    first_digit = (num_str[0])
    return first_digit * multiply_digits(num_str[1:])

# Function Usage
print(f"Final result: {result}")

# PROCESS NUMBER 2
def get_multiplied_digits1(number):
    str_number = str(number)
    if len(str(number)) <= 1:
        return int(str_number)

    first = int(str_number[0])
    return first * get_multiplied_digits1(int(str_number[-1:]))

# Function Usage
result = get_multiplied_digits1(9986755)
print(f"Second Final Result: ", result)



