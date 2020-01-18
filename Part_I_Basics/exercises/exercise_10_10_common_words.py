# 10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/ )
# and find a few texts you’d like to analyze. Download the text files for these
# works, or copy the raw text from your browser into a text file on your
# computer.

# You can use the count() method to find out how many times a word or
# phrase appears in a string. For example, the following code counts the number
# of times 'row' appears in a string:

# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3

# Notice that converting the string to lowercase using lower() catches
# all appearances of the word you’re looking for, regardless of how it’s
# formatted.
# Write a program that reads the files you found at Project Gutenberg and
# determines how many times the word 'the' appears in each text.

file_names = ["exercise_10_10_little_women.txt",
              "exercise_10_10_alice.txt"]
key_word = "the"

for file_name in file_names:
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
            count = contents.lower().count(key_word)

    except FileNotFoundError:
        print("Sorry, the file " + file_name + " dose not exist.")

    else:
        print("The word " + "'" + key_word + "'" + " appears " + str(count)
              + " times in the book.")
