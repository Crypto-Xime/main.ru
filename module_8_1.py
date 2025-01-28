try:
    i = 0
    print(10 / i)
    print("Task done successfully")

except ZeroDivisionError:
    print("You can not divide by zero")
    print("*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*")

def add_everything_up(a , b):
    """
    Adds numbers or concatenates strings. If the types are mixed, return their string representation.

    :param a: The first input, can be int, float, or str
    :param b: The second input, can be int, float, or str
    :return: The result of addition or concatenation, or string representation of mixed types
    """
    try:
        #Attempt to add if types
        result = a + b
        return result
    except TypeError:
        # Handle case when types are mixed
        return str(a) + str(b)

# Example usage
print(add_everything_up(123.456, 'line'))  # Output: 123.456line
print(add_everything_up('Apple', 4215))    # Output: Apple4215
print(add_everything_up(123.456, 7))       # Output: 130.456
print("*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*")
