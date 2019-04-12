# letting the user choose when it quit
prompt = "Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
		
message = ""

while message != "quit":
	message = input(prompt)
	if (message != "quit"):
		print(message)
	
# using a flag
active = True
while active:
	message = input(prompt)
	if message != "quit":
		print(message)
	else:
		active = False

