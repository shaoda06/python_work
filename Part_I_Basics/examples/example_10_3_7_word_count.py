# 10.3.7 Working with Multiple Files


def count_words(file_name):
    """Count the approximate number of words in a file."""
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + file_name + " dose not exist."
        print(msg)
        # 10.3.8 Failing Silently
        # In the previous example, we informed our users that one of the
        # files was unavailable. But you don’t need to report every exception
        # you catch. Sometimes you’ll want the program to fail silently when
        # an exception occurs and continue on as if nothing happened. To make
        # a program fail silently, you write a try block as usual, but you
        # explicitly tell Python to do nothing in the except block. Python
        # has a pass statement that tells it to do nothing in a block:

        # pass

    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + file_name + " has about " + str(num_words)
              + " words.")


file_name = "example_10_3_6_alice.txt"
count_words(file_name)

file_names = ['example_10_3_6_alice.txt', 'example_10_3_7_siddhartha.txt',
              'example_10_3_7_moby_dick.txt', 'example_10_3_7_little_women.txt']

for file_name in file_names:
    count_words(file_name)
