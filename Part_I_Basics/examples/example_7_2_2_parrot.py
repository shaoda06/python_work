# Letting the User Choose When to Quit
prompt = "Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."

message = ""

while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)

# Using a Flag
active = True
while active:
    message = input(prompt)
    if message != "quit":
        print(message)
    else:
        active = False
