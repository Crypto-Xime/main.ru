
print('*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*')
print()

import this


a = 5
print('*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*')
print()
print(a)
print('*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*')

# Programming example Number 1
def outer():

    def inner():
        print("I am in the scope of test_function")

    inner()
outer()

# Programming example Number 2

#Assigning Values
def test_function():
    def inner_function():
        print("I am in the scope of test_function")

    # Call inner_function inside test_function
    inner_function()

# Call test_function
test_function()

# Try calling inner_function outside of test_function
try:
    inner_function()  # This will raise an error
except NameError as e:
    print(f"Error: {e}")

