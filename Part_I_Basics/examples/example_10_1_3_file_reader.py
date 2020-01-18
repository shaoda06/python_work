# 10.1.3 Reading Line By Line
file_name = "example_10_1_1_pi_digits.txt"

with open(file_name) as file_object:
    # for line in file_object:
    #     print(line)

    for line in file_object:
        # using rstrip() on each line in the print statement eliminates these
        # extra blank lines:
        print(line.rstrip())
