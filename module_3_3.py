                                        # "Unpacking positional parameters".

# Objective of the task: To master the creation of functions with default parameters
# And the practice of calling these functions with different numbers of arguments.

# Task "Unpacking":

def print_params(a: int = 4,
                 b: int = 8,
                 c: int =10):
    print(a, b, c)
    print(a + c)

print_params(8, True, 14)
print('------------------------------------------------------------')
print_params(a = 12)
print_params( 10,2,6)
print('------------------------------------------------------------')

# Creating Values List to Assign values

list1_ = {'a': 10, 'b': 'Seven Deadly Sins', 'c': 144}
dict_ = {'d': 100, 'e': 37.05, 'f': 26}

def print_params1(**kwargs):
    for key in kwargs:
        print(key)

print_params1(**dict_)

def print_params1(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_params1(**dict_)
print('------------------------------------------------------------')

def print_params2(*args):
    for value in args:
        print(value)

print_params1(**list1_)
print('------------------------------------------------------------')
