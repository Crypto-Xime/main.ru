def sum_number_and_lengths(iterable):
    total_sum = 0
    total_length = 0

    def recursive_helper(item):
        nonlocal total_sum, total_length  # Access outer variables
        if isinstance(item, (int, float)):
            total_sum += item
        elif isinstance(item, str):
            total_length += len(item)
        elif isinstance(item, dict):
            for key, value in item.items():
                recursive_helper(key)
                recursive_helper(value)
        elif isinstance(item, (list, tuple, set)):
            for sub_item in item:
                recursive_helper(sub_item)

    recursive_helper(iterable)
    return total_sum, total_length

# Example Usage
data_structure = [1, 2, 3, 4]  # Sum: 10
value_data = {'a': 5, 'b': 6, 'c': 7}  # Sum: 18
data = (6, {'cube': 7, 'drum': 8})  # Sum: 21
string_value = "Hello"  # Length: 5
structure = (10, ('Urban', 5), ('Urban2', 35))  # Sum: 37, Length: 11

# Combine all data into a single iterable
combined_data = [
    data_structure,
    value_data,
    data,
    string_value,
    structure
]

# Calculate results
result_sum, result_length = sum_number_and_lengths(combined_data)

# Print Results
print('*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*')
print('Sum of numbers:', result_sum)
print('Length of Strings:', result_length)
print('*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*')
