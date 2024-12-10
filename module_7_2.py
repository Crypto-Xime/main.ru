                                    # Task "Write and remember":

def custom_write(file_name, strings):
    """
    Writes a list of strings to a file, each on a new line.
    Returns a dictionary of positions and their corresponding strings.

    :param file_name: Name of the file to write to
    :param strings: List of strings to write
    :return: Dictionary with line number and byte offset as keys, and strings as values
    """
    strings_positions = {}  # Dictionary to store positions and strings

    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            # Get the current byte position
            start_position = file.tell()
            # Write the string with a newline
            file.write(string + '\n')
            # Store the position and the string in the dictionary
            strings_positions[(line_number, start_position)] = string

    return strings_positions

# Example usage
info = [
    'Text for tell.',
    'Use utf-8 encoding.',
    'Because there are 2 languages!',
    'Thank you!'
]

result = custom_write('test.txt', info)

# Print the resulting dictionary
for elem in result.items():
    print(elem)