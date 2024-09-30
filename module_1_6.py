# Create a variable my_dict and assign it a dictionary
my_dict = {
          "Name": "Ximena",
          "Year_Of_Birth": 1998,
          "City": "Guatemala"
}

# Display the dictionary
print(my_dict)

# Access existing Key
print("Name:", my_dict.get("name"))

# Access a Missing Key Safely
print("Country:", my_dict.get("Country", "Key not found"))

# Remove one of the pairs in the dictionary
print(my_dict)
my_dict.pop('Year_Of_Birth')
print(my_dict)

# Create a New Set
my_set = {'Ximena': 1998, 'Anton': 1986, 'Carolina': 1973}

# Print Existing Set
print("Existing set:", my_set)

#Add Two Values
my_set.update({'Paolo': 1979,
               'Luz': 1946})
print("Modified Set:", my_set)

# Remove one value fro my set
my_set.pop('Luz')
print("New Set:", my_set)

#print The deleted Values and the Final Modified Set
print("Deleted Value: Luz: 1946")
print("Final Modified Set:", my_set)
