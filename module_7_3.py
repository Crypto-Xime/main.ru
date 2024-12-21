import string  # task: "Find everywhere"

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)  # Store file names as a list

    def get_all_words(self):
        """
        Reads words from each file and returns a dictionary
        mapping file names to lists of words.
        """
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    words = []
                    for line in file:
                        # Convert to lowercase and remove punctuation
                        line = line.lower()
                        line = line.translate(str.maketrans("", "", string.punctuation))
                        words.extend(line.split())
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"File '{file_name}' not found. Skipping file.")
            except Exception as e:
                print(f"An error occurred while processing '{file_name}': {e}")
        return all_words

    def find(self, word):
        """
        Finds the first occurrence of the word in each file's word list.
        Returns a dictionary with file names as keys and word positions as values.
        """
        word = word.lower()
        all_words = self.get_all_words()
        if not all_words:
            raise ValueError("No valid files were processed. Check file paths and content.")

        word_positions = {}
        for file_name, words in all_words.items():
            try:
                position = words.index(word) + 1  # Index + 1 for 1-based position
                word_positions[file_name] = position
            except ValueError:
                word_positions[file_name] = None  # Word not found
        return word_positions

    def count(self, word):
        """
        Counts occurrences of the word in each file's word list.
        Returns a dictionary with file names as keys and word counts as values.
        """
        word = word.lower()
        all_words = self.get_all_words()
        if not all_words:
            raise ValueError("No valid files were processed. Check file paths and content.")

        word_counts = {}
        for file_name, words in all_words.items():
            count = words.count(word)
            word_counts[file_name] = count
        return word_counts


# Example Usage
finder = WordsFinder('test_file.txt')

# Get all words
print("All words in files:", finder.get_all_words())

# Find the first occurrence of the word "TEXT"
print("First occurrence of 'TEXT':", finder.find('TEXT'))

# Count the occurrences of the word "TEXT"
print("Count of 'TEXT':", finder.count('teXT'))