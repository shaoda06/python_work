# 10.1.2 File Paths
with open(r"text_files\example_10_1_2_pi_digits.txt") as file_object:
    content = file_object.read()
    print(content.rstrip())

# Absolute paths are usually longer than relative paths, so it's helpful
# to store them in a variable and the npass that variable to open()
file_path = r"C:\Users\MrrNonsense\Desktop\python_work\text_files" \
            r"\example_10_1_2_pi_digits.txt "
with open(file_path) as file_object:
    content = file_object.read()
    print(content.rstrip())

# Using absolute paths, you can read files from any location on your system.
# For now it’s easiest to store files in the same directory as your program
# files or in a folder such as text_files within the directory that stores your
# program files.

# Note:  Windows systems will sometimes interpret forward slashes in file paths
# correctly. If you’re using Windows and you’re not getting the results you
# expect, make sure you try using backslashes.
