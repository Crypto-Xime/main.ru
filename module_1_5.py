# List Creation
food = ("Banana", "Strawberry", "Coconut", "Pear")
print(food)
print(food[0] , food[3])

# Set Variables Of Different Data Types: Creating an immutable_var variable and Printing the Tuple to the screen
immutable_var = ["Coconut", 3, 4.5, True, "Strawberry"]
print("immutable_tuple:", immutable_var)

#Changing variable values attempt:
try:
    immutable_var[4] = 1     #This will raise an error
except TypeError as e:
    print(f"Error:, {e}")
print("Error: 'Tuple' object does not support item assignment")
# Explanation: Tuples in Python are immutable, meaning that once a tuple is created, its elements cannot be modified, added, or removed.
# This is different from lists. It ensures that the data stored in the tuple remains constant and unchanged throughout the program;
# Can be more memory efficient and faster; maintaining data integrity and optimizing performance in Python.

# Creating Mutable Data Structure:
mutable_list = [2, 4, "Strawberry", "Coconut"]

# Display The Original Mutable List:
print("Original mutable list:", mutable_list)

# Changing the Second Element and Adding a New Element:
mutable_list[1] = 6                   # Change the first element to 6
mutable_list.append('Modified')       #Add a New element to the end

#Displaying the Modified Mutable List
print("Modified mutable list:", mutable_list)










