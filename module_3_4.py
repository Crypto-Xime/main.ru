print('---------------------------------------------------------------------------')
# Creating the Output list of synonyms
def single_words(root_word, *other_words12):
    same_words = []
    root_word_lower = root_word.lower()

    # Loop through each word in other_words1
    for word in other_words12:
        word_lower = word.lower()  # Convert current word to lowercase

        # Add the matching word to the list
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    return sorted(same_words)  # Move return statement outside the loop

# Calls to the function with unpacking of lists
result1 = single_words('rich', 'richest', 'orichalcum')
result2 = single_words('Disablement', 'Able', 'Disable')

# Print the results
print(result1)  # Expected: ['orichalcum', 'richest', 'rich']
print(result2)  # Expected: ['Able', 'Disable']
print("Starting to find matches...")
print('---------------------------------------------------------------------------')

#Sorting words by synonyms
def categorize_words(root_words, other_words):
    categorized = {
        "Matched": {},
        "Others": []
    }

# Define relationships for matching
    matches_map = {
            'Hell': ['Tartarus', 'Purgatory', 'Sheol', 'Zion'],
            'Heaven': ['Riot', 'Lark', 'Good', 'Delight'],
            'thorn': ['tribulation'],
            # You can add more mappings if necessary
        }

# Loop through each root word to find matches
    for roots in root_words:
            if roots in matches_map:
                categorized["Matched"][roots] = matches_map[roots]
            else:
                categorized["Matched"][roots] = []  # No matches found

        # Collect words that didn't match any root word
    for word in other_words:
            if word not in categorized["Matched"].values():
                categorized["Others"].append(word)

    return categorized

# Provided lists of words
single_root_words = ('Hell','Tartarus', 'Purgatory', 'Sheol', 'Zion', 'thorn','bliss')
other_words1 = ('Heaven','Riot', 'Lark', 'tumble', 'Good', 'Delight', 'tribulation')

# Categorize words
result = categorize_words(single_root_words, other_words1)

# Print the results
for root, matches in result["Matched"].items():
    print(f"{root} = {', '.join(matches) if matches else 'None'}")
print(f"Heaven = {', '.join(result['Others']) if result['Others'] else 'None'}")
print('---------------------------------------------------------------------------')
