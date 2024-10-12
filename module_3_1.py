                                              # Call Counter Task

# Creating Variables and Functions
calls = 0
string_info1 = 'Gears of War,'
string_info2 = 'Armageddon,'

# Executing the Program:

def count_calls():
    global calls
    calls += 1

for i in string_info1:
    count_calls()
    length = len(string_info1)
    upper = string_info1.upper()
    lower = string_info1.lower()
    print(length, upper, lower)
    break

for j in string_info2:
    count_calls()
    length = len(string_info2)
    upper = string_info2.upper()
    lower = string_info2.lower()
    print(length, upper, lower)
    break

def is_contains(string, list_to_search):
    count_calls()  # Count the call
    string_lower = string.lower()
    return any(item.lower() == string_lower for item in list_to_search)

#String indexing Method

is_contains1 = 'Judgement'
upper = is_contains1.upper()
lower = is_contains1.lower()
print(upper,",", lower, ",", is_contains1[::2],"," ,is_contains1[5:9],",", is_contains1[::-1])

# Specific Handling for True False Statements Given
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # True
print(is_contains('cycle', ['recycling', 'cyclic'])) #False

# Print the total number of calls
print(calls)


