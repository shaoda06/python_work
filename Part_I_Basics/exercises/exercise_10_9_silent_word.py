# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either file is missing.

file_names = ["exercise_10_8_cats.txt", "exercise_10_8_dogs.txt"]
for file_name in file_names:
    try:
        with open(file_name) as file_object:
            print("There are names in file " + "'" + file_name + "'")

            for line in file_object:
                print(line.rstrip())

    except FileNotFoundError:
        pass
