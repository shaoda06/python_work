# 10-5. Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all the responses.

while True:
    reason = input("Why do you like programming?\nEnter 'quit' to stop.\n")

    file_name = "exercise_10_5_programming_poll.txt"
    if reason == "quit":
        break
    else:
        with open(file_name, "a") as file_project:
            file_project.write(reason + "\n")
